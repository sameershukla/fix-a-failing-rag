"""Build a static HTML report from a run record. No server, no vendor, no scripts to install.

    python -m dashboard.build [--run RUN_ID] [--baseline RUN_ID]

Writes dashboard/out/<run_id>.html and dashboard/out/latest.html.
Sections that have no data yet (gate thresholds, generation, cost and latency) are named at the bottom,
not faked. They arrive in Modules 4, 6 and 7.
"""
import argparse
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS = [("hit", "Hit Rate"), ("recall", "Recall"), ("precision", "Precision"), ("mrr", "MRR"), ("ndcg", "nDCG")]
LINES = [("hit", "Hit Rate", 1), ("recall", "Recall", 2), ("mrr", "MRR", 3), ("ndcg", "nDCG", 4)]
e = html.escape


def load_run(run_id):
    d = ROOT / "eval" / "runs" / run_id
    if not d.exists():
        sys.exit(f"no such run: {run_id}")
    rec = json.loads((d / "run.json").read_text())
    qs = [json.loads(l) for l in (d / "questions.jsonl").open(encoding="utf-8")]
    return rec, qs


def latest_run_id():
    idx = ROOT / "eval" / "runs" / "index.jsonl"
    if not idx.exists():
        sys.exit("no runs yet. Run: make eval")
    return json.loads(idx.read_text().strip().splitlines()[-1])["run_id"]


def verdict(a, b):
    delta = b["mean"] - a["mean"]
    banded = a["max"] > a["min"] or b["max"] > b["min"]
    if abs(delta) < 1e-12:
        return "same", "no change"
    if not (b["min"] > a["max"] or a["min"] > b["max"]) and banded:
        return "same", "inside the band"
    return ("up", "improved") if delta > 0 else ("down", "declined")


def fmt(v):
    return f"{v['mean']:.3f}" + (f" <span class=band>[{v['min']:.3f} to {v['max']:.3f}]</span>" if v["max"] != v["min"] else "")


def short_doc(d):
    return d.replace("brightcart/", "").replace("generated/level2-noise/", "noise/")


def line_chart(rec):
    ks = rec["ks"]
    W, H, L, R, T, B = 640, 300, 44, 110, 16, 40
    pw, ph = W - L - R, H - T - B
    x = lambda i: L + (pw * i / (len(ks) - 1) if len(ks) > 1 else 0)
    y = lambda v: T + ph * (1 - v)
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Retrieval metrics by K" class="chart">']
    for g in (0, .25, .5, .75, 1):
        out.append(f'<line x1="{L}" x2="{L+pw}" y1="{y(g):.1f}" y2="{y(g):.1f}" class="grid"/><text x="{L-8}" y="{y(g)+4:.1f}" class="tick" text-anchor="end">{g:.2f}</text>')
    for i, k in enumerate(ks):
        out.append(f'<text x="{x(i):.1f}" y="{T+ph+20}" class="tick" text-anchor="middle">{k}</text>')
    out.append(f'<text x="{L+pw/2:.1f}" y="{H-4}" class="axis" text-anchor="middle">K, the number of chunks looked at (not to scale)</text>')
    ends = []
    for key, name, n in LINES:
        pts = [(x(i), y(rec["metrics"][f"{key}@{k}"]["mean"])) for i, k in enumerate(ks)]
        out.append(f'<polyline points="{" ".join(f"{px:.1f},{py:.1f}" for px, py in pts)}" class="line s{n}" fill="none"/>')
        for i, (px, py) in enumerate(pts):
            v = rec["metrics"][f"{key}@{ks[i]}"]["mean"]
            out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" class="dot s{n}"><title>{name} at K={ks[i]}: {v:.3f}</title></circle>')
        ends.append([pts[-1][1], name, n, rec["metrics"][f"{key}@{ks[-1]}"]["mean"]])
    ends.sort()
    for j in range(1, len(ends)):
        if ends[j][0] - ends[j-1][0] < 15:
            ends[j][0] = ends[j-1][0] + 15
    for py, name, n, v in ends:
        out.append(f'<rect x="{L+pw+10}" y="{py-5:.1f}" width="10" height="10" rx="2" class="sw s{n}"/><text x="{L+pw+25}" y="{py+4:.1f}" class="lab">{name} {v:.2f}</text>')
    out.append("</svg>")
    return "".join(out)


def slice_bars(rec, k=5):
    rows = sorted(((t, s) for t, s in rec["slices"].items()), key=lambda ts: -ts[1][f"hit@{k}"]["mean"])
    out = ['<div class="bars">']
    for tag, s in rows:
        v = s[f"hit@{k}"]["mean"]
        out.append(f'<div class="barrow" title="{e(tag)}: Hit Rate@{k} {v:.3f} over {s["n"]} questions"><span class="blabel">{e(tag)} <span class="n">n={s["n"]}</span></span>'
                   f'<span class="track"><span class="fill" style="width:{v*100:.1f}%"></span></span><span class="bval">{v:.2f}</span></div>')
    out.append("</div>")
    return "".join(out)


