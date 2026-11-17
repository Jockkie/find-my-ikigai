#!/usr/bin/env python3
"""Render a Find My Ikigai profile as a one-file HTML map.

Usage: python3 ikigai_map.py profile.json map.html

Shows the seven needs as a radar (score now, with importance as dot size),
the candidates with the user's own verdict, the chosen direction and the
first step. Standard library only.
"""
import html
import json
import math
import sys

NEEDS = ["Life satisfaction", "Change and growth", "A bright future", "Resonance",
         "Freedom", "Self-actualization", "Meaning and value"]
IMP = {"low": 3, "medium": 5, "high": 8, "not in top three": 4}


def esc(v):
    return html.escape("" if v is None else str(v))


def radar(needs, before=None):
    by = {n.get("name"): n for n in needs}
    cx, cy, r = 220, 210, 150
    pts, dots, labels, rings = [], [], [], []
    for k in (2, 4, 6, 8, 10):
        ring = []
        for i in range(7):
            a = -math.pi / 2 + i * 2 * math.pi / 7
            ring.append(f"{cx + r * k / 10 * math.cos(a):.1f},{cy + r * k / 10 * math.sin(a):.1f}")
        rings.append(f'<polygon points="{" ".join(ring)}" class="ring"/>')
    for i, name in enumerate(NEEDS):
        a = -math.pi / 2 + i * 2 * math.pi / 7
        n = by.get(name, {})
        s = n.get("score") or 0
        x, y = cx + r * s / 10 * math.cos(a), cy + r * s / 10 * math.sin(a)
        pts.append(f"{x:.1f},{y:.1f}")
        imp = n.get("importance", "medium")
        gap = imp == "high" and s <= 4
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{IMP.get(imp, 5)}" class="{"gap" if gap else "dot"}"/>')
        lx, ly = cx + (r + 26) * math.cos(a), cy + (r + 26) * math.sin(a)
        anchor = "middle" if abs(math.cos(a)) < 0.3 else ("start" if math.cos(a) > 0 else "end")
        labels.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" class="{"lab gaplab" if gap else "lab"}">{esc(name)} · {s}</text>')
    ghost = ""
    if before:
        bb = {n.get("name"): n.get("score") or 0 for n in before}
        gp = []
        for i, name in enumerate(NEEDS):
            a = -math.pi / 2 + i * 2 * math.pi / 7
            gp.append(f"{cx + r * bb.get(name, 0) / 10 * math.cos(a):.1f},{cy + r * bb.get(name, 0) / 10 * math.sin(a):.1f}")
        ghost = f'<polygon points="{" ".join(gp)}" class="ghost"/>'
    return (f'<svg viewBox="-140 0 720 420" role="img" aria-label="Seven needs">{"".join(rings)}{ghost}'
            f'<polygon points="{" ".join(pts)}" class="area"/>{"".join(dots)}{"".join(labels)}</svg>')


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    p = json.load(open(sys.argv[1], encoding="utf-8"))
    nl = str(p.get("language", "en")).startswith("nl")
    L = ({"feeling": "Het gevoel (ikigai-kan)", "hard": "In een zware periode:", "forward": "Waar ik naar uitkijk:", "sources": "Bronnen", "source": "Bron", "kind": "Soort", "brings": "Wat het me geeft", "fragile": "kwetsbaar", "nosource": "Behoeften zonder bron:"}
         if nl else {"feeling": "The feeling (ikigai-kan)", "hard": "In a hard period:", "forward": "Looking forward to:", "sources": "Sources", "source": "Source", "kind": "Kind", "brings": "What it gives me", "fragile": "fragile", "nosource": "Needs without a source:"})
    cands = "".join(
        f'<tr><td>{esc(c.get("name"))}</td><td>{esc(c.get("origin"))}</td><td>{esc(c.get("qualities"))}</td>'
        f'<td><span class="v {esc(c.get("verdict"))}">{esc(c.get("verdict"))}</span>'
        + (f'<div class="core">core: {esc(c.get("owned_core"))}</div>' if c.get("owned_core") else "")
        + "</td></tr>" for c in p.get("candidates", []))
    kan = p.get("ikigai_kan") or {}
    moments = "".join(f'<li><strong>{esc(m.get("what"))}</strong><br><span class="feel">{esc(m.get("feelings"))}</span>' + (f' · <span class="feel">{esc(m.get("body"))}</span>' if m.get("body") else "") + "</li>" for m in kan.get("moments", []))
    feeling = ""
    if moments or kan.get("looking_forward"):
        feeling = f'<h2>{L["feeling"]}</h2><div class="card"><ul class="moments">{moments}</ul>'
        if kan.get("hard_period"):
            feeling += f'<p><span class="lbl">{L["hard"]}</span> {esc(kan["hard_period"])}</p>'
        if kan.get("looking_forward"):
            feeling += f'<p><span class="lbl">{L["forward"]}</span> {esc(kan["looking_forward"])}</p>'
        feeling += "</div>"
    src = p.get("sources") or []
    sources = ""
    if src:
        rows = "".join(f'<tr><td>{esc(x.get("name"))}{" <span class=fragile>" + L["fragile"] + "</span>" if str(x.get("fragile", "")).lower() in ("yes", "ja") else ""}</td><td>{esc(x.get("kind", ""))}</td><td>{esc(x.get("feeling"))}</td></tr>' for x in src)
        sources = f'<h2>{L["sources"]}</h2><div class="card"><table><tr><th>{L["source"]}</th><th>{L["kind"]}</th><th>{L["brings"]}</th></tr>{rows}</table></div>'
    gaps = [n["name"] for n in p.get("needs", []) if n.get("fed_by") == []]
    gap_html = f'<p class="gapnote">{L["nosource"]} {esc(", ".join(gaps))}</p>' if gaps else ""
    cand = p.get("candidates") or []
    fu = p.get("follow_ups") or []
    follow = ""
    if fu:
        items = "".join(f'<tr><td>{esc(f.get("date"))}</td><td>{esc(f.get("step_result"))}</td><td>{esc(f.get("decision"))}</td><td>{esc(f.get("next_step"))}</td></tr>' for f in fu)
        follow = f'<h2>Follow-ups</h2><div class="card"><table><tr><th>Date</th><th>What the step taught</th><th>Decision</th><th>Next step</th></tr>{items}</table></div>'
    owned_section = (f'''<h2>Owned or borrowed <span class="lbl">(NLP)</span></h2>
<div class="card"><p style="margin-top:0">Your owned signature: <em>{esc(p.get('owned_signature'))}</em></p>
<table><tr><th>Candidate</th><th>Origin</th><th>How it shows up inside</th><th>Your verdict</th></tr>{cands}</table></div>''' if cand else "")
    direction_section = (f'<h2>Direction to explore</h2><div class="card"><strong>{esc(p.get("direction"))}</strong></div>' if p.get("direction") else "")
    step = p.get("step") or p.get("first_step")
    page = f"""<!doctype html><html lang="{esc(p.get('language', 'en'))}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>My ikigai map</title>
<style>
:root {{ --bg:#F5F5DC; --fg:#212121; --muted:#5D4037; --line:rgba(33,33,33,.12); --card:#FBFBEE; --own:#388E3C; --gap:#F57C00; --gold:#FFCA28; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#212121; --fg:#F5F5DC; --muted:rgba(245,245,220,.62); --line:rgba(245,245,220,.14); --card:#292929; --own:#81C784; }} }}
* {{ box-sizing:border-box; }} body {{ margin:0; background:var(--bg); color:var(--fg); font:15px/1.55 Inter, system-ui, sans-serif; }}
main {{ max-width:860px; margin:0 auto; padding:40px 22px 64px; }}
.eyebrow {{ font-size:11px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
.eyebrow::before {{ content:""; display:inline-block; width:22px; height:2px; background:var(--gap); vertical-align:middle; margin-right:10px; }}
h1 {{ font-size:30px; letter-spacing:-0.04em; margin:12px 0 4px; }}
h2 {{ font-size:11px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin:34px 0 12px; }}
.quote {{ font-family:Spectral, Georgia, serif; font-size:22px; line-height:1.4; margin:18px 0 0; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:18px 20px; }}
svg {{ width:100%; max-width:680px; display:block; margin:0 auto; font-family:Inter, system-ui, sans-serif; }}
.ring {{ fill:none; stroke:var(--line); }} .area {{ fill:rgba(56,142,60,.18); stroke:var(--own); stroke-width:1.5; }}
.ghost {{ fill:none; stroke:var(--muted); stroke-dasharray:4 4; opacity:.7; }} .dot {{ fill:var(--own); }} .gap {{ fill:var(--gap); }} .lab {{ fill:var(--fg); font-size:12px; }} .gaplab {{ fill:var(--gap); font-weight:700; }}
table {{ width:100%; border-collapse:collapse; }} th, td {{ text-align:left; padding:9px 8px; border-bottom:1px solid var(--line); vertical-align:top; }}
th {{ color:var(--muted); font-weight:500; font-size:12.5px; }}
.v {{ border-radius:999px; padding:2px 10px; font-size:12.5px; border:1px solid var(--line); }}
.owned {{ background:rgba(56,142,60,.15); color:var(--own); border-color:var(--own); }} .borrowed {{ opacity:.6; }} .mixed {{ background:rgba(255,202,40,.2); }}
.moments {{ margin:0; padding-left:18px; }} .moments li {{ margin-bottom:8px; }} .feel {{ color:var(--muted); font-size:13.5px; }} .lbl {{ color:var(--muted); font-size:12.5px; }} .fragile {{ font-size:11px; color:var(--gap); border:1px solid var(--gap); border-radius:999px; padding:0 6px; margin-left:6px; }} .gapnote {{ color:var(--gap); font-size:13px; text-align:center; }}
.core {{ font-size:12.5px; color:var(--muted); margin-top:4px; }}
.step {{ font-family:Spectral, Georgia, serif; font-size:18px; }}
footer {{ color:var(--muted); font-size:12px; margin-top:36px; }}
</style></head><body><main>
<div class="eyebrow">Find My Ikigai · by Jockkie Studio</div>
<h1>My ikigai map</h1>
<div style="color:var(--muted)">{esc(p.get('updated'))} · next reflection {esc(p.get('next_reflection'))}</div>
<p class="quote">"{esc(p.get('keep_sentence', ''))}"</p>
{feeling}
{sources}
<h2>Seven needs (Kamiya)</h2>
<div class="card">{radar(p.get('needs', []), p.get('first_needs'))}<p style="color:var(--muted);font-size:12.5px;text-align:center">Dot size is how important the need is to you. Orange: important and low right now.{(' Dashed: your first scores.' if p.get('first_needs') else '')}</p>{gap_html}</div>
{owned_section}
{direction_section}
<h2>First step</h2>
<div class="card step">{esc(step or 'not chosen yet')}</div>
{follow}
<footer>Find My Ikigai by Jockkie Studio · Based on Mieko Kamiya's ikigai psychology: the feeling (ikigai-kan), its sources and the seven needs. Reflective coaching, not therapy. This map stays with you.</footer>
</main></body></html>"""
    open(sys.argv[2], "w", encoding="utf-8").write(page)
    print(f"Map written to {sys.argv[2]}")


if __name__ == "__main__":
    main()
