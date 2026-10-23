// Tes alat Tahap 5: audit lintas bank dan analisis uji coba (data sintetis di tests/fixtures/progress, bukan data siswa).
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const py = (...a) => execFileSync("python3", a, { cwd: ROOT, encoding: "utf8" });

test("audit lintas bank: komposisi 3/6/3 per modul dan semua objective_id ada di materi", () => {
  const out = py("scripts/audit_bank.py");
  assert.doesNotMatch(out, /komposisi tidak/);
  assert.doesNotMatch(out, /objective_id .* tidak ditemukan/);
  assert.doesNotMatch(out, /tidak tertulis apa adanya/);
});

test("analisis uji coba: berkas rusak dilewati, penanda kesulitan muncul, tanpa nama berkas", () => {
  const out = py("scripts/analyze_progress.py", "tests/fixtures/progress");
  assert.match(out, /Berkas progres valid: 6 \(1 berkas dilewati\)/);
  assert.match(out, /TB01-P001 \(fondasi\)/);
  assert.match(out, /TB01-P010 \(tantangan\)/);
  assert.doesNotMatch(out, /sintetis-|rusak/);
});