def scorecard(rec, base):
    heads = "".join(f"<th>{n}</th>" for _, n in METRICS)
    rows = []
    for k in rec["ks"]:
        cells = []
        for m, _ in METRICS:
            key = f"{m}@{k}"
            c = fmt(rec["metrics"][key])
            if base and key in base["metrics"]:
                d = rec["metrics"][key]["mean"] - base["metrics"][key]["mean"]
                cls, word = verdict(base["metrics"][key], rec["metrics"][key])
                c += f'<br><span class="delta {cls}" title="{word}">{d:+.3f} {word}</span>'
            cells.append(f"<td>{c}</td>")
        rows.append(f"<tr><th scope=row>K = {k}</th>{''.join(cells)}</tr>")
    return f'<div class="scroll"><table><thead><tr><th></th>{heads}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def failing_table(qs, k=5):
    bad = [q for q in qs if q["answerable"] and q["metrics"][str(k)]["hit"] == 0]
    bad.sort(key=lambda q: q["id"])
    rows = []
    for q in bad:
        rank = [r for r in q["first_rank_by_build"] if r]
        found = f"rank {rank[0]}" if rank else "not in top 20"
        got = "<br>".join(f'{i+1}. {e(short_doc(h["doc_id"]))} <span class=band>{h["score"]:.2f}</span>' for i, h in enumerate(q["top_retrieved"][:k]))
        rows.append(f"<tr><td>{q['id']}</td><td>{e(q['question'])}</td><td>{'<br>'.join(e(short_doc(d)) for d in q['evidence_docs'])}</td><td>{found}</td><td class=small>{got}</td></tr>")
    return bad, f'<div class="scroll"><table class="fail"><thead><tr><th>id</th><th>question</th><th>expected evidence</th><th>first found</th><th>retrieved (top {k}, score)</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def trend_table(current):
    idx = ROOT / "eval" / "runs" / "index.jsonl"
    rows = [json.loads(l) for l in idx.read_text().strip().splitlines()][-10:]
    body = []
    for r in reversed(rows):
        mark = " class=cur" if r["run_id"] == current["run_id"] else ""
        note = "" if r["golden_hash"] == current["golden"]["hash"] and r["min_cover"] == current["relevance_rule"]["min_cover"] else " different golden set or rule"
        body.append(f"<tr{mark}><td>{e(r['run_id'])}</td><td>{e(r['label'] or '')}{e(note)}</td><td>{r['hit@5']:.3f}</td><td>{r['recall@5']:.3f}</td><td>{r['mrr@5']:.3f}</td></tr>")
    return f'<div class="scroll"><table><thead><tr><th>run</th><th>label</th><th>Hit@5</th><th>Recall@5</th><th>MRR@5</th></tr></thead><tbody>{"".join(body)}</tbody></table></div>'


