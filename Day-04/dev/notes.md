[<< Day 03](../../Day-03/dev/notes.md) | [🏠 Today's tasks](../task.md) | [Day 05 >>](../../Day-05/dev/notes.md)

# Day 4 (night) — The Semantic CV: Zero CSS, Full Meaning

## So far → Tonight

Three nights of collecting tags:

- **Night 1** — the skeleton: doctype, head vs body, and the landmark tags.
- **Night 2** — text, lists, links, images.
- **Night 3** — forms and tables.

Tonight everything combines into the **first real page**: my own CV. Not a toy example — a page I could actually send to a recruiter. And the rule that makes it a lesson: **not one line of CSS**. Structure only. If the page still reads perfectly, the structure is right.

---

## 1. Why structure-first?

You don't paint a house before the walls are up. Walls, doors, rooms in the right places first; paint later. CSS is paint. It can make a good structure beautiful, but it cannot fix a broken one.

**Semantic HTML** means choosing tags by *meaning*, not by looks. `<section>` says "this is one themed block of content". `<div>` says nothing — it's a plain cardboard box with no label. Browsers draw both identically, so why care?

- **Screen readers** (software that reads pages aloud for blind users) jump between landmarks: header, nav, main, footer. A page of divs gives them nothing to jump to.
- **Search engines** rank a page better when its headings and sections carry meaning.
- **Recruiters' parsing software** (ATS) extracts your name, skills, and experience more reliably from clean structure.
- **Future you** opens the file in a month and instantly knows what each block is.

Think of a wedding invitation card with zero decoration. The order alone tells you everything: family names on top, the couple, venue, date, RSVP at the bottom. Structure carries meaning. Decoration is optional. That is tonight's page.

## 2. Tag → CV section mapping

| CV part | Tag | Why this tag |
|---|---|---|
| Name, title, contact strip at top | `<header>` | Introductory content for the whole document. |
| Contact details inside the header | `<address>` | The tag *made* for contact info — see the caveat below. |
| Jump links to Education / Skills / etc. | `<nav>` | Navigation landmark. Optional on a one-page CV; add it if the page links to its own sections. |
| Everything that IS the CV | `<main>` | The one unique main-content area. **Exactly one per page.** |
| Summary / Education / Skills / Experience / Projects | `<section>` | Each is a thematic group **with its own heading**. |
| One job entry, one project entry | `<article>` | Self-contained; would still make sense lifted out alone — like one wicket's highlight clip cut from a full match. |
| Skills list | `<ul>` + `<li>` | Bullets with no ranking → unordered. Ranking them? Then `<ol>`. |
| Dates (jobs, degrees) | `<time datetime="...">` | Human text outside, machine date inside. |
| Emphasis on a keyword ("led", "built") | `<strong>` | Importance with meaning, unlike `<b>` which is only looks. |
| Declarations / languages / hobbies footer | `<footer>` | Closing matter of the document. |

## 3. The full skeleton

This is the shape, with placeholder content. Build yours from memory first, then compare.

```html
<header>
  <h1>Priya Sharma</h1>
  <p>Aspiring Software Engineer</p>
  <address>
    Email: <a href="mailto:priya@example.com">priya@example.com</a><br>
    Phone: <a href="tel:+919876543210">+91 98765 43210</a><br>
    Bengaluru, India
  </address>
  <nav>
    <a href="#education">Education</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
  </nav>
</header>

<main>
  <section id="summary">
    <h2>Summary</h2>
    <p>Final-year student building one project a week. Strong in Python fundamentals.</p>
  </section>

  <section id="education">
    <h2>Education</h2>
    <article>
      <h3>B.Tech, Computer Science — XYZ Institute of Technology</h3>
      <p><time datetime="2022-08">Aug 2022</time> – <time datetime="2026-05">May 2026</time> · CGPA 8.4</p>
    </article>
  </section>

  <section id="skills">
    <h2>Skills</h2>
    <ul>
      <li>Python</li>
      <li>HTML</li>
      <li>Problem solving (LeetCode)</li>
    </ul>
  </section>

  <section id="projects">
    <h2>Projects</h2>
    <article>
      <h3>Daily DSA Tracker</h3>
      <p>A public repo logging <strong>224 days</strong> of DSA practice with day-wise notes.</p>
    </article>
  </section>
</main>

<footer>
  <p>Languages: English, Hindi, Telugu</p>
  <p>Updated on <time datetime="2026-08-16">16 August 2026</time></p>
</footer>
```

Notice what is absent: no `<div>`, no `class=`, no `style=`. Every tag earns its place by meaning.

## 4. Heading hierarchy — the strict ladder

Headings are the page's table of contents, and screen readers literally use them as one.

- **Exactly one `<h1>`** — your name. It is the title of the document, and a CV's title is you.
- Sections get `<h2>` (Education, Skills, Projects...).
- Entries inside a section get `<h3>` (a degree, a job, a project).
- **Never skip levels.** h1 → h3 with no h2 is like numbering chapters 1, 3 — the reader wonders what went missing. Going *back up* (h3 then a new h2 for the next section) is fine; that's just closing one chapter and opening another.
- Never pick a heading tag for its size. Size is CSS's job later; the number is only about **rank**.

## 5. The `<address>` caveat

`<address>` is not for any street address in general — it is specifically for the **contact information of the author/owner of the page or article**. On your CV that is perfect: the page's author is you, so your email, phone, and city belong inside it. But the office address of a company you once worked at? That is *not* the page author's contact — leave it as a plain `<p>`.

Also: put `<address>` inside `<header>` or `<footer>`, but never nest a `<header>` or `<footer>` inside it.

## 6. `<time>` and `datetime` — dates that machines can read

"May 2026" is easy for humans, useless for software. The `datetime` attribute carries the machine version:

```html
<time datetime="2026-05">May 2026</time>
<time datetime="2024-06-15">15 June 2024</time>
```

Format: `YYYY-MM-DD`, or just `YYYY-MM`, or just `YYYY`. Browsers, search engines, and CV-parsing tools read the attribute; humans read the text. Both are happy.

## 7. Lists for skills — pick the honest one

- `<ul>` — unordered: the bullets have no ranking. "Python, HTML, Git" — order doesn't claim anything.
- `<ol>` — ordered: position means something. "Steps to run my project: 1, 2, 3."
- Nesting works: a `<ul>` of categories (Languages, Tools), each `<li>` holding its own inner `<ul>`.

A skills list as comma-separated text in a `<p>` is a missed opportunity — a list *is* the meaning here, so use a list tag.

## 8. Section order — what recruiters expect

Recruiters scan a CV in seconds; the order should hand them what they need first.

**Fresher (you, right now):**
1. Header — name, title, contact
2. Summary / objective (2–3 lines max)
3. **Education** (your strongest card — it comes early)
4. **Skills**
5. **Projects** (your substitute for experience — make it meaty)
6. Achievements / certifications
7. Footer — languages, declarations

**Experienced:**
1. Header
2. Summary
3. **Experience** (most recent job first — reverse chronological)
4. Skills
5. Projects (optional, if they add beyond the job)
6. Education (drops near the bottom — the degree matters less than the work)
7. Footer

Same tags, different order. Structure is not just *which* tag — it's also *where*.

## 9. The final test: read it naked

Open your page in the browser. No CSS, so it will look plain — black text, default sizes, blue links. Now read it top to bottom and ask:

- Does it read like a sensible document, in the right order?
- Is my name obviously the title?
- Can I tell where each section starts, just from the headings?
- Do the dates, lists, and entries make sense without any visual styling?

If yes — the structure is correct, and any CSS added later is pure decoration on a solid wall. If you feel the urge to "fix" something with styling, that is usually a structure problem in disguise. Fix the tags, not the paint.

Second test, if you can: press Tab repeatedly. Focus should jump through your links in a sensible order. That's the keyboard-user's experience of your structure.

## 10. Common mistakes

1. **Div soup.** `<div class="header">` instead of `<header>`. The class name fools humans, not machines.
2. **Multiple `<h1>`s.** One page, one title. Sections start at `<h2>`.
3. **Skipping heading levels downward.** h2 → h4 because "h3 looked too big" — size is CSS's problem, not the heading number's.
4. **Choosing tags for their default look.** Using `<blockquote>` for indenting, `<h4>` for small bold text. Meaning first, always.
5. **`<address>` for every address.** It's for the page author's contact only.
6. **`<section>` without a heading.** A section is a *titled* thematic block; no title usually means you wanted something else (or the section needs its `<h2>`).
7. **`<article>` for everything (or nothing).** Test: would this block make sense alone, out of context? Yes → article. No → section or plain elements.
8. **Forgetting `<main>`** — or using two of them. Exactly one.
9. **Dates as bare text.** Wrap them in `<time datetime="...">` — free machine-readability.

## 11. Quick recap

- Semantics = tags chosen for **meaning**; CSS is paint that comes later and fixes nothing structural.
- CV map: `header` (name + `address` contact) → `main` → one `section` per CV part → `article` per entry → `footer`.
- One `<h1>` (your name), `h2` for sections, `h3` for entries, never skip down a level.
- `<address>` = page author's contact only. `<time datetime="...">` = dates machines can parse.
- Skills are a `<ul>` — a list should look like a list in the code, not just on screen.
- Fresher order: Education → Skills → Projects. Experienced: Experience first, Education last.
- The proof of good structure: the page reads perfectly top to bottom with **zero** CSS.

## Learn more

- W3Schools — Semantic elements: <https://www.w3schools.com/html/html5_semantic_elements.asp>
- MDN — `<time>`: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time>
- MDN — `<address>`: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address>
- MDN — Heading elements and document structure: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements>

---

## Tomorrow night

The CV gets interactive. Tomorrow we return to its contact form and make it actually **validate input** — required fields, email format checks, number ranges — using HTML's built-in validation before a single line of JavaScript. Structure tonight, behaviour tomorrow.

---

[<< Day 03](../../Day-03/dev/notes.md) | [🏠 Today's tasks](../task.md) | [Day 05 >>](../../Day-05/dev/notes.md)
