import html, re, pathlib

root = pathlib.Path(__file__).parent
lines = (root / "README.md").read_text(encoding="utf-8").splitlines()


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


sections = []  # dict(title, rows, note)
cur = None
for ln in lines:
    if ln.startswith("## ") or ln.startswith("# Quiz"):
        title = ln.lstrip("# ").strip()
        cur = {"title": title, "rows": [], "note": None}
        sections.append(cur)
    elif cur and ln.startswith("|") and not ln.startswith("|---") and not ln.startswith("| ศัพท์"):
        cells = [c.strip() for c in ln.strip().strip("|").split(" | ", 1)]
        cur["rows"].append(cells)
    elif cur and ln.startswith("> ⚠️"):
        cur["note"] = ln[2:].strip()

sections = [s for s in sections if s["rows"]]
intro = [l[2:] for l in lines if l.startswith("> ") and "⚠️" not in l]

toc, body = [], []
total = 0
for i, s in enumerate(sections):
    sid = f"s{i}"
    total += len(s["rows"])
    toc.append(f'<a href="#{sid}">{html.escape(s["title"])}</a>')
    rows = "\n".join(
        f"<tr><th scope=\"row\">{inline(a)}</th><td>{inline(b)}</td></tr>" for a, b in s["rows"]
    )
    note = f'<p class="note">{inline(s["note"])}</p>' if s["note"] else ""
    body.append(
        f'<section id="{sid}"><h2>{html.escape(s["title"])} <small>{len(s["rows"])} คำ</small></h2>'
        f'<table><thead><tr><th>ศัพท์</th><th>คืออะไร</th></tr></thead><tbody>\n{rows}\n</tbody></table>{note}</section>'
    )

page = f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>คลังศัพท์ ITDS231</title>
<meta name="description" content="คลังศัพท์ ITDS231 Computer Networks Lecture 1–7 ใช้ทวนก่อนสอบ">
<style>
:root {{
  --bg:#f7f8fa; --surface:#ffffff; --text:#1b1f27; --muted:#5b6472; --line:#e2e6ec;
  --accent:#1d5fd6; --accent-soft:#e6eefc; --mark:#ffe58a; --note:#fff6d6; --note-line:#e6c85a;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg:#0f1319; --surface:#171c24; --text:#e8ebf0; --muted:#9aa4b2; --line:#2a313c;
    --accent:#7aa7ff; --accent-soft:#1d2a45; --mark:#6b5a10; --note:#2c2712; --note-line:#8a7420;
  }}
}}
:root[data-theme="dark"] {{
  --bg:#0f1319; --surface:#171c24; --text:#e8ebf0; --muted:#9aa4b2; --line:#2a313c;
  --accent:#7aa7ff; --accent-soft:#1d2a45; --mark:#6b5a10; --note:#2c2712; --note-line:#8a7420;
}}
* {{ box-sizing:border-box; }}
html {{ scroll-behavior:smooth; scroll-padding-top:84px; }}
body {{ margin:0; background:var(--bg); color:var(--text); line-height:1.65;
  font-family:"Sarabun","Noto Sans Thai",system-ui,-apple-system,"Segoe UI",sans-serif; }}
header.bar {{ position:sticky; top:0; z-index:10; background:var(--surface); border-bottom:1px solid var(--line);
  display:flex; gap:12px; align-items:center; padding:10px 16px; }}
header.bar h1 {{ font-size:1.05rem; margin:0; white-space:nowrap; }}
#q {{ flex:1; min-width:0; padding:8px 12px; border:1px solid var(--line); border-radius:8px;
  background:var(--bg); color:var(--text); font:inherit; }}
#q:focus, button:focus-visible, a:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
#theme {{ border:1px solid var(--line); background:var(--bg); color:var(--text); border-radius:8px;
  padding:8px 12px; font:inherit; cursor:pointer; white-space:nowrap; }}
main {{ max-width:960px; margin:0 auto; padding:20px 16px 60px; }}
.intro {{ color:var(--muted); margin:0 0 16px; }}
nav.toc {{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:24px; }}
nav.toc a {{ background:var(--accent-soft); color:var(--accent); text-decoration:none; padding:6px 12px;
  border-radius:999px; font-size:.9rem; }}
