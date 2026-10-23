// Aplikasi latihan statis. Data dari window.OSNK_DATA (dibuat scripts/build.mjs).
(function () {
  "use strict";
  const D = window.OSNK_DATA;
  const G = window.Grader;
  const $main = document.getElementById("main");
  const DOMAIN = { teori_bilangan: "Teori Bilangan", aljabar: "Aljabar", geometri: "Geometri", kombinatorika: "Kombinatorika" };
  const DIFF = { foundation: "Fondasi", core: "Inti", challenge: "Tantangan" };
  const byId = Object.fromEntries(D.questions.map((q) => [q.id, q]));
  const qsOf = (mid, role) => D.questions.filter((q) => q.module_id === mid && q.role === role);
  // Paket lintas modul (diagnostik, Latihan Campuran): butir dikenali dari prefiks ID.
  const PACKS = [
    { id: "DG", title: "Diagnostik", note: "16 soal, ±60 menit, dikerjakan mandiri sebelum program. Ringkasan per bidang di bawah menunjukkan bidang yang perlu diperkuat." },
    { id: "MX1", title: "Latihan Campuran 1", note: "20 soal dari modul 1–8 (akhir minggu 4), dikerjakan mandiri." },
    { id: "MX2", title: "Latihan Campuran 2", note: "20 soal dari modul 1–19 (minggu 10), dikerjakan mandiri." },
  ];
  const packQs = (pid) => D.questions.filter((q) => q.id.startsWith(pid + "-")).sort((a, b) => a.id.localeCompare(b.id));
  const packOf = (pid) => PACKS.find((p) => p.id === pid);
  // Modul rujukan sebuah butir: modulnya sendiri, atau modul pertama yang diujinya (butir paket).
  const homeModule = (q) => q.module_id || (q.prerequisites || [])[0];
  // Versi build di footer, agar guru dapat memastikan situs memakai commit terbaru.
  const $foot = document.querySelector("footer small");
  if ($foot && D.commit) {
    const v = document.createElement("span");
    v.className = "muted";
    v.textContent = ` Versi ${D.commit.slice(0, 7)} · dibangun ${String(D.built).slice(0, 10)}.`;
    $foot.after(v);
  }

  // ---- Progres lokal ----
  const KEY = "osnk-progres-v1";
  let P = {};
  try { P = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { P = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(P)); } catch (e) { /* mode privat */ } }
  function rec(id) {
    return (P[id] = P[id] || { attempts: 0, solved: false, solvedUnaided: false, hintsUsed: 0, solutionViewed: false, lastWrong: false });
  }

  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  function typeset(el) {
    // MathJax selesai inisialisasi secara asinkron; tunggu startup.promise sebelum typeset.
    const mj = window.MathJax;
    if (!mj || !mj.startup || !mj.startup.promise) return;
    mj.startup.promise = mj.startup.promise
      .then(() => { mj.typesetClear([el]); return mj.typesetPromise([el]); })
      .catch((e) => console.error(e));
  }
  function render(html, focus) {
    $main.innerHTML = html;
    typeset($main);
    if (focus) $main.focus();
  }
  const draftChip = (q) => (q.status !== "verified" ? `<span class="chip draft" title="Belum lolos audit">DRAF: ${esc(q.status)}</span>` : "");

  // ---- Halaman: daftar modul ----
  function viewHome() {
    const f = JSON.parse(sessionStorage.getItem("osnk-filter") || "{}");
    const banner = D.release ? "" : `<p class="chip draft">Build pengembangan: butir belum verified ikut tampil dan ditandai.</p>`;
    render(`<h1>Modul</h1>${banner}
      <div class="filters" role="search">
        <label class="sr">Bidang <select id="fDom"><option value="">Semua bidang</option>${Object.entries(DOMAIN).map(([k, v]) => `<option value="${k}">${v}</option>`).join("")}</select></label>
        <label class="sr">Kesulitan <select id="fDiff"><option value="">Semua kesulitan</option>${Object.entries(DIFF).map(([k, v]) => `<option value="${k}">${v}</option>`).join("")}</select></label>
        <input id="fText" type="search" placeholder="Cari judul, subtopik, teknik…" aria-label="Cari">
      </div>
      <ul class="cards" id="list"></ul>${packList()}${recommend()}`);
    const dom = document.getElementById("fDom"), diff = document.getElementById("fDiff"), txt = document.getElementById("fText");
    dom.value = f.dom || ""; diff.value = f.diff || ""; txt.value = f.txt || "";
    const update = () => {
      sessionStorage.setItem("osnk-filter", JSON.stringify({ dom: dom.value, diff: diff.value, txt: txt.value }));
      const t = txt.value.trim().toLowerCase();
      const items = D.modules.filter((m) => {
        if (dom.value && m.domain !== dom.value) return false;
        const qs = D.questions.filter((q) => q.module_id === m.id);
        if (diff.value && !qs.some((q) => q.difficulty === diff.value)) return false;
        if (!t) return true;
        const hay = [m.id, m.title, ...qs.flatMap((q) => [q.subtopic, ...q.tags])].join(" ").toLowerCase();
        return hay.includes(t);
      });
      document.getElementById("list").innerHTML = items.map((m) => {
        const qs = qsOf(m.id, "practice"), done = qs.filter((q) => P[q.id] && P[q.id].solved).length;
        const ready = m.ready || qs.length;
        return `<li class="card"><div><strong>${m.order}. ${ready ? `<a href="#/m/${m.id}">${esc(m.title)}</a>` : esc(m.title)}</strong></div>
          <div class="meta"><span class="chip">${m.id}</span><span class="chip">${DOMAIN[m.domain]}</span> Minggu ${m.week} ·
          ${ready ? `${done}/${qs.length} latihan selesai` : "belum tersedia"}</div></li>`;
      }).join("") || `<li class="muted">Tidak ada modul yang cocok.</li>`;
    };
    [dom, diff].forEach((e) => e.addEventListener("change", update));
    txt.addEventListener("input", update);
    update();
  }

  function packList() {
    const items = PACKS.map((p) => ({ p, qs: packQs(p.id) })).filter((x) => x.qs.length);
    if (!items.length) return "";
    return `<h2>Paket latihan</h2><ul class="cards">${items.map(({ p, qs }) => {
      const done = qs.filter((q) => P[q.id] && P[q.id].solved).length;
      return `<li class="card"><div><strong><a href="#/p/${p.id}">${esc(p.title)}</a></strong></div>
        <div class="meta"><span class="chip">${p.id}</span> ${done}/${qs.length} soal selesai</div></li>`;
    }).join("")}</ul>`;
  }

  // Rekomendasi deterministik: tag dari soal yang terakhir dijawab salah -> modul yang memuat tag itu.
  function recommend() {
    const wrong = Object.entries(P).filter(([id, r]) => r.lastWrong && !r.solved && byId[id]).map(([id]) => byId[id]);
    if (!wrong.length) return "";
    const mods = {};
    wrong.forEach((q) => { const mid = homeModule(q); if (mid) mods[mid] = (mods[mid] || 0) + 1; });
    const list = Object.entries(mods).sort((a, b) => b[1] - a[1]).slice(0, 3)
      .map(([mid, n]) => { const m = D.modules.find((x) => x.id === mid); return `<li><a href="#/m/${mid}">${esc(m.title)}</a> — ${n} soal belum tuntas</li>`; });
    return `<h2>Disarankan untuk diulang</h2><ul>${list.join("")}</ul>`;
  }

  // ---- Halaman: modul ----
  function qBlock(q, n, interactive) {
    const r = P[q.id] || {};
    const choices = q.choices.length ? `<ul class="choices">${q.choices.map((c) =>
      `<li><label><input type="radio" name="c-${q.id}" value="${c.id}"> <b>${c.id}.</b> ${c.html}</label></li>`).join("")}</ul>` : "";
    const input = !interactive ? "" : q.answer_type === "self_check" ? "" : q.choices.length
      ? `<div class="answer-row"><button class="primary" data-act="check" data-id="${q.id}">Periksa</button><span class="feedback" role="status" aria-live="polite"></span></div>`
      : `<div class="answer-row"><label for="a-${q.id}">Jawaban</label><input type="text" inputmode="text" autocomplete="off" id="a-${q.id}">
         <button class="primary" data-act="check" data-id="${q.id}">Periksa</button><span class="feedback" role="status" aria-live="polite"></span></div>`;
    const status = r.solved ? `<span class="chip">✓ ${r.solvedUnaided ? "tuntas tanpa bantuan" : "tuntas dengan bantuan"}</span>` : r.attempts ? `<span class="chip">sudah dicoba</span>` : "";
    return `<article class="q" id="${q.id}"><header><span class="qid">${n}</span><span class="chip">${q.id}</span>
      <span class="chip">${DIFF[q.difficulty]}</span>${q.module_id ? "" : `<span class="chip">${DOMAIN[q.domain]} · ${esc((q.prerequisites || []).join(", "))}</span>`}<span class="muted">±${q.minutes} menit</span>${status}${draftChip(q)}</header>
      ${q.statement}${q.diagram ? `<figure class="diagram" role="img" aria-label="${esc(q.diagram_alt)}">${q.diagram}<figcaption class="muted">${esc(q.diagram_alt)}</figcaption></figure>` : ""}
      ${choices}${input}
      ${q.hints.map((h, i) => `<details data-act="hint" data-id="${q.id}" data-n="${i + 1}"><summary>Petunjuk ${i + 1}</summary>${h}</details>`).join("")}
      <details data-act="sol" data-id="${q.id}"><summary>Jawaban dan pembahasan</summary>
        <p><b>Jawaban:</b> ${q.answer_html}</p>${q.solution}
        <p><b>Ide kunci.</b> ${q.key_idea}</p><p><b>Kekeliruan umum.</b> ${q.common_error}</p>
        ${q.alternative ? `<p><b>Cara lain.</b></p>${q.alternative}` : ""}</details></article>`;
  }

  function viewModule(mid) {
    const m = D.modules.find((x) => x.id === mid);
    if (!m) return render("<p>Modul tidak ditemukan.</p>");
    const ex = qsOf(mid, "worked_example"), pr = qsOf(mid, "practice");
    const order = { foundation: 0, core: 1, challenge: 2 };
    pr.sort((a, b) => order[a.difficulty] - order[b.difficulty] || a.id.localeCompare(b.id));
    render(`<p class="muted"><a href="#/">← Modul</a></p><h1>${m.order}. ${esc(m.title)}</h1>
      <div class="toolbar"><a href="#/cetak/${mid}/soal">Cetak soal</a><a href="#/cetak/${mid}/pembahasan">Cetak soal + pembahasan</a></div>
      <section class="material">${m.material || `<p class="muted">Materi modul belum tersedia.</p>`}</section>
      ${ex.length ? `<h2>Contoh terselesaikan</h2>${ex.map((q, i) => `<article class="q"><header><span class="qid">Contoh ${i + 1}</span>${draftChip(q)}</header>${q.statement}
        ${q.diagram ? `<figure class="diagram" role="img" aria-label="${esc(q.diagram_alt)}">${q.diagram}</figure>` : ""}${q.solution}
        <p><b>Jawaban:</b> ${q.answer_html}</p><p><b>Pelajaran.</b> ${q.key_idea}</p></article>`).join("")}` : ""}
      <h2>Latihan</h2>${pr.map((q, i) => qBlock(q, i + 1, true)).join("") || `<p class="muted">Belum ada latihan.</p>`}`, true);
  }

  // ---- Halaman: paket ----
  function viewPack(pid) {
    const p = packOf(pid), qs = packQs(pid);
    if (!p || !qs.length) return render("<p>Paket tidak ditemukan.</p>");
    const rows = Object.entries(DOMAIN).map(([k, v]) => {
      const d = qs.filter((q) => q.domain === k);
      if (!d.length) return "";
      const solved = d.filter((q) => P[q.id] && P[q.id].solvedUnaided).length;
      const tried = d.filter((q) => P[q.id] && P[q.id].attempts).length;
      return `<tr><td>${v}</td><td>${solved} / ${d.length}</td><td>${tried}</td></tr>`;
    }).join("");
    render(`<p class="muted"><a href="#/">← Modul</a></p><h1>${esc(p.title)}</h1><p>${esc(p.note)}</p>
      <div class="toolbar"><a href="#/cetak/${pid}/soal">Cetak soal</a><a href="#/cetak/${pid}/pembahasan">Cetak soal + pembahasan</a></div>
      <table class="summary"><thead><tr><th>Bidang</th><th>Benar tanpa bantuan</th><th>Dicoba</th></tr></thead><tbody>${rows}</tbody></table>
      <p class="muted">Ringkasan diperbarui saat halaman dibuka ulang. Modul rujukan setiap soal tertera pada label soal.</p>
      ${qs.map((q, i) => qBlock(q, i + 1, true)).join("")}`, true);
  }

  // ---- Interaksi latihan (delegasi event) ----
  $main.addEventListener("click", (e) => {
    const b = e.target.closest("button[data-act=check]");
    if (!b) return;
    const q = byId[b.dataset.id], art = document.getElementById(q.id);
    const val = q.choices.length ? (art.querySelector(`input[name="c-${q.id}"]:checked`) || {}).value || "" : art.querySelector("input[type=text]").value;
    const res = G.grade(q, val), fb = art.querySelector(".feedback");
    fb.className = "feedback " + res.status;
    fb.textContent = res.message;
    if (res.status !== "correct" && res.status !== "incorrect") return;
    const r = rec(q.id);
    r.attempts++;
    if (res.status === "correct") {
      if (!r.solved) r.solvedUnaided = r.hintsUsed === 0 && !r.solutionViewed;
      r.solved = true; r.lastWrong = false;
    } else r.lastWrong = true;
    save();
  });
  $main.addEventListener("toggle", (e) => {
    const d = e.target;
    if (!d.open || !d.dataset || !d.dataset.id) return;
    const r = rec(d.dataset.id);
    if (d.dataset.act === "hint") r.hintsUsed = Math.max(r.hintsUsed, +d.dataset.n);
    if (d.dataset.act === "sol") r.solutionViewed = true;
    save();
  }, true);

  // ---- Cetak ----
  function viewPrint(mid, mode) {
    const pack = packOf(mid), m = pack || D.modules.find((x) => x.id === mid);
    if (!m) return render("<p>Tidak ditemukan.</p>");
    const withSol = mode === "pembahasan";
    const pr = pack ? packQs(mid) : qsOf(mid, "practice");
    render(`<p class="no-print"><a href="#/${pack ? "p" : "m"}/${mid}">← Kembali</a> · <button onclick="window.print()">Cetak / simpan PDF</button></p>
      <h1>${esc(m.title)} — ${withSol ? "Soal dan Pembahasan" : "Soal"}</h1>
      ${pr.map((q, i) => `<article class="q"><header><span class="qid">${i + 1}.</span><span class="chip">${q.id}</span>${draftChip(q)}</header>${q.statement}
        ${q.diagram ? `<figure class="diagram">${q.diagram}</figure>` : ""}
        ${q.choices.length ? `<ul class="choices">${q.choices.map((c) => `<li><b>${c.id}.</b> ${c.html}</li>`).join("")}</ul>` : ""}
        ${withSol ? `<p><b>Jawaban:</b> ${q.answer_html}</p>${q.solution}` : ""}</article>`).join("")}`);
  }

  // ---- Progres: ringkasan, ekspor, impor ----
  function viewProgress() {
    const pr = D.questions.filter((q) => q.role !== "worked_example");
    const n = (f) => pr.filter((q) => P[q.id] && f(P[q.id])).length;
    render(`<h1>Progres</h1><p class="muted">Tersimpan di browser ini saja. Gunakan ekspor/impor untuk pindah perangkat.</p>
      <ul><li>Dicoba: ${n((r) => r.attempts > 0)} dari ${pr.length} soal (latihan modul dan paket)</li>
      <li>Tuntas tanpa bantuan: ${n((r) => r.solvedUnaided)}</li>
      <li>Tuntas dengan petunjuk/pembahasan: ${n((r) => r.solved && !r.solvedUnaided)}</li></ul>
      <div class="toolbar"><button id="exp">Ekspor progres (JSON)</button>
      <label>Impor progres <input type="file" id="imp" accept="application/json"></label>
      <button id="reset">Hapus progres</button></div><p id="msg" role="status"></p>`);
    document.getElementById("exp").onclick = () => {
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([JSON.stringify({ format: KEY, data: P }, null, 1)], { type: "application/json" }));
      a.download = "progres-osnk.json"; a.click();
    };
    document.getElementById("imp").onchange = async (e) => {
      try {
        const j = JSON.parse(await e.target.files[0].text());
        if (j.format !== KEY || typeof j.data !== "object") throw new Error();
        P = j.data; save(); viewProgress(); document.getElementById("msg").textContent = "Progres diimpor.";
      } catch (err) { document.getElementById("msg").textContent = "Berkas tidak dikenali."; }
    };
    document.getElementById("reset").onclick = () => { if (confirm("Hapus semua progres di perangkat ini?")) { P = {}; save(); viewProgress(); } };
  }

  function route() {
    const h = location.hash.replace(/^#\/?/, "").split("/");
    if (h[0] === "m") viewModule(h[1]);
    else if (h[0] === "p") viewPack(h[1]);
    else if (h[0] === "cetak") viewPrint(h[1], h[2]);
    else if (h[0] === "progres") viewProgress();
    else viewHome();
  }
  window.addEventListener("hashchange", route);
  route();
})();
