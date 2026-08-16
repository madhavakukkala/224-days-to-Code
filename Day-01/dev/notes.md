# Day 1 (Night) — HTML: The Skeleton of Every Webpage

## What is HTML, really?

**HTML** stands for HyperText Markup Language. Forget the full form — here's what it actually is:

HTML is the **structure** of a webpage. Nothing more.

Think of building a house. First comes the brick structure — walls, rooms, doorways. No paint, no lights, no furniture. That bare structure is HTML. Later, CSS is the paint and interiors (how it looks), and JavaScript is the electricity and plumbing (what it does). Today is only bricks.

Two words to know:

- **Tag** — an instruction wrapped in angle brackets, like `<p>`. Most tags come in pairs: `<p>` opens, `</p>` closes (the `/` means "closing").
- **Element** — the opening tag + the content + the closing tag, all together: `<p>Hello</p>` is a paragraph element.

A browser (Chrome, etc.) reads the HTML file top to bottom and draws the page from it. That's the whole game.

---

## Document structure — the fixed skeleton

Every HTML page on earth follows this shape:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First Page</title>
  </head>
  <body>
    <p>Hello world</p>
  </body>
</html>
```

Line by line:

- `<!DOCTYPE html>` — the very first line, always. It tells the browser "this is modern HTML". It's like the "Govt. of India" seal on a document — a declaration of what kind of document this is. Not a tag, just a declaration. No closing pair.
- `<html>` — the outermost box. Everything else lives inside it. One per page.
- `<head>` — information **about** the page (details below).
- `<body>` — the actual visible content of the page.
- `</html>` — closes the outermost box. Done.

Indentation (the spaces) is only for human readability. The browser doesn't care, but future-you does.

---

## head vs body — the one-line rule

> **head = things ABOUT the page. body = things ON the page.**

Think of a parcel from Amazon. The shipping label on the box — address, weight, contents description — is the head. Nobody keeps the label, but the delivery system needs it. What's inside the box is the body — the thing you actually wanted.

**Goes in `<head>`** (invisible to the visitor):

- `<title>` — the text on the browser tab.
- `<meta charset="UTF-8">` — which character set to use (so ₹, हिंदी, etc. display correctly).
- Links to CSS files, icons, etc. (later days).

**Goes in `<body>`** (everything the visitor sees):

- Headings, paragraphs, images, links, buttons — all of it.

Classic beginner bug: writing visible content in the head. The browser may still show it, but it's wrong — like scribbling your message on the shipping label instead of putting a letter in the box.

---

## Two small tools: comments and attributes

### Comments — notes the browser ignores

```html
<!-- This is a comment. The browser skips it completely. -->
```

A comment is a pencil note in the margin of your textbook — useful for the reader (you), invisible in the exam (the rendered page). Use them to label chunks of a long file: `<!-- navbar starts -->` ... `<!-- navbar ends -->`.

One catch: comments ARE visible if someone does right-click → View Page Source. So never put passwords or secrets in them.

### Attributes — extra settings on a tag

An **attribute** sits inside the *opening* tag and gives extra information. The shape is always `name="value"`:

```html
<a href="/about">About</a>       <!-- href = where the link goes -->
<meta charset="UTF-8">           <!-- charset = which character set -->
<html lang="en">                 <!-- lang = the page's language -->
```

Think of a tag as a courier packet and attributes as the fields filled on its label: `to="..."`, `weight="..."`. The packet type stays the same; the fields fine-tune it.

Three small rules:

- Value goes in quotes: `href="/about"`, not `href=/about`.
- No spaces around the `=`.
- Attributes live only in the opening tag — never in a closing tag like `</a>`.

---

## Semantic tags — the newspaper analogy

**Semantic** just means "having meaning". A semantic tag's *name tells you what's inside it*.

You could build an entire page out of `<div>` tags — `<div>` is a plain, meaningless box. But then your page is a warehouse of identical unlabeled cartons. Semantic tags are labeled cartons.

The best mental model: **a newspaper**. Pick up any Sunday newspaper and every semantic tag is right there.

### `<header>` — the masthead

The top strip of the newspaper: the paper's name in big letters, the date, the price. On a website: the logo, site name, maybe a tagline. The "who we are" banner at the top.

```html
<header>
  <h1>The Daily Chai</h1>
</header>
```

### `<nav>` — the index

"Sports — page 12, Business — page 8, Cinema — page 15." The index tells you where things are. On a website, `<nav>` (navigation) holds the menu of links: Home, About, Contact.

```html
<nav>
  <a href="/">Home</a>
  <a href="/about">About</a>
</nav>
```

### `<main>` — the main story

The big front-page story — the reason you picked up the paper. `<main>` wraps the primary content of the page, the part that is unique to *this* page. **Only one `<main>` per page**, just like one front-page lead.

### `<section>` — the sections

Sports section, Business section, Editorial section. A `<section>` groups related content under one theme. A page can have many sections, and each usually has its own heading.

```html
<section>
  <h2>Sports</h2>
  ...
