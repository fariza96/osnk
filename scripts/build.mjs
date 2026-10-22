// Build situs statis: web/ (sumber tampilan) + content/ -> dist/
//   node scripts/build.mjs            semua butir (status non-verified diberi tanda DRAF)
//   node scripts/build.mjs --release  hanya butir verified
//   node scripts/build.mjs --questions DIR --out DIR   (dipakai tes)
import { marked } from "marked";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
const opt = (name, def) => (args.includes(name) ? args[args.indexOf(name) + 1] : def);
const RELEASE = args.includes("--release");
const QDIR = path.resolve(opt("--questions", path.join(ROOT, "content/questions")));
const OUT = path.resolve(opt("--out", path.join(ROOT, "dist")));

// Lindungi LaTeX dari Markdown: ganti $$..$$ / $..$ dengan placeholder, render, lalu kembalikan.
function md(src, inline = false) {
  if (!src) return "";
  const math = [];
  const keep = (m) => `@@M${math.push(m) - 1}@@`;
  let s = src.replace(/\$\$[\s\S]+?\$\$/g, keep).replace(/(?<!\\)\$(?:\\\$|[^$\n])+?\$/g, keep);
  s = inline ? marked.parseInline(s) : marked.parse(s);
  const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  return s.replace(/@@M(\d+)@@/g, (_, i) => esc(math[+i]));
}

const readJSON = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const modules = readJSON(path.join(ROOT, "content/modules/modules.json"));
const diagramDir = path.join(ROOT, "content/diagrams");

let questions = [];
for (const f of fs.existsSync(QDIR) ? fs.readdirSync(QDIR).sort() : []) {
  if (f.endsWith(".json")) questions.push(...readJSON(path.join(QDIR, f)));
}
const skipped = questions.filter((q) => q.verification_status !== "verified").length;
if (RELEASE) questions = questions.filter((q) => q.verification_status === "verified");
questions = questions.filter((q) => q.verification_status !== "quarantined");

const renderQ = (q) => ({
  id: q.id, module_id: q.module_id, domain: q.domain, role: q.role, difficulty: q.difficulty,
  subtopic: q.subtopic, minutes: q.estimated_minutes, tags: q.technique_tags,
  status: q.verification_status, answer_type: q.answer_type,
  answer_spec: q.answer_spec, answer_html: md(q.answer_spec.display, true),
  statement: md(q.statement), hints: q.hints.map((h) => md(h)), solution: md(q.solution),
  key_idea: md(q.key_idea), common_error: md(q.common_error),
  alternative: md(q.alternative_solution),
  choices: (q.choices || []).map((c) => ({ id: c.id, html: md(c.text, true) })),
  diagram: q.diagram ? fs.readFileSync(path.join(diagramDir, q.diagram), "utf8") : "",
  diagram_alt: q.diagram_alt || "",
});

const data = {
  built: new Date().toISOString(),
  release: RELEASE,
  modules: modules.map((m) => {
    const f = path.join(ROOT, "content/modules", `${m.id}.md`);
    return { ...m, ready: fs.existsSync(f), material: fs.existsSync(f) ? md(fs.readFileSync(f, "utf8")) : "" };
  }),
  questions: questions.map(renderQ),
};

fs.rmSync(OUT, { recursive: true, force: true });
fs.cpSync(path.join(ROOT, "web"), OUT, { recursive: true });
// "<" di-escape agar teks soal tidak dapat menutup tag <script>.
fs.writeFileSync(path.join(OUT, "data.js"),
  "window.OSNK_DATA = " + JSON.stringify(data).replace(/</g, "\\u003c") + ";\n");
const mj = path.join(ROOT, "node_modules/mathjax/es5");
fs.mkdirSync(path.join(OUT, "vendor/mathjax/output/chtml"), { recursive: true });
fs.copyFileSync(path.join(mj, "tex-chtml.js"), path.join(OUT, "vendor/mathjax/tex-chtml.js"));
fs.cpSync(path.join(mj, "output/chtml/fonts"), path.join(OUT, "vendor/mathjax/output/chtml/fonts"), { recursive: true });
fs.copyFileSync(path.join(ROOT, "node_modules/mathjax/LICENSE"), path.join(OUT, "vendor/mathjax/LICENSE"));

console.log(`dist: ${data.questions.length} butir, ${data.modules.filter((m) => m.ready).length} modul bermateri` +
  (RELEASE ? `, ${skipped} butir non-verified dikeluarkan` : `, ${skipped} butir belum verified (ditandai DRAF)`));
