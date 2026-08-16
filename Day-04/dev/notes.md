# Day 4 (night) — A Semantic CV Page, With ZERO CSS

Tonight's build: my CV as a plain HTML page. Not one line of CSS allowed. The point is to prove the **structure** is right before any styling exists.

---

## 1. Why structure-first?

You don't paint a house before the walls are up. First the skeleton — walls, doors, rooms in the right places. Paint (CSS) comes later and only makes a good structure *look* good; it cannot fix a bad one.

**Semantic HTML** means choosing tags by *meaning*, not by looks. A `<section>` says "this is a distinct section of content". A `<div>` says nothing — it is just a plain box. Browsers render `<div>` and `<section>` the same, so why care?

- **Screen readers** (software that reads pages aloud for blind users) navigate by landmarks like `header`, `main`, `nav`. Divs give them nothing to jump to.
- **Search engines** understand a page better when headings and sections are meaningful.
- **Future me** reads the code and instantly knows what each block is.

Think of it like a wedding invitation card. Even with no decoration, the order tells you everything: names on top, venue, date, RSVP at the bottom. Structure carries the meaning. Decoration is optional.

---

## 2. Which tag for which part of the CV

| CV part | Tag | Why this tag |
|---|---|---|
| Name + contact block at top | `<header>` | The introductory strip of the page. Not just "stuff at the top" — it *introduces* the document. |
| Links to jump to Education/Skills/etc. | `<nav>` | Navigation landmark. Only needed if the page links to its own sections; a short CV can skip it. |
| Everything that IS the CV | `<main>` | The one unique main content area. **Only one `<main>` per page.** |
| Education / Skills / Experience / Projects | `<section>` | Each is a thematic group with its own heading. |
| Each individual job (or project) entry | `<article>` | An `<article>` is a self-contained piece that would make sense on its own — one job entry could be lifted out and still be complete, like one wicket's highlight clip out of a full match. |
| List of skills | `<ul>` | Skills have no ranking order between the bullets → unordered list. (If I were ranking them, `<ol>`.) |
| Declaration / copyright / "references on request" | `<footer>` | Closing information of the page. |

Skeleton:

```html
<header>
  <h1>Uday Kiran</h1>
  <address>
    <a href="mailto:me@example.com">me@example.com</a>, Hyderabad
  </address>
</header>

<main>
  <section>
    <h2>Experience</h2>
    <article>
      <h3>Software Engineer — Some Company</h3>
      <p><time datetime="2024-06">June 2024</time> – Present</p>
      <ul>
        <li>Built the payments dashboard.</li>
      </ul>
    </article>
  </section>

  <section>
    <h2>Skills</h2>
    <ul>
      <li>Python</li>
      <li>HTML</li>
    </ul>
  </section>
</main>

<footer>
  <p>References available on request.</p>
</footer>
```

### The order of sections a recruiter expects

A recruiter scans a CV for barely 30 seconds — like a TTE checking tickets, one quick glance each. The sections must arrive in the order they expect, strongest first:

1. **Name + contact** (header) — always on top.
2. **One-line summary/objective** — optional, skip if it says nothing.
3. For a **fresher**: Skills → Projects → Education → internships if any.
4. For someone **experienced**: Experience climbs to the top; Education drops near the bottom.
5. **Certifications / achievements**, then the declaration in the footer — always last.

Semantic tags cannot fix a wrong order. Write the `<section>`s in reading order — because the source order IS the order a screen reader, a bot, and a skimming recruiter all get.

---

## 3. Heading hierarchy — one h1, never skip levels

Headings are the page's table of contents, like a school textbook: chapter title → topic → sub-topic.

- **Exactly one `<h1>`** — the page's single subject. On a CV, that's my name.
- `<h2>` for each major section: Education, Skills, Experience.
- `<h3>` for entries inside a section: a degree name, a job title.
- **Never skip levels.** `h1 → h3` is like a book jumping from Chapter 1 straight to sub-sub-topic 1.1.1 — a screen-reader user hears the gap and thinks content is missing.
- Never pick a heading tag because of its *size* ("h4 looks about right here"). Size is CSS's job later. Headings encode *outline position* only.

---

## 4. `<address>` — contact info has its own tag

`<address>` marks contact information for the page's author/owner. Inside a CV's `<header>`, it is exactly right:

```html
<address>
  <a href="mailto:udathak@example.com">udathak@example.com</a><br>
  <a href="tel:+919000000000">+91 90000 00000</a><br>
  Hyderabad, India
</address>
```

Common trap: `<address>` is **not** for any postal address appearing in content (like a company's office address in a job description). It is specifically "how to contact the author of this page/article".

---

## 5. `<time>` — dates that machines can read

Humans read "June 2024". Machines prefer `2024-06`. The `<time>` tag gives both:

```html
<time datetime="2024-06">June 2024</time> – <time datetime="2025-03">March 2025</time>
```

- The visible text can be in any human style — "Diwali 2024", "Jun '24".
- The `datetime` attribute holds the machine format: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`.
- Why bother? Search engines and parsing tools (including résumé scanners) can extract exact dates without guessing what "3/6/24" means — is that 3rd June or 6th March? The `datetime` attribute removes the doubt, like writing the date in figures AND words on a cheque.

---

## 6. The real test: read it with no CSS

Open the page. It is plain black-on-white browser-default styling. Now read it top to bottom.

- Does it read like a proper CV? Name first, then contact, then sections in a sensible order, each with a clear heading?
- Can you tell where Experience ends and Skills begin, using headings alone?
- Do the lists read as lists, the dates as dates?

**If a page still reads perfectly with zero CSS, the semantics are right.** This is exactly how a screen reader, a search engine bot, or the "reader mode" button experiences the page — none of them see your CSS. A dabbawala can deliver the right tiffin using only the code painted on the lid, no fancy packaging needed. The markup is that code.

If instead the no-CSS page is a soup of same-looking text, the structure was being faked by styling — and that's the bug to fix *before* writing any CSS tomorrow.

---

## Common mistakes

- **Div soup.** `<div class="header">` instead of `<header>`. The class name means nothing to browsers or screen readers; the tag does.
- **Multiple `<h1>`s** (one per section). One page, one h1. Sections get h2.
- **Skipping heading levels** because a smaller heading "looked better". Looks are CSS's problem.
- **More than one `<main>`**, or putting header/footer inside `<main>`. `<main>` wraps only the unique content between them.
- **Using `<article>` for things that can't stand alone** (a single skill bullet) or `<section>` without any heading. Section = themed group *with* a heading.
- **`<address>` for every address on the page.** It is only for the author's contact info.
- **`<time>` without `datetime`**, or a `datetime` in a non-standard format like `06/2024`. Use `2024-06`.
- **Using `<br>` chains or empty paragraphs to create spacing.** Spacing is styling. If the structure needs a gap to make sense, the structure is wrong.

---

## Quick recap

- Structure first, decoration later — walls before paint.
- CV map: `header` (name + `address`) → optional `nav` → one `main` → `section` per topic → `article` per job → `ul` for skills → `footer`.
- Section order = recruiter order: contact first, strongest section next (fresher: skills/projects/education), declaration last. Source order is what everyone gets.
- One `h1`, ordered heading levels, never skip.
- `<time datetime="2024-06">` = human text outside, machine date inside.
- Final exam for the markup: switch off all CSS. If it still reads perfectly top to bottom, the semantics pass.
