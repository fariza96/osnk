// Penilai jawaban isian/pilihan. Skrip biasa (bukan modul) agar jalan via file:// dan di tes Node.
// Tidak memakai eval. Pecahan dibandingkan dengan aritmetika rasional BigInt.
(function (root) {
  "use strict";

  function gcd(a, b) {
    a = a < 0n ? -a : a;
    b = b < 0n ? -b : b;
    while (b) [a, b] = [b, a % b];
    return a;
  }

  // Normalisasi input siswa: spasi, tanda minus unicode, koma desimal Indonesia.
  function normalize(s) {
    return String(s == null ? "" : s)
      .trim()
      .replace(/\s+/g, "")
      .replace(/[−–—]/g, "-")
      .replace(/^\+/, "");
  }

  // "3/4", "-12", "0,75", "1.50" -> {n, d} tersederhana (d > 0) atau null.
  function parseRational(raw) {
    const s = normalize(raw).replace(",", ".");
    let m = s.match(/^(-?)(\d+)\/(\d+)$/);
    if (m) {
      let n = BigInt(m[2]), d = BigInt(m[3]);
      if (d === 0n) return null;
      if (m[1]) n = -n;
      const g = gcd(n, d) || 1n;
      return { n: n / g, d: d / g };
    }
    m = s.match(/^(-?)(\d+)(?:\.(\d+))?$/);
    if (m) {
      const frac = m[3] || "";
      let n = BigInt(m[2] + frac), d = 10n ** BigInt(frac.length);
      if (m[1]) n = -n;
      const g = gcd(n, d) || 1n;
      return { n: n / g, d: d / g };
    }
    return null;
  }

  // Hasil: {status: "correct" | "incorrect" | "invalid" | "empty" | "manual", message}
  function grade(q, input) {
    const spec = q.answer_spec || {};
    const s = normalize(input);
    if (q.answer_type === "self_check") return { status: "manual", message: "Nilai sendiri dengan rubrik." };
    if (s === "") return { status: "empty", message: "Jawaban masih kosong." };

    switch (q.answer_type) {
      case "integer": {
        if (!/^-?\d+$/.test(s)) return { status: "invalid", message: "Masukkan bilangan bulat, mis. 12 atau -3." };
        return BigInt(s) === BigInt(spec.value) ? ok() : no();
      }
      case "rational": {
        const a = parseRational(s), b = parseRational(spec.value);
        if (!a) return { status: "invalid", message: "Masukkan bilangan bulat, pecahan p/q, atau desimal." };
        return a.n === b.n && a.d === b.d ? ok() : no();
      }
      case "decimal": {
        const t = s.replace(",", ".");
        if (!/^-?\d+(\.\d+)?$/.test(t)) return { status: "invalid", message: "Masukkan bilangan desimal." };
        return Math.abs(Number(t) - Number(spec.value)) <= Number(spec.tolerance) + 1e-12 ? ok() : no();
      }
      case "choice":
        return s.toUpperCase() === String(spec.correct).toUpperCase() ? ok() : no();
      default:
        return { status: "invalid", message: "Tipe jawaban tidak dikenal." };
    }
  }
  const ok = () => ({ status: "correct", message: "Benar." });
  const no = () => ({ status: "incorrect", message: "Belum tepat." });

  // Fisher–Yates dengan RNG yang dapat disuntikkan (untuk tes); mengacak salinan.
  function shuffle(arr, rand) {
    rand = rand || Math.random;
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(rand() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  const api = { normalize, parseRational, grade, shuffle };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.Grader = api;
})(typeof globalThis !== "undefined" ? globalThis : this);