CSS = """
:root{color-scheme:light;--bg:#fcfcfb;--panel:#fff;--ink:#0b0b0b;--ink2:#52514e;--ink3:#7a7974;--line:#e4e3de;--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;--seq:#2a78d6;--up:#0a6b3c;--down:#b3261e;--same:#52514e}
@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])){color-scheme:dark;--bg:#1a1a19;--panel:#22221f;--ink:#f0efec;--ink2:#c3c2b7;--ink3:#97968c;--line:#3a3a36;--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--seq:#3987e5;--up:#5fd08f;--down:#ff8a80;--same:#c3c2b7}}
:root[data-theme="dark"]{color-scheme:dark;--bg:#1a1a19;--panel:#22221f;--ink:#f0efec;--ink2:#c3c2b7;--ink3:#97968c;--line:#3a3a36;--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--seq:#3987e5;--up:#5fd08f;--down:#ff8a80;--same:#c3c2b7}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:1040px;margin:0 auto;padding:24px 16px 64px}h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:32px 0 4px}p.sub{margin:0 0 12px;color:var(--ink2)}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:8px 16px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:12px 0}
.meta div span{display:block;color:var(--ink3);font-size:12px}.meta div b{font-weight:600;overflow-wrap:anywhere;font-size:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px;margin:8px 0}.warn{border-left:4px solid var(--s4);padding:8px 12px;background:var(--panel);margin:8px 0;border-radius:6px}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}thead th{color:var(--ink2);font-weight:600;white-space:nowrap}tbody th{white-space:nowrap;font-weight:600}
.band{color:var(--ink3);font-size:12px}.small{font-size:12px;color:var(--ink2)}.scroll{overflow-x:auto}tr.cur td{font-weight:600}
.delta{font-size:12px;font-weight:600}.delta.up{color:var(--up)}.delta.down{color:var(--down)}.delta.same{color:var(--same)}
.chart{width:100%;height:auto}.grid{stroke:var(--line);stroke-width:1}.tick{fill:var(--ink3);font-size:11px}.axis{fill:var(--ink2);font-size:12px}.lab{fill:var(--ink);font-size:12px}
.line{stroke-width:2;stroke-linejoin:round}.dot{stroke:var(--panel);stroke-width:2}.s1{stroke:var(--s1);fill:var(--s1)}.s2{stroke:var(--s2);fill:var(--s2)}.s3{stroke:var(--s3);fill:var(--s3)}.s4{stroke:var(--s4);fill:var(--s4)}.line.s1,.line.s2,.line.s3,.line.s4{fill:none}.sw.s1,.sw.s2,.sw.s3,.sw.s4{stroke:none}
.bars{display:grid;gap:6px}.barrow{display:grid;grid-template-columns:minmax(120px,210px) 1fr 44px;gap:10px;align-items:center;font-size:14px}.n{color:var(--ink3);font-size:12px}
.track{height:12px;background:var(--line);border-radius:0 4px 4px 0;overflow:hidden;display:block}.fill{display:block;height:100%;background:var(--seq);border-radius:0 4px 4px 0}.bval{text-align:right;font-variant-numeric:tabular-nums}
details summary{cursor:pointer;color:var(--ink2);margin:8px 0}.pending{color:var(--ink2)}
@media (max-width:560px){.barrow{grid-template-columns:1fr 44px}.track{grid-column:1/-1}}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run")
    ap.add_argument("--baseline")
    args = ap.parse_args()
    run_id = args.run or latest_run_id()
    rec, qs = load_run(run_id)
    base = load_run(args.baseline)[0] if args.baseline else None

    bad, fail_html = failing_table(qs)
    n_ans = rec["golden"]["answerable"]
    git = rec["git"]
    warn = ""
    if base and (base["golden"]["hash"] != rec["golden"]["hash"] or base["relevance_rule"] != rec["relevance_rule"]):
        warn = '<div class="warn"><b>The golden set or the relevance rule differs from the baseline run.</b> The deltas below are changes in the measurement, not in the system.</div>'
    if base and base["config_hash"] != rec["config_hash"]:
        warn += f'<div class="warn">System config changed: {e(base["config_hash"])} to {e(rec["config_hash"])}.</div>'

    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Retrieval report {e(run_id)}</title><style>{CSS}</style></head><body><main>
<h1>Retrieval report</h1><p class="sub">{e(rec['label'] or 'no label')}{(' &middot; compared with ' + e(base['run_id'])) if base else ''}</p>
<div class="meta">
<div><span>run</span><b>{e(rec['run_id'])}</b></div><div><span>system</span><b>{e(rec['system'])}</b></div>
<div><span>git</span><b>{e(str(git['commit']))}{' + uncommitted changes' if git['dirty'] else ''}</b></div><div><span>config hash</span><b>{e(rec['config_hash'])}</b></div>
<div><span>golden set</span><b>{rec['golden']['answerable']} answerable of {rec['golden']['questions']} (hash {e(rec['golden']['hash'])})</b></div>
<div><span>index builds</span><b>{rec['builds']} (headline = mean, band = min to max)</b></div>
<div><span>relevance rule</span><b>chunk covers at least {rec['relevance_rule']['min_cover']:.0%} of the passage</b></div>
<div><span>one question is worth</span><b>{100/n_ans:.2f} points</b></div></div>{warn}

<h2>1. Gate status</h2><p class="pending">No thresholds are set yet. The gate arrives in Module 7. Until then nothing here passes or fails.</p>

<h2>2. Retrieval</h2><p class="sub">Each metric is the mean over {n_ans} answerable questions. Unanswerable questions have no evidence and are not scored here.</p>
<div class="card">{scorecard(rec, base)}</div>
<div class="card"><b>Metrics by K</b><p class="sub">Hover a point for its value.</p>{line_chart(rec)}</div>
<h3>Hit Rate@5 by slice</h3><p class="sub">Slices overlap, so a question can count in several rows. Rows with n under 10 are indicative only.</p>
<div class="card">{slice_bars(rec)}</div>

<h2>5. Failing questions (Hit@5 = 0)</h2><p class="sub">{len(bad)} of {n_ans} answerable questions found no evidence in the top 5.</p>
<details><summary>Show all {len(bad)}</summary>{fail_html}</details>

<h2>6. Recent runs</h2><p class="sub">A row marked as a different golden set or rule is not comparable with the others.</p>
<div class="card">{trend_table(rec)}</div>

<h2>Not built yet</h2><p class="pending">Generation panel (Module 4), cost and latency panel (Module 6), gate status and PR comment (Module 7).</p>
</main></body></html>"""
    out = ROOT / "dashboard" / "out"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{run_id}.html").write_text(page, encoding="utf-8")
    (out / "latest.html").write_text(page, encoding="utf-8")
    print(f"dashboard -> dashboard/out/{run_id}.html")


if __name__ == "__main__":
    main()
