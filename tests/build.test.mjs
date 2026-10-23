// Kelengkapan build: setiap modul bermateri dan setiap butir verified di repositori masuk ke situs,
// commit sumber tercatat, dan aset lokal diberi penanda versi agar cache browser tidak memakai data lama.
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

test("build rilis memuat semua modul bermateri dan semua butir verified dari commit yang dibangun", () => {
  const out = fs.mkdtempSync(path.join(os.tmpdir(), "osnk-build-"));
  try {
    execFileSync("node", [path.join(ROOT, "scripts/build.mjs"), "--release", "--out", out],
      { env: { ...process.env, GITHUB_SHA: "abc1234def5678" } });
    const ctx = {};
    new Function("window", fs.readFileSync(path.join(out, "data.js"), "utf8"))(ctx);
    const d = ctx.OSNK_DATA;
    assert.equal(d.commit, "abc1234def5678");

    const modules = JSON.parse(fs.readFileSync(path.join(ROOT, "content/modules/modules.json"), "utf8"));
    assert.deepEqual(d.modules.map((m) => m.id), modules.map((m) => m.id), "daftar modul = modules.json");
    for (const m of d.modules) {
      const hasMd = fs.existsSync(path.join(ROOT, "content/modules", `${m.id}.md`));
      assert.equal(m.ready, hasMd, `${m.id}: status ready`);
      if (hasMd) assert.ok(m.material.length > 500, `${m.id}: materi kosong`);
    }

    const qdir = path.join(ROOT, "content/questions");
    const verified = fs.readdirSync(qdir).filter((f) => f.endsWith(".json"))
      .flatMap((f) => JSON.parse(fs.readFileSync(path.join(qdir, f), "utf8")))
      .filter((q) => q.verification_status === "verified").map((q) => q.id).sort();
    assert.deepEqual(d.questions.map((q) => q.id).sort(), verified, "semua butir verified ikut, tidak lebih");
    for (const m of d.modules.filter((x) => x.ready)) {
      assert.ok(d.questions.some((q) => q.module_id === m.id), `${m.id}: modul bermateri tanpa soal`);
    }

    const html = fs.readFileSync(path.join(out, "index.html"), "utf8");
    for (const a of ["data.js", "js/app.js", "js/grader.js", "css/style.css"]) {
      assert.ok(html.includes(`${a}?v=abc1234def56`), `${a} tanpa penanda versi`);
    }
  } finally {
    fs.rmSync(out, { recursive: true, force: true });
  }
});
