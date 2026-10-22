// Tes validator + build + situs (Chromium via file:// dan subpath http seperti GitHub Pages).
import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import fs from "node:fs";
import http from "node:http";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const FIX = path.join(ROOT, "tests/fixtures");
const OUT = fs.mkdtempSync(path.join(os.tmpdir(), "osnk-dist-"));
const CHROME = process.env.CHROME_PATH || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";
let browser, server, base;

test("validator: fixture valid lolos, rilis menolak draf, fixture rusak ditolak", () => {
  const run = (...a) => spawnSync("python3", [path.join(ROOT, "scripts/validate.py"), ...a], { encoding: "utf8" });
  assert.equal(run("--dir", path.join(FIX, "valid")).status, 0);
  const rel = run("--dir", path.join(FIX, "valid"), "--release");
  assert.equal(rel.status, 1);
  assert.match(rel.stdout, /TB01-P002: status draft/);
  const bad = run("--dir", path.join(FIX, "invalid"));
  assert.equal(bad.status, 1);
  for (const pat of [/karakter kontrol/, /ID ganda/, /correct tidak menunjuk/, /hints harus tepat 2/]) assert.match(bad.stdout, pat);
});

before(async () => {
  execFileSync("node", [path.join(ROOT, "scripts/build.mjs"), "--questions", path.join(FIX, "valid"), "--out", OUT]);
  browser = await chromium.launch({ executablePath: CHROME });
  // Sajikan dist di subpath /repo/ untuk meniru situs proyek GitHub Pages.
  server = http.createServer((req, res) => {
    const u = decodeURIComponent(new URL(req.url, "http://x").pathname);
    if (!u.startsWith("/repo/")) { res.writeHead(404); return res.end(); }
    const f = path.join(OUT, u.slice(6) || "index.html");
    if (!f.startsWith(OUT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
    res.end(fs.readFileSync(f));
  }).listen(0);
  base = `http://127.0.0.1:${server.address().port}/repo/`;
});
after(async () => { await browser?.close(); server?.close(); fs.rmSync(OUT, { recursive: true, force: true }); });

async function open(url, width = 390) {
  const page = await browser.newPage({ viewport: { width, height: 800 } });
  // Situs harus berjalan tanpa internet: semua permintaan di luar file:// dan server lokal diblokir.
  await page.route(/^(?!file:|http:\/\/127\.0\.0\.1).*/, (r) => r.abort());
  const errors = [], failed = [];
  page.on("pageerror", (e) => errors.push(e.message));
  page.on("console", (m) => m.type() === "error" && errors.push(m.text()));
  page.on("requestfailed", (r) => failed.push(r.url()));
  page.on("response", (r) => r.status() >= 400 && failed.push(r.url()));
  await page.goto(url);
  return { page, errors, failed };
}
const mathReady = (page) => page.waitForFunction(() => document.querySelectorAll("mjx-container").length > 0, null, { timeout: 15000 });

test("build: data.js tidak dapat menutup <script>, tanpa panggilan API Claude", () => {
  const js = fs.readFileSync(path.join(OUT, "data.js"), "utf8");
  assert.ok(!js.includes("</"), "tidak ada '</' mentah");
  const g = spawnSync("grep", ["-rIl", "-i", "-E", "anthropic|api[_-]?key|x-api-key", OUT, "--exclude-dir=vendor"], { encoding: "utf8" });
  assert.equal(g.stdout.trim(), "", "tidak ada rujukan API/kunci di frontend");
});

for (const mode of ["subpath http", "file://"]) {
  test(`situs (${mode}): rumus, penilaian, petunjuk, progres setelah reload`, async () => {
    const url = mode === "file://" ? "file://" + path.join(OUT, "index.html") : base;
    const { page, errors, failed } = await open(url + "#/m/TB01");
    await mathReady(page);
    const art = page.locator("#TB01-P001");
    assert.match(await art.innerText(), /kutip/);
    // pecahan ekuivalen diterima, salah ditolak, kosong tidak dihitung
    const input = art.locator("input[type=text]"), btn = art.locator("button[data-act=check]"), fb = art.locator(".feedback");
    await btn.click(); assert.equal(await fb.innerText(), "Jawaban masih kosong.");
    await input.fill("2/3"); await btn.click(); assert.equal(await fb.innerText(), "Belum tepat.");
    await art.locator("details[data-n='1'] summary").click();
    await input.fill("0,75"); await btn.click(); assert.equal(await fb.innerText(), "Benar.");
    // pilihan ganda
    const ch = page.locator("#TB01-P002");
    await ch.locator("input[value=B]").check(); await ch.locator("button[data-act=check]").click();
    assert.equal(await ch.locator(".feedback").innerText(), "Benar.");
    assert.match(await ch.innerText(), /DRAF/);
    // progres bertahan setelah reload; bantuan petunjuk tercatat
    await page.reload(); await mathReady(page);
    assert.match(await page.locator("#TB01-P001").innerText(), /tuntas dengan bantuan/);
    assert.match(await page.locator("#TB01-P002").innerText(), /tuntas tanpa bantuan/);
    // tanpa scroll horizontal di lebar ponsel
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1));
    // cetak dengan pembahasan
    await page.goto(url + "#/cetak/TB01/pembahasan"); await mathReady(page);
    assert.match(await page.locator("main").innerText(), /Bagi dengan/);
    await page.goto(url + "#/cetak/TB01/soal"); await mathReady(page);
    assert.doesNotMatch(await page.locator("main").innerText(), /Bagi dengan/);
    assert.equal(await page.locator("mjx-merror").count(), 0, "tidak ada galat LaTeX");
    assert.deepEqual(errors, []);
    assert.deepEqual(failed, []);
    await page.close();
  });
}

test("situs: teks soal di-escape untuk LaTeX, HTML Markdown tetap dirender", async () => {
  const { page } = await open(base + "#/m/TB01", 1024);
  await mathReady(page);
  // "<b>tag</b>" dalam Markdown menjadi HTML (konten dipercaya, ditulis penulis); "a<b" di dalam $...$ tetap rumus.
  const n = await page.locator("#TB01-P001 mjx-container").count();
  assert.ok(n >= 3, `rumus dirender (${n})`);
  await page.close();
});
