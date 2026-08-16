[🏠 Today's tasks](../task.md) | [Day 02 >>](../../Day-02/dev/notes.md)

# Day 01 — Night School: What is HTML?

Welcome to night school! 🌙 This is the web-development half of your 224-day journey. Mornings build your problem-solving brain (Python/DSA); nights build things you can actually *see* — websites.

You need zero prior knowledge here too. Same rule as mornings: attempt today's tasks from `task.md` first, then read these notes to check yourself. Tonight, we meet the skeleton of every web page on Earth.

---

## 1. What is the web, and where does HTML fit?

When you open `flipkart.com`, your phone (the **client**) sends a request across the internet to Flipkart's computer (the **server** — just a computer that's always on, waiting to serve pages). The server replies with files. The main file it sends back? An **HTML file**.

**HTML** = **HyperText Markup Language**.

- **HyperText** = text with links — text that can jump you to other pages. That jumping is what makes the web a "web".
- **Markup** = you *mark up* plain text with labels describing what each piece IS. Like a teacher marking your essay: "this is the title", "this is a paragraph", "this is important".
- **Language** = it has fixed rules and vocabulary.

One honest clarification: HTML is **not a programming language**. It cannot calculate or make decisions like Python does. It only *describes structure* — "this is a heading, that is a paragraph". Think of a house: HTML is the **brick structure**, CSS (later) is the **paint and interiors**, JavaScript (much later) is the **electricity** that makes switches work.

## 2. How a browser reads HTML

A **browser** (Chrome, Firefox, Edge) is an HTML-reading machine. It receives your file, reads it top to bottom, and for each label it draws the right thing on screen — big bold text for headings, normal text for paragraphs. The reader never sees your tags; they only see the result. Your HTML is the recipe; the rendered page is the dish.

## 3. Tags, elements, and attributes — the grammar

A **tag** is a label in angle brackets: `<p>`. Most come in pairs — an opening tag `<p>` and a closing tag `</p>` (note the slash). Everything from opening tag to closing tag, content included, is called an **element**:

```html
<p>Chai is life.</p>
```

Read it as: "Dear browser, the text 'Chai is life.' is a **p**aragraph."

A few elements are **empty** (self-contained, no closing tag) because they have no text inside — like `<br>` (line break) and `<img>` (image).

### Attributes — extra settings on the opening tag

An **attribute** gives extra information about an element. It always sits **inside the opening tag**, in `name="value"` form (value in double quotes):

```html
<html lang="en">
<a href="https://leetcode.com">Practice here</a>
```

Here `lang="en"` tells the browser the page's language is English, and `href="..."` tells the link where to go. Pattern to memorize: `<tagname attribute="value">content</tagname>`.

### Comments — notes to yourself

```html
<!-- The browser completely ignores this line -->
```

