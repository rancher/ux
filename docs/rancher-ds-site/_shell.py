import sys
FIG="https://www.figma.com/design/Eu4nW2RSGyezdjlXhxzmj8/Rancher_DS_NEW"
PAGES=[("index.html","Home"),("why.html","Why adopt it"),("start.html","Getting started"),("hood.html","Under the hood"),("faq.html","Coexistence & FAQ")]
def shell(active,title,body):
    nav="".join(f'<a href="{f}"{" class=\"active\"" if f==active else ""}>{t}</a>' for f,t in PAGES)
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Rancher_DS_NEW</title>
<link rel="stylesheet" href="tokens/tokens.css"><link rel="stylesheet" href="site.css"></head>
<body><header><span class="brand">Rancher_DS_NEW</span><nav>{nav}</nav>
<select id="theme" aria-label="Theme"><option value="light">Light</option><option value="dark">Dark</option><option value="prime-light">Prime Light</option><option value="prime-dark">Prime Dark</option></select></header>
<main>{body}</main>
<footer>Rancher_DS_NEW · a SUSE design system preview · this site is styled entirely by tokens/tokens.css — try the theme switcher.</footer>
<script src="theme.js"></script></body></html>"""

index=f"""
<h1>One design system.<br>Four themes. Zero drift.</h1>
<p class="sub">Rancher_DS_NEW is a fully tokenised design system for SUSE cloud-native products — every colour is a variable, every component passes WCAG 2.2 AA in all four themes, and dark mode is one property, not a redesign.</p>
<div class="btnrow"><a class="btn primary" href="start.html">Get started</a><a class="btn secondary" href="why.html">Why adopt it</a></div>
<p>It began as the Rancher design system. It is built for more: any SUSE product team can adopt the components as they are, or extend them — within the same tokens, the same accessibility guarantees, and the same style logic. The point is not to re-skin it. The point is that you should never have to.</p>
<p>This page is the proof: everything you see is drawn from <a href="tokens/tokens.css">tokens.css</a>, generated from the Figma variables. Flip the theme switcher in the header — that is the entire dark-mode migration.</p>
<div class="card"><div class="label">See it live</div>
<p><a href="{FIG}?node-id=5400-433">A full app-catalog screen built from the system</a> · <a href="{FIG}?node-id=5788-773">the same product screen in dark</a> · <a href="{FIG}?node-id=5858-433">all 71 components under dark mode</a>.</p></div>
<div class="label">The feedback pattern, in this very CSS</div>
<div class="chip error">Namespace is required.</div>
<div class="chip warning">&ldquo;Never&rdquo; can leave stale images on nodes.</div>
<div class="chip success">Saved successfully.</div>
<div class="chip info">Values apply after the next sync.</div>
<div class="chip attention">3 nodes need a look.</div>
<div class="chip neutral">Optional — shown in the cluster overview.</div>
"""

why=f"""
<h1>Why adopt it</h1>
<p class="sub">A design system succeeds when it removes work nobody wanted to do: re-checking contrast, re-drawing dark variants, reconciling documentation with reality. This one removes all three, verifiably.</p>
<h2>Accessibility is enforced, not aspired to</h2>
<p>Every component is audited programmatically against WCAG 2.2 AA in all four themes — including hover, focus and disabled states. The Button family alone passes 768 contrast checks with zero exemptions; the Forms audit runs over 3,700. When a colour cannot pass, we change the token, never the rule.</p>
<h2>Dark mode is a property, not a project</h2>
<p>Components carry no theme of their own. Set the mode on a page or frame and everything inside re-themes — Light, Dark, Prime Light, Prime Dark. Our dark test pages are the same instances as the light ones, one property apart. That is the whole migration. <a href="{FIG}?node-id=5788-773">See the same product screen, dark — no component was edited.</a></p>
<h2>Documentation that cannot lie</h2>
<p>The colour documentation is generated from the tokens themselves: every ramp swatch and every token-table value is bound to the variable it documents. If a value changes, the docs change. Drift is structurally impossible. The same export feeds <a href="tokens/tokens.css">tokens.css</a> — designers and engineers read from one source.</p>
<h2>Adopt, then extend</h2>
<p>Your product is not Rancher — and it does not need to be. The system is a base: use the components directly, or compose new ones from the documented role tokens. Extensions inherit the themes and the AA guarantees for free. What we ask is that extensions stay inside the style logic, so that a SUSE user moving between products stays in one world.</p>
<h2>Proof, not promises</h2>
<p>Two full product screens — the app catalog and a cluster-explorer table — are built purely from the system, in both themes, as standing stress tests. A QA page instantiates all 71 component sets under dark mode as a permanent regression check. A decision log records every architectural choice with dates and revert paths.</p>
"""

start=f"""
<h1>Getting started</h1>
<p class="sub">You can be productive in your first half hour. No design-system theory — just what to click, what to pick, and the handful of mistakes worth avoiding.</p>
<h2>The first four steps</h2>
<div class="card"><p><strong>1 · Turn the library on.</strong> Assets panel → book icon → enable “Rancher_DS_NEW”. Components, icons, styles and all four themes arrive together.</p>
<p><strong>2 · Pin your theme.</strong> Select your top-level frame → Appearance → pick a mode. Pin it early — you should never see dark mode for the first time at review.</p>
<p><strong>3 · Drag in a component, don’t draw one.</strong> Almost everything you need is a property in the right sidebar, not an edit.</p>
<p><strong>4 · Read the description.</strong> Every component documents what it is for, how to use it, and its accessibility behaviour, right in the inspector.</p></div>
<h2>Five rules</h2>
<p>Never type a hex code — every colour is a token that changes with the theme. Never detach an instance. Set the Surface property to match what is behind the control. Leave the focus ring alone. Sizes are Small / Medium / Large, not pixels.</p>
<h2>Before you hand off</h2>
<p>Switch your frame to Dark and look again — it takes ten seconds and it is the single highest-value check. Then: tab through it in your head, no detached instances, one solid destructive action per screen.</p>
<div class="card"><div class="label">Go deeper</div>
<p><a href="{FIG}?node-id=5382-433">The full guide as a live Figma page</a> · <a href="assets/Rancher-DS-Getting-Started.pdf">or as a PDF</a>.</p></div>
"""

hood=f"""
<h1>Under the hood</h1>
<p class="sub">For those who want to know why it holds, not just that it does.</p>
<h2>Token architecture</h2>
<p>Three tiers, one direction. Primitives (hidden from publishing) hold every raw value in luminance-ordered colour ramps. Theme tokens are aliases only — 125 published tokens across four modes, each carrying its CSS custom-property name. Component tokens alias into those. An automated audit confirms zero hardcoded colours in any published component.</p>
<pre><span class="c">/* engineering handoff is the same file this site uses */</span>
<span class="k">.banner-error</span> {{
  <span class="k">background</span>: <span class="s">var(--semantic-error-badge)</span>;
  <span class="k">color</span>: <span class="s">var(--semantic-on-error-badge)</span>; <span class="c">/* AA on its own wash, all four themes */</span>
}}</pre>
<h2>The role vocabulary</h2>
<p>New components are composed from a closed menu of about 25 role tokens — surfaces, text, borders, interactive accents, feedback pairs. Variable scopes enforce it in the picker: text tokens only appear for text, borders only for strokes. A new token is only born when a value must diverge from its role.</p>
<h2>Self-contained feedback colours</h2>
<p>Every semantic family ships as a pair: a wash plus its own AA-tuned foreground. A message chip is legible on any surface it lands on, in any theme, because it brings its own background. Six types: Error, Warning, Success, Info, Attention — and Neutral, for information that implies no state at all.</p>
<h2>Tokens, ready to consume</h2>
<table class="tok"><tr><th>Token</th><th>Light</th><th>Dark</th></tr>
<tr><td><code>--semantic-error</code></td><td><span class="sw" style="background:#d42b3a"></span>#d42b3a</td><td><span class="sw" style="background:#d42b3a"></span>#d42b3a</td></tr>
<tr><td><code>--type-body</code></td><td><span class="sw" style="background:#1f212b"></span>#1f212b</td><td><span class="sw" style="background:#f5f5f8"></span>#f5f5f8</td></tr>
<tr><td><code>--body-background</code></td><td><span class="sw" style="background:#ffffff"></span>#ffffff</td><td><span class="sw" style="background:#14151d"></span>#14151d</td></tr></table>
<p>The full set: <a href="tokens/tokens.css">tokens.css</a> (drop-in custom properties, four themes) and <a href="tokens/tokens.json">tokens.json</a> (for build pipelines). <a href="{FIG}?node-id=5013-7281">The palette in Figma</a> · <a href="{FIG}?node-id=5858-433">the standing dark-mode QA page</a>.</p>
"""

faq=f"""
<h1>Coexistence &amp; FAQ</h1>
<p class="sub">This is a preview, not a migration order. Both design systems stay enabled during the trial.</p>
<h2>The one rule</h2>
<p>Build each screen from one library only. New work: Rancher_DS_NEW. Existing product screens: the current system. If a screen must migrate, migrate it whole. Mixed screens inherit two colour systems, and only one of them switches themes.</p>
<h2>FAQ</h2>
<div class="card"><p><strong>Will my existing files break?</strong> No. Nothing changes until you enable the new library, and enabling it changes nothing you have built.</p>
<p><strong>Can my team fork it for our product?</strong> Extend, yes — fork, no. Compose from the role tokens and keep the style logic; you inherit four themes and AA for free. A fork inherits nothing and drifts immediately.</p>
<p><strong>What about our own brand colours?</strong> Colour ramps carry no meaning in this system — meaning is assigned in the token layer. A brand variant is a token-mode conversation, not a redraw. Talk to us; that is exactly the extension path the architecture was built for.</p>
<p><strong>Where do I report issues or gaps?</strong> [your channel here] — and check the Decision log on the Colors page first; if it is a known trade-off, the reasoning and its revert path are already written down.</p></div>
<p class="note">Poster for printing or slides: <a href="assets/Rancher-DS-Poster-A1.pdf">the one-page pitch (A1 PDF)</a>.</p>
"""

for fn,body,title in [("index.html",index,"Home"),("why.html",why,"Why adopt it"),("start.html",start,"Getting started"),("hood.html",hood,"Under the hood"),("faq.html",faq,"Coexistence & FAQ")]:
    open(fn,"w").write(shell(fn,title,body))
print("pages written")