</section>
```

### `<article>` — one article

Inside the Sports section there are individual articles — one match report, one interview. An `<article>` is one self-contained piece that would still make sense if you cut it out and handed it to someone alone. A blog post, a news story, a product card.

```html
<article>
  <h3>India wins by 6 wickets</h3>
  <p>Match report goes here...</p>
</article>
```

Sections contain articles; the nesting mirrors the newspaper exactly.

### `<footer>` — the publisher info at the bottom

The bottom of the newspaper: "Printed and published by..., RNI No..., address". On a website: copyright line, contact info, social links, small-print links.

```html
<footer>
  <p>&copy; 2026 The Daily Chai</p>
</footer>
```

### Full skeleton, all together

```html
<body>
  <header>...site name, logo...</header>
  <nav>...menu links...</nav>
  <main>
    <section>
      <article>...one story...</article>
      <article>...another story...</article>
    </section>
  </main>
  <footer>...copyright, contact...</footer>
</body>
```

---

## Why semantic tags beat div-soup

**Div-soup** = a page built entirely from nested `<div>`s. It works — the browser renders it — so why bother with semantic tags?

1. **Readability.** `<nav>` tells you it's a menu before you read a single line inside. Fifty nested `<div class="wrapper2">`s tell you nothing. Like a railway platform where every train board just says "TRAIN" instead of "Mumbai Local, Platform 2".
2. **Accessibility.** Screen readers (software that reads pages aloud for blind users) understand semantic tags. A user can jump straight to `<main>` or `<nav>`. With div-soup, they're stuck listening to the whole page linearly. Semantic HTML is the difference between a station with signboards and one without.
3. **SEO.** Search engines (Google) use semantic structure to figure out what matters on your page. Content inside `<main>` and `<article>` gets understood better than anonymous divs.
4. **Future-you.** Coming back to your own code after two weeks, semantic tags are self-documenting.

Rule of thumb: reach for a semantic tag first; use `<div>` only when no semantic tag fits (pure layout grouping).

---

## Nesting — last opened, first closed

Tags sit inside each other like steel dabbas in a tiffin stack. The one rule: **the tag you opened last must be closed first**. No overlapping.

```html
<!-- CORRECT — article closes fully inside section -->
<section>
  <article>
    <p>India wins by 6 wickets</p>
  </article>
</section>

<!-- WRONG — section closes while article is still open (overlap!) -->
<section>
  <article>
</section>
  </article>
```

The wrong version is like closing the big dabba while the small dabba is half in, half out. The browser tries to auto-fix bad nesting, and its guesses cause weird bugs later.

Two habits that keep you safe:

1. Type the closing tag *immediately* after the opening tag, then fill the middle.
2. Indent one level every time you go deeper — the visual staircase makes overlaps jump out.

And remember the containment order you've already seen: `<head>` and `<body>` sit directly inside `<html>`, visible things sit inside `<body>`, and sections hold articles — the newspaper order.

---

## Common mistakes

1. **Putting visible content in `<head>`.** Head is about the page, body is on the page.
2. **Forgetting to close tags.** `<section>` without `</section>` makes the browser guess, and it guesses badly.
3. **Using more than one `<main>`.** One page, one main. Multiple `<header>`/`<footer>` are allowed (an article can have its own), but keep it simple for now.
4. **Using `<header>` when you mean `<h1>`.** `<header>` is a container region; `<h1>` is a heading text. Different things.
5. **Div-soup by habit.** Ask "what IS this block?" before typing `<div>` — usually a semantic tag answers.
6. **Skipping `<!DOCTYPE html>`.** Without it the browser drops into old-compatibility mode ("quirks mode") and styling behaves weirdly later.
7. **Overlap-closing tags.** `<section><article></section></article>` closes the outer box before the inner one. Last opened, first closed — always.
8. **Attribute typos.** Missing quotes (`href=/about`) or spaces around `=` (`href = "/about"`). Keep it tight: `href="/about"`.

---

## Quick recap

- HTML = the brick structure of the house. CSS = paint, JS = electricity (coming later).
- Fixed skeleton: `<!DOCTYPE html>` → `<html>` → `<head>` + `<body>`.
- **Head = about the page** (title, meta). **Body = on the page** (visible content).
- `<!-- comment -->` = pencil note in the margin; the browser ignores it (but View Source shows it).
- Attributes: `name="value"` inside the opening tag — `<a href="/about">`. Quotes on, no spaces around `=`.
- Newspaper map: `header` = masthead, `nav` = index, `main` = the main story (only one), `section` = sports/business sections, `article` = one self-contained story, `footer` = publisher info at the bottom.
- Nesting: last opened, first closed — dabbas in a tiffin stack, no overlaps.
- Semantic tags beat div-soup: readable, accessible, SEO-friendly, kind to future-you.
