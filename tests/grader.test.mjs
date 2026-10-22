import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const ctx = { globalThis: {} };
ctx.globalThis = ctx;
vm.runInNewContext(readFileSync(new URL("../web/js/grader.js", import.meta.url), "utf8"), ctx);
const { grade, parseRational, shuffle } = ctx.Grader;

const intQ = { answer_type: "integer", answer_spec: { value: "12" } };
const negQ = { answer_type: "integer", answer_spec: { value: "-3" } };
const zeroQ = { answer_type: "integer", answer_spec: { value: "0" } };
const ratQ = { answer_type: "rational", answer_spec: { value: "3/4" } };
const decQ = { answer_type: "decimal", answer_spec: { value: "2.5", tolerance: 0.01 } };
const chQ = { answer_type: "choice", answer_spec: { correct: "C" } };

test("integer: normal, spasi, tanda plus", () => {
  assert.equal(grade(intQ, "12").status, "correct");
  assert.equal(grade(intQ, " 1 2 ").status, "correct");
  assert.equal(grade(intQ, "+12").status, "correct");
  assert.equal(grade(intQ, "13").status, "incorrect");
});

test("integer: negatif (minus unicode) dan nol", () => {
  assert.equal(grade(negQ, "-3").status, "correct");
  assert.equal(grade(negQ, "−3").status, "correct");
  assert.equal(grade(negQ, "3").status, "incorrect");
  assert.equal(grade(zeroQ, "0").status, "correct");
  assert.equal(grade(zeroQ, "-0").status, "correct");
});

test("integer: input tidak sah dan kosong", () => {
  assert.equal(grade(intQ, "12.0").status, "invalid");
  assert.equal(grade(intQ, "2*6").status, "invalid");
  assert.equal(grade(intQ, "").status, "empty");
  assert.equal(grade(intQ, "   ").status, "empty");
});

test("rational: pecahan ekuivalen, desimal, koma", () => {
  for (const s of ["3/4", "6/8", "0.75", "0,75", "75/100"]) assert.equal(grade(ratQ, s).status, "correct", s);
  assert.equal(grade(ratQ, "-3/4").status, "incorrect");
  assert.equal(grade(ratQ, "3/0").status, "invalid");
  assert.equal(grade(ratQ, "abc").status, "invalid");
  assert.equal(grade({ answer_type: "rational", answer_spec: { value: "-2/6" } }, "-1/3").status, "correct");
  assert.equal(grade({ answer_type: "rational", answer_spec: { value: "5" } }, "10/2").status, "correct");
});

test("rational: bilangan besar tetap eksak", () => {
  const q = { answer_type: "rational", answer_spec: { value: "1/3" } };
  assert.equal(grade(q, "333333333333333333/1000000000000000000").status, "incorrect");
  assert.equal(grade(q, "333333333333333333/999999999999999999").status, "correct");
  const r = parseRational("10/4");
  assert.equal(r.n, 5n);
  assert.equal(r.d, 2n);
});

test("decimal: toleransi", () => {
  assert.equal(grade(decQ, "2.5").status, "correct");
  assert.equal(grade(decQ, "2.51").status, "correct");
  assert.equal(grade(decQ, "2,49").status, "correct");
  assert.equal(grade(decQ, "2.52").status, "incorrect");
  assert.equal(grade(decQ, "5/2").status, "invalid");
});

test("choice dan self_check", () => {
  assert.equal(grade(chQ, "C").status, "correct");
  assert.equal(grade(chQ, "c").status, "correct");
  assert.equal(grade(chQ, "B").status, "incorrect");
  assert.equal(grade({ answer_type: "self_check", answer_spec: {} }, "").status, "manual");
});

test("shuffle: tidak menggandakan/menghilangkan, kunci opsi tetap", () => {
  let seed = 7;
  const rand = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
  const choices = ["A", "B", "C", "D", "E"].map((id) => ({ id, text: "opsi " + id }));
  for (let k = 0; k < 50; k++) {
    const s = shuffle(choices, rand);
    assert.equal(s.map((c) => c.id).sort().join(), "A,B,C,D,E");
    assert.equal(s.find((c) => c.id === "C").text, "opsi C");
  }
  assert.equal(choices.map((c) => c.id).join(), "A,B,C,D,E", "asli tidak berubah");
});
