// Tes tampilan konten nyata: setiap modul bermateri dirender tanpa galat LaTeX, tanpa jaringan,
// dan tanpa scroll horizontal di lebar ponsel (semua petunjuk/pembahasan dibuka).
import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright-core";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const OUT = fs.mkdtempSync(path.join(os.tmpdir(), "osnk-content-"));
const CHROME = process.env.CHROME_PATH || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";
const modules = JSON.parse(fs.readFileSync(path.join(ROOT, "content/modules/modules.json"), "utf8"))
  .filter((m) => fs.existsSync(path.join(ROOT, "content/modules", `${m.id}.md`)));
let browser;

before(async () => {
  execFileSync("node", [path.join(ROOT, "scripts/build.mjs"), "--out", OUT]);
  browser = await chromium.launch({ executablePath: CHROME });
});
after(async () => { await browser?.close(); fs.rmSync(OUT, { recursive: true, force: true }); });

for (const m of modules) {
  for (const route of [`m/${m.id}`, `cetak/${m.id}/pembahasan`]) {
    test(`konten ${route}: rumus valid, luring, muat di layar 390 px`, async () => {
      const page = await browser.newPage({ viewport: { width: 390, height: 900 } });
      const errors = [];
      await page.route(/^(?!file:).*/, (r) => r.abort());
      page.on("pageerror", (e) => errors.push(e.message));
      page.on("console", (msg) => msg.type() === "error" && errors.push(msg.text()));
      await page.goto("file://" + path.join(OUT, "index.html") + "#/" + route);
      await page.waitForFunction(() => document.querySelectorAll("mjx-container").length > 0, null, { timeout: 15000 });
      await page.evaluate(() => document.querySelectorAll("details").forEach((d) => (d.open = true)));
      await page.waitForTimeout(2500);
      const r = await page.evaluate(() => ({
        merror: [...document.querySelectorAll("mjx-merror")].map((e) => e.getAttribute("data-mjx-error") || e.textContent),
        rawDollar: [...document.querySelectorAll("main p, main li, main td")].filter((e) => /\$/.test(e.textContent)).map((e) => e.textContent.slice(0, 60)),
        overflow: document.documentElement.scrollWidth - window.innerWidth,
        svgs: document.querySelectorAll("figure.diagram svg").length,
      }));
      assert.deepEqual(r.merror, [], "galat LaTeX");
      assert.deepEqual(r.rawDollar, [], "tanda $ tidak terender");
      assert.ok(r.overflow <= 1, `scroll horizontal ${r.overflow}px`);
      assert.deepEqual(errors, []);
      await page.close();
    });
  }
}