Anything between `<!--` and `-->` is invisible on the page. Use comments to leave notes for future-you: "navbar starts here". (Same idea as Python's `#`.)

## 4. The full skeleton, line by line

Every proper HTML page starts from this exact skeleton. Learn it like you learnt the national anthem — by heart:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My First Page</title>
  </head>
  <body>
    <h1>Namaste, world!</h1>
    <p>My first web page.</p>
  </body>
</html>
```

Line by line:

- **`<!DOCTYPE html>`** — the very first line, always. It declares "this is a modern HTML5 document". Without it, browsers may fall back into an old compatibility mode ("quirks mode") and render things weirdly. It's a declaration, not a tag — no closing needed.
- **`<html lang="en">`** — the root element. EVERYTHING else lives inside it. `lang="en"` helps screen readers (software that reads pages aloud for blind users) and search engines know the language.
- **`<head>`** — information *about* the page. Nothing here appears in the page window itself.
- **`<meta charset="UTF-8">`** — tells the browser which character encoding to use. UTF-8 covers every script — English, हिन्दी, தமிழ், emojis. Skip it and "नमस्ते" may render as garbage symbols.
- **`<title>`** — the text on the **browser tab** (and in Google search results). Note: it lives in head, so it's not on the page body itself.
- **`<body>`** — everything the visitor actually **sees**: headings, paragraphs, images, links. All visible content goes here, and only here.
- **`<h1>`** — the main heading, biggest text. (There are `<h1>` to `<h6>`, big to small — more tomorrow.)
- **`<p>`** — a paragraph of normal text.

## 5. Head vs body — the envelope and the letter

Think of a courier package:

- **`<head>`** = the info written on the envelope — addressee, sender, handling instructions. The delivery system reads it; the person opening the package experiences the *contents*, not the envelope text.
- **`<body>`** = the actual gift inside. This is what the visitor sees and enjoys.

| Goes in `<head>` | Goes in `<body>` |
|---|---|
| `<title>` (tab text) | Headings, paragraphs |
| `<meta>` settings | Images, links, lists |
| Links to CSS files (later) | Buttons, forms — anything visible |

Beginner mistake #1 is putting visible content in `<head>`. Rule of thumb: *can the visitor see it on the page? Then it belongs in `<body>`.*

## 6. Nesting — boxes inside boxes

Elements sit **inside** other elements, like dabbas inside a tiffin carrier. Two rules:

1. **Close inner before outer.** An element opened inside another must close before the outer one closes.

```html
<p>This is <strong>important</strong> news.</p>   <!-- ✅ correct -->
<p>This is <strong>important news.</p></strong>   <!-- ❌ overlapping — never do this -->
```

2. **Indent children.** Push nested elements a couple of spaces right, like we did in the skeleton. The browser doesn't care, but human eyes (yours, in three weeks, at 11 pm) absolutely do.

The whole document is one big nesting: `html` holds `head` and `body`; `body` holds everything visible; those hold smaller pieces. Browsers actually build a family tree of these boxes internally — you'll hear it called the DOM someday.

## 7. Semantic tags — the newspaper layout

**Semantic** means *meaningful* — the tag's name tells you what its content IS, not just how it looks. Picture the front page of a newspaper (say, The Hindu). It isn't one blob of text; it has clearly named regions. HTML5 gives a tag for each region:

| Tag | Newspaper part | Meaning |
|---|---|---|
| `<header>` | The **masthead** — paper's name, date, logo at the top | Introductory content of a page (or of a section). Usually holds the site name and logo. |
| `<nav>` | The **index strip** — "Sports p.12, Business p.8" | Navigation: the block of major links to other pages (Home, About, Contact). |
| `<main>` | The **day's news pages** — the actual reason you bought the paper | The primary, unique content of THIS page. Only **one** `<main>` per page. |
| `<section>` | A named **section** — Sports section, Business section | A thematic grouping of related content, usually with its own heading. |
| `<article>` | **One news story** — complete in itself | Self-contained content that would still make sense if you cut it out and read it alone (a blog post, one product card, one news item). |
| `<footer>` | The **bottom strip** — printer's name, RNI number, address | Closing info: copyright, contact details, small links. |

How they nest, typically:

```html
<body>
  <header> ... site name, logo ... </header>
  <nav> ... links ... </nav>
  <main>
    <section>
      <article> ... one story ... </article>
      <article> ... another story ... </article>
    </section>
  </main>
  <footer> ... © 2026, contact ... </footer>
</body>
```

### Why not just `<div>` everywhere? (the div-soup problem)

There's a generic container tag, `<div>`, that means... nothing. Just "a box". You *could* build a whole page from anonymous divs — people call that **div-soup** — and it would *look* identical in the browser. So why bother with semantic tags?

- **Screen readers**: a blind user's software can announce "navigation" and jump straight to `<nav>` or `<main>`. With div-soup, it's a maze of unlabeled rooms.
- **Search engines**: Google understands your page's structure better and ranks the right content.
- **Future you and teammates**: `<footer>` explains itself; `<div class="bottom-thing2">` explains nothing.

Analogy: a railway station where every board says "Room" vs one with boards saying "Ticket Counter", "Waiting Hall", "Platform 1". Both have the same rooms. Only one is usable by strangers. Write pages for strangers.

`<div>` still has honest uses (grouping purely for styling, later with CSS) — but reach for a semantic tag *first*, and use `<div>` only when no meaningful tag fits.

## 8. Create and open your first page — right now

1. In VS Code: `File → Open Folder`, pick/create a folder for tonight.
2. New file → save it as `index.html`. The `.html` extension is what makes it a web page. (`index.html` is the traditional name for a site's front page — servers look for it by default.)
3. Type the skeleton from Section 4. VS Code shortcut: type `!` and press `Tab` — the whole skeleton appears. Magic, but type it by hand at least twice first; muscle memory matters.
4. Save (`Ctrl+S`).
5. Open the file in a browser: find it in File Explorer and double-click, or right-click in VS Code → "Reveal in File Explorer" → double-click. Your page opens in Chrome/Edge.
6. Edit text in VS Code → save → press `F5` (refresh) in the browser to see changes. This edit-save-refresh loop is your new life.

No internet needed! The browser reads the file straight from your disk — you are the client *and* the server tonight.

## 9. Common mistakes

1. **Forgetting the closing tag** — `<p>text` with no `</p>`. Browsers silently guess and pages break in weird ways later. Type the closing tag immediately after the opening one, *then* fill the middle.
2. **Forgetting the `/` in closing tags** — `<p>text<p>` opens a second paragraph instead of closing the first.
3. **Visible content inside `<head>`** — headings/paragraphs go in `<body>`, always.
4. **Overlapping tags** — `<p><strong>text</p></strong>`. Close inner-first, like removing inner dabbas before closing the tiffin.
5. **Skipping `<!DOCTYPE html>`** — page may render in quirks mode and behave oddly.
6. **Saving as `page.txt` or `page.html.txt`** — then the browser shows raw text. Check the extension is exactly `.html`.
7. **Wrong quote habits in attributes** — write `href="..."` with quotes, no spaces around `=`.
8. **Expecting Enter/spaces in your file to appear on the page** — browsers collapse extra whitespace; line breaks on screen come from tags, not from your Enter key. (More on this tomorrow.)

## 10. Quick recap

- The web = clients requesting files from servers; the main file is HTML.
- HTML marks up text with **tags** to describe structure — it's a markup language, not a programming language.
- Element = opening tag + content + closing tag. Attributes = `name="value"` in the opening tag. Comments = `<!-- ... -->`.
- Skeleton: `<!DOCTYPE html>` → `<html>` → `<head>` (about the page: `<meta charset>`, `<title>`) + `<body>` (everything visible).
- Nesting: boxes in boxes, close inner before outer, indent for humans.
- Six semantic regions, newspaper-style: `header`, `nav`, `main` (only one!), `section`, `article`, `footer`. Semantic tags beat div-soup for accessibility, search, and sanity.
- `index.html` + browser + refresh = your workshop.

## 11. Learn more

- [W3Schools — HTML Introduction](https://www.w3schools.com/html/html_intro.asp)
- [W3Schools — HTML5 Semantic Elements](https://www.w3schools.com/html/html5_semantic_elements.asp)

---

## 🌙 Tomorrow night (Day 2)

Tonight you built the skeleton — an empty newspaper with named regions but no news. Tomorrow we fill it with **real content**: headings and paragraphs that say something, **lists** (your daily timetable!), **links** to other pages, and **images**. The page starts looking like an actual website. Same time, same desk. 🌃

---

[🏠 Today's tasks](../task.md) | [Day 02 >>](../../Day-02/dev/notes.md)
