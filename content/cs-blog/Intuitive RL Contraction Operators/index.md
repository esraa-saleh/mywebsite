---
title: "Intuitive RL Series : Contraction Operators"
subtitle: 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: "2026-09-11T00:00:00Z"

# Date updated
lastmod: "2026-09-11T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Enable LaTeX math
math: true

# authors:
# - admin

tags:
- Intuitive RL series
- Reinforcement Learning
- pedagogical

categories:
- Intuitive RL Series
---

If you are teaching or learning RL and have ever wished an idea showed up as a picture first, this series is for you. I am trying to communicate science the way I always wanted it communicated to me: precision and clarity, with as few words as I can get away with (written or spoken), as much visual structure as I can find, and a clear sense of where each stepping stone sits in the larger picture. I recognize this is not a universal preference, and I am targeting a specific kind of reader. This first post is intentionally simple so I can learn, from your feedback, what actually works for people who share my communication preferences. Main ideas from *Reinforcement Learning: Foundations* [[1]](#ref1). Videos use Manim [[2]](#ref2), 3Blue1Brown's animation tool.

---

Let's start!

Click 💡 whenever you want more intuition.

**Contraction operators** keep showing up in RL proofs. They are a main tool for reasoning about convergence: if we keep applying the same update, do we settle on a solution?

Contractions are defined using norms.

A **norm** is a function {{< math >}}$\|\cdot\| : \mathbb{R}^d \to [0, \infty)${{< /math >}} such that {{< math >}}$\forall\, x, y \in \mathbb{R}^d,\; \forall\, a \in \mathbb{R}${{< /math >}}

<style>
.norm-list { margin: 0.4rem 0 1rem; padding-left: 1.4rem; }
.norm-list > li { margin: 0.25rem 0 0.7rem; }
.norm-list .norm-row { display: flex; flex-wrap: wrap; align-items: center; column-gap: 0.45rem; }
.norm-list .norm-row > p { display: inline; margin: 0; }
.norm-list .norm-toggle { display: contents; }
.norm-list .norm-toggle summary { cursor: pointer; user-select: none; font-size: 1.25rem; display: inline-block; line-height: 1; }
.norm-list .norm-toggle summary::-webkit-details-marker { display: none; }
.norm-list .norm-intuition { flex: 1 1 100%; width: 100%; margin-top: 0.35rem; }
.norm-list .norm-toggle p { margin: 0.2rem 0 0.35rem; font-size: 0.95rem; }
</style>
<ol class="norm-list">
<li>
<div class="norm-row">
{{< math >}}$\|ax\| = |a| \cdot \|x\|${{< /math >}}
<details class="norm-toggle">
<summary aria-label="Idea">💡</summary>
<div class="norm-intuition">
<p>Scaling a vector by {{< math >}}$a${{< /math >}} scales its size by {{< math >}}$|a|${{< /math >}}.</p>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 180" width="560" height="180" style="max-width:100%;height:auto" role="img" aria-label="OK: -2x is twice as long as x and flipped. Not OK: a claimed -2x with the same length as x.">
  <defs>
    <marker id="n1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="currentColor" font-family="ui-sans-serif, system-ui, sans-serif">
    <text x="28" y="24" font-size="15" font-weight="700">OK</text>
    <text x="308" y="24" font-size="15" font-weight="700">not OK</text>
  </g>
  <line x1="280" y1="8" x2="280" y2="172" stroke="currentColor" stroke-width="1" opacity="0.35"/>
  <g fill="none" stroke="currentColor" stroke-width="2">
    <line x1="40" y1="70" x2="150" y2="70" marker-end="url(#n1)"/>
    <line x1="260" y1="125" x2="40" y2="125" marker-end="url(#n1)"/>
    <line x1="320" y1="70" x2="430" y2="70" marker-end="url(#n1)"/>
    <line x1="430" y1="125" x2="320" y2="125" marker-end="url(#n1)"/>
  </g>
  <g fill="currentColor" font-size="14" font-family="ui-sans-serif, system-ui, sans-serif" text-anchor="middle">
    <text x="95" y="94">x</text>
    <text x="150" y="149">−2x</text>
    <text x="375" y="94">x</text>
    <text x="375" y="149">−2x</text>
  </g>
</svg>
</div>
</details>
</div>
</li>
<li>
<div class="norm-row">
{{< math >}}$\|x + y\| \le \|x\| + \|y\|${{< /math >}}
<details class="norm-toggle">
<summary aria-label="Idea">💡</summary>
<div class="norm-intuition">
<p>The size of a sum is at most the sum of the sizes.</p>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 170" width="560" height="170" style="max-width:100%;height:auto" role="img" aria-label="OK when x+y is shorter than x then y; not OK when it is longer.">
  <defs>
    <marker id="n2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="currentColor" font-family="ui-sans-serif, system-ui, sans-serif">
    <text x="28" y="22" font-size="15" font-weight="700">OK</text>
    <text x="308" y="22" font-size="15" font-weight="700">not OK</text>
  </g>
  <line x1="280" y1="8" x2="280" y2="162" stroke="currentColor" stroke-width="1" opacity="0.35"/>
  <g fill="none" stroke="currentColor" stroke-width="2">
    <line x1="40" y1="60" x2="140" y2="60" marker-end="url(#n2)"/>
    <line x1="140" y1="60" x2="240" y2="60" marker-end="url(#n2)"/>
    <line x1="40" y1="115" x2="206" y2="115" marker-end="url(#n2)"/>
    <line x1="320" y1="60" x2="401" y2="60" marker-end="url(#n2)"/>
    <line x1="401" y1="60" x2="445" y2="60" marker-end="url(#n2)"/>
    <line x1="320" y1="115" x2="520" y2="115" marker-end="url(#n2)"/>
  </g>
  <g stroke="currentColor" stroke-width="1" opacity="0.35">
    <line x1="240" y1="48" x2="240" y2="128"/>
    <line x1="445" y1="48" x2="445" y2="128"/>
  </g>
  <g fill="currentColor" font-size="14" font-family="ui-sans-serif, system-ui, sans-serif" text-anchor="middle">
    <text x="90" y="84">x</text>
    <text x="190" y="84">y</text>
    <text x="123" y="139">x+y</text>
    <text x="360" y="84">x</text>
    <text x="423" y="84">y</text>
    <text x="475" y="139">x+y</text>
  </g>
</svg>
</div>
</details>
</div>
</li>
<li>
<div class="norm-row">
{{< math >}}$\|x\| = 0 \implies x = 0${{< /math >}}
<details class="norm-toggle">
<summary aria-label="Idea">💡</summary>
<div class="norm-intuition">
<p>Size zero means the zero vector.</p>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 210" width="560" height="210" style="max-width:100%;height:auto" role="img" aria-label="OK: the zero vector has size zero. Not OK: a nonzero vector claimed to have size zero.">
  <defs>
    <marker id="n3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="currentColor" font-family="ui-sans-serif, system-ui, sans-serif">
    <text x="28" y="24" font-size="15" font-weight="700">OK</text>
    <text x="308" y="24" font-size="15" font-weight="700">not OK</text>
  </g>
  <line x1="280" y1="8" x2="280" y2="202" stroke="currentColor" stroke-width="1" opacity="0.35"/>
  <circle cx="140" cy="110" r="5" fill="currentColor"/>
  <circle cx="340" cy="110" r="5" fill="currentColor"/>
  <g fill="none" stroke="currentColor" stroke-width="2">
    <line x1="340" y1="110" x2="500" y2="55" marker-end="url(#n3)"/>
  </g>
  <g fill="currentColor" font-size="14" font-family="ui-sans-serif, system-ui, sans-serif" text-anchor="middle">
    <text x="140" y="52">‖0‖ = 0</text>
    <text x="140" y="138">0</text>
    <text x="340" y="138">0</text>
    <text x="420" y="175">‖x‖ = 0</text>
    <text x="518" y="48">x ≠ 0</text>
  </g>
</svg>
</div>
</details>
</div>
</li>
</ol>

Examples:

<ul class="norm-examples">
<li>
the {{< math >}}$p${{< /math >}}-norm {{< math >}}$\|x\|_p = \big(\sum_i |x_i|^p\big)^{1/p}${{< /math >}} for {{< math >}}$p \ge 1${{< /math >}}
<ul>
<li>Euclidean: {{< math >}}$p = 2${{< /math >}}</li>
</ul>
</li>
<li>
the max-norm {{< math >}}$\|x\|_\infty = \max_i |x_i|${{< /math >}}
</li>
</ul>
<style>
.norm-examples > li { margin: 0 0 1.15rem; }
.norm-examples > li:last-child { margin-bottom: 0; }
.norm-examples ul { margin: 0.4rem 0 0; }
</style>

An **operator** is a function between spaces. Here, real vector spaces.

{{< math >}}
$$
T : \mathbb{R}^d \to \mathbb{R}^d,
\qquad
T(v) \in \mathbb{R}^d
$$
{{< /math >}}

Applied {{< math >}}$n${{< /math >}} times:

{{< math >}}
$$
T^n(v) = T\big(T^{n-1}(v)\big), \qquad n \ge 2,
$$
{{< /math >}}

{{< math >}}$T${{< /math >}} is a **contraction operator** (or specifically a **{{< math >}}$\boldsymbol{\beta}${{< /math >}}-contraction operator**) w.r.t. {{< math >}}$\|\cdot\|${{< /math >}} if

{{< math >}}
$$
\forall\, v_1, v_2 \in \mathbb{R}^d \qquad \|T(v_1) - T(v_2)\| \le \beta \, \|v_1 - v_2\|.
$$
{{< /math >}}

{{< math >}}
$$
\text{where } \beta \text{ is } \in (0, 1)
$$
{{< /math >}}

{{< video src="ContractionOnLine_v_final.mp4" controls="yes" >}}

## References

<a id="ref1"></a>[1] S. Mannor, Y. Mansour, and A. Tamar, *Reinforcement Learning: Foundations*. Cambridge, U.K.: Cambridge University Press, 2026. [Online]. Available: [https://sites.google.com/view/rlfoundations/home](https://sites.google.com/view/rlfoundations/home)

<a id="ref2"></a>[2] G. Sanderson, *Manim*, 3Blue1Brown. [Online]. Available: [https://github.com/3b1b/manim](https://github.com/3b1b/manim)
