[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AEBN5VKN)
# HW02 — Semantic HTML

**Week 2 · DSAW · Universidad de La Sabana**

## Objective

Build the HTML skeleton of your project's landing page using **semantic HTML only** — no CSS, no JavaScript.

## Deliverables

### `index.html`

Build your project's landing page with:

- Complete semantic HTML5 structure: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` — used meaningfully, not as div replacements
- A single `<h1>` per page. Use `<h2>` and `<h3>` for subsections.
- At least one `<form>` with:
  - `<input>` fields with appropriate types (`text`, `email`, `password`, etc.)
  - Every field has a `<label>` associated via matching `for` and `id` attributes
- All images have a descriptive `alt` attribute — not empty, not "image"
- **No styles. No scripts.** This deliverable evaluates structure only.

## Layer 2

Run your page through [WAVE Web Accessibility Evaluator](https://wave.webaim.org/). Fix at least 2 of the flagged errors or alerts. Include a screenshot of the result in an `assets/` folder.

## AI Log

If you used AI to generate the HTML, include at the end of the file or in an `AI-LOG.md`:
- Which parts were AI-generated
- What you had to fix and why

## Deployment

Push to GitHub Pages. Plain HTML — no build step required.

## Autograding

The pipeline will check:
- ✅ `index.html` exists and has content
- ✅ HTMLHint: zero HTML errors
- ✅ GitHub Pages responds with HTTP 200
- ✅ Correct use of semantic tags, forms, and accessibility attributes (reviewed by Claude)

> **Submission rule:** If it is not deployed and public, it cannot be graded.