section {{ margin-bottom:32px; }}
h2 {{ font-size:1.25rem; margin:0 0 10px; }}
h2 small {{ color:var(--muted); font-weight:400; font-size:.8rem; margin-left:6px; }}
table {{ width:100%; border-collapse:collapse; background:var(--surface); border:1px solid var(--line);
  border-radius:10px; overflow:hidden; }}
th, td {{ text-align:left; vertical-align:top; padding:10px 12px; border-bottom:1px solid var(--line); }}
thead th {{ background:var(--accent-soft); color:var(--accent); font-size:.85rem; }}
tbody th {{ width:32%; font-weight:600; }}
tbody tr:last-child > * {{ border-bottom:0; }}
code {{ background:var(--accent-soft); padding:1px 5px; border-radius:4px; font-size:.9em; }}
mark {{ background:var(--mark); color:inherit; border-radius:2px; }}
.note {{ background:var(--note); border:1px solid var(--note-line); border-radius:8px; padding:10px 12px; margin-top:10px; }}
#empty {{ display:none; color:var(--muted); text-align:center; padding:40px 0; }}
footer {{ text-align:center; color:var(--muted); font-size:.85rem; padding:0 16px 32px; }}
footer a {{ color:var(--accent); }}
@media (max-width:640px) {{
  header.bar h1 {{ display:none; }}
  thead {{ display:none; }}
  tr {{ display:block; border-bottom:1px solid var(--line); padding:8px 0; }}
  tbody th, td {{ display:block; width:auto; border:0; padding:2px 12px; }}
  tbody th {{ color:var(--accent); }}
}}
</style>
</head>
<body>
<header class="bar">
  <h1>📚 คลังศัพท์ ITDS231</h1>
  <input id="q" type="search" placeholder="ค้นหาศัพท์ เช่น CSMA, VLAN, ACK" aria-label="ค้นหาศัพท์">
  <button id="theme" type="button" aria-label="สลับโหมดสว่าง/มืด">🌓 สลับโหมด</button>
</header>
<main>
  <p class="intro">{html.escape(" ".join(intro))}</p>
  <p class="intro">ทั้งหมด {total} รายการ</p>
  <nav class="toc" aria-label="สารบัญ">{"".join(toc)}</nav>
  {"".join(body)}
  <p id="empty">ไม่พบศัพท์ที่ค้นหา</p>
</main>
<footer>ที่มา: Notion · <a href="https://github.com/Thinnaphat-tht/itds231-glossary">ดูบน GitHub</a></footer>
<script>
(function () {{
  var root = document.documentElement, KEY = "itds231-theme";
  try {{ var saved = localStorage.getItem(KEY); if (saved) root.setAttribute("data-theme", saved); }} catch (e) {{}}
  document.getElementById("theme").addEventListener("click", function () {{
    var dark = root.getAttribute("data-theme") === "dark" ||
      (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme: dark)").matches);
    var next = dark ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try {{ localStorage.setItem(KEY, next); }} catch (e) {{}}
  }});

  var rows = Array.prototype.slice.call(document.querySelectorAll("tbody tr"));
  var originals = rows.map(function (r) {{ return r.innerHTML; }});
  var secs = Array.prototype.slice.call(document.querySelectorAll("section"));
  var empty = document.getElementById("empty");
  function esc(s) {{ return s.replace(/[.*+?^${{}}()|[\\]\\\\]/g, "\\\\$&"); }}
  document.getElementById("q").addEventListener("input", function (e) {{
    var q = e.target.value.trim().toLowerCase(), shown = 0;
    rows.forEach(function (r, i) {{
      r.innerHTML = originals[i];
      var hit = !q || r.textContent.toLowerCase().indexOf(q) !== -1;
      r.style.display = hit ? "" : "none";
      if (hit) shown++;
      if (hit && q) {{
        var re = new RegExp(esc(q), "gi");
        r.querySelectorAll("th, td").forEach(function (c) {{
          c.innerHTML = c.innerHTML.replace(/(<[^>]*>)|([^<]+)/g, function (m, tag, text) {{
            return tag ? tag : text.replace(re, function (x) {{ return "<mark>" + x + "</mark>"; }});
          }});
        }});
      }}
    }});
    secs.forEach(function (s) {{
      var any = s.querySelector("tbody tr:not([style*='none'])");
      s.style.display = any ? "" : "none";
    }});
    empty.style.display = shown ? "none" : "block";
  }});
}})();
</script>
</body>
</html>
"""
(root / "index.html").write_text(page, encoding="utf-8")
print("sections", len(sections), "rows", total)
