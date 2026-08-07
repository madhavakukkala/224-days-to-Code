# Day 2 (Night) — HTML: Text, Lists, Links, Images, Attributes, Paths

Yesterday was the skeleton of an HTML page. Today is about actually putting content on it — the stuff people read, click, and see.

---

## 1. Text elements

### Headings: h1 to h6

Six levels of headings, `<h1>` (biggest, most important) to `<h6>` (smallest). Think of a newspaper: the front-page banner headline is `h1`, section titles like "Sports" are `h2`, individual match reports are `h3`, and so on.

```html
<h1>India Wins the Series</h1>
<h2>Match Highlights</h2>
<h3>First Innings</h3>
```

Rules of thumb:

- **One `h1` per page.** It is the page's main title.
- Don't skip levels (`h1` → `h3`) just because you like the size. Headings are structure, not styling. Size can be changed with CSS later.
- Search engines and screen readers use headings to understand your page's outline.

### Paragraph: p

`<p>` wraps a paragraph of text. The browser automatically adds spacing above and below.

```html
<p>Chai without biscuits is just hot water with attitude.</p>
```

### strong vs b, em vs i

All four make text look different, but two of them carry **meaning** and two are purely visual:

| Tag | Looks | Meaning |
|---|---|---|
| `<strong>` | **bold** | This text is IMPORTANT (urgency, seriousness) |
| `<b>` | **bold** | Just make it bold, no special importance |
| `<em>` | *italic* | Emphasis — you would stress this word while speaking |
| `<i>` | *italic* | Just italic — book titles, foreign words like *jugaad* |

Why does it matter if they look the same? **Screen readers** (software that reads pages aloud for blind users) may change tone for `<strong>` and `<em>`, but not for `<b>` and `<i>`. Meaning-first tags are called *semantic* tags. Prefer `<strong>` and `<em>` when the emphasis is real.

```html
<p><strong>Warning:</strong> Train departs at <em>exactly</em> 8:02. It will not wait.</p>
```

### br and hr

- `<br>` — a line **br**eak. Forces the next text onto a new line without starting a new paragraph. Good for addresses or poems. Do NOT use a pile of `<br>` tags to create spacing — that's a CSS job.
- `<hr>` — a **h**orizontal **r**ule, a dividing line across the page. Marks a change of topic, like the line a shopkeeper draws in his hisaab notebook between two days' accounts.

Both are **empty elements** — they have no closing tag, because they wrap nothing.

```html
<p>Flat 12, Shanti Niwas<br>MG Road<br>Pune 411001</p>
<hr>
```

---

## 2. Lists

### Unordered list: ul — order does not matter

`<ul>` = **u**nordered **l**ist. Bullet points. Use when the order is irrelevant, like a grocery list.

```html
<ul>
  <li>Milk</li>
  <li>Sugar</li>
  <li>Tea leaves</li>
</ul>
```

`<li>` = **l**ist **i**tem. Every single item goes inside its own `<li>`.

### Ordered list: ol — order matters

`<ol>` = **o**rdered **l**ist. Numbered automatically by the browser. Use for steps, rankings, anything where sequence matters.

```html
<ol>
  <li>Boil water</li>
  <li>Add tea leaves and masala</li>
  <li>Add milk, boil again</li>
  <li>Strain and serve</li>
</ol>
```

Note: you never type the numbers. The browser numbers them. Add an item in the middle and everything renumbers itself — that's the whole point.

### Nested lists — a restaurant menu

A list inside a list. Think of a restaurant menu: categories, and dishes under each category. The inner `<ul>` goes **inside an `<li>`** of the outer list — not directly inside the outer `<ul>`.

```html
<ul>
  <li>South Indian
    <ul>
      <li>Masala Dosa</li>
      <li>Idli Sambar</li>
    </ul>
  </li>
  <li>North Indian
    <ul>
      <li>Chole Bhature</li>
      <li>Rajma Chawal</li>
    </ul>
  </li>
</ul>
```

You can mix them too — an `<ol>` of steps where one step has a `<ul>` of options.

---

## 3. Links: the a tag

`<a>` = **a**nchor. It turns text (or an image) into something clickable.

```html
<a href="https://www.irctc.co.in">Book train tickets</a>
```

- `href` = **h**ypertext **ref**erence — the destination address. Without `href`, the link goes nowhere.
- The text between `<a>` and `</a>` is what the user sees and clicks.
- Make link text meaningful: "Book train tickets", not "click here". Screen reader users often jump link-to-link, and ten "click here"s in a row tell them nothing.

### Opening in a new tab

```html
<a href="https://www.cricbuzz.com" target="_blank" rel="noopener">Live score</a>
```

- `target="_blank"` opens the link in a new tab, so the user doesn't lose your page. Use it for external sites; for pages within your own site, stay in the same tab.
- Habit worth building: add `rel="noopener"` with `target="_blank"` — it stops the new page from getting access to yours (a small security hole otherwise).

### Linking to a section on the same page (#id)

First give the target element an `id` (a unique name for one element on the page). Then link to it with `#` + that id.

```html
<h2 id="contact">Contact Us</h2>

<a href="#contact">Jump to Contact section</a>
```

Clicking scrolls the page to that heading. This is how "Back to top" links and table-of-contents links work. You can even combine both: `href="menu.html#desserts"` opens another page AND scrolls to its desserts section.

---

## 4. Images: the img tag

```html
<img src="taj-mahal.jpg" alt="The Taj Mahal at sunrise, reflected in the pool">
```

- `<img>` is an empty element — no closing tag.
- `src` = **s**ou**rc**e — where the image file lives (a path or URL).
- `alt` = **alt**ernative text — a short description of the image.

### Why alt text matters (really)

1. **Screen readers.** A blind user's screen reader cannot "see" the photo. It reads the alt text aloud. Without it, they just hear "image" — useless.
2. **Broken images.** If the file fails to load (wrong path, slow network — very common on 2G in a train), the browser shows the alt text instead of an empty broken icon. The page still makes sense.
3. **Search engines** read alt text to understand what the image is, which helps your page show up in image search.

Write alt text like you're describing the photo to a friend on the phone. If an image is purely decorative (a border flourish), use an empty `alt=""` so screen readers skip it — but never omit the attribute entirely.

---

## 5. Attributes in general

An **attribute** gives extra information about an element. It always sits **inside the opening tag** and follows the pattern:

```
name="value"
```

```html
<a href="https://example.com" target="_blank">link</a>
<img src="photo.jpg" alt="description" width="300">
<h2 id="contact">Contact</h2>
```

Rules:

- Written as `name="value"` pairs, separated by spaces.
- Always in the **opening** tag, never the closing one.
- Values go in quotes. (HTML sometimes forgives missing quotes; don't rely on its mercy.)
- Some attributes are global (work on any element): `id`, `class`, `title`, `style`. Others belong to specific tags: `href` for `<a>`, `src` and `alt` for `<img>`.
- `id` must be **unique** on the page — one element, one id. Like a roll number: two students can't share it.

---

## 6. Absolute vs relative paths

A **path** tells the browser where a file is. Two styles:

### Absolute path — full postal address

The complete address from the start, works from anywhere:

```html
<img src="https://example.com/images/logo.png">
```

Like writing: "Flat 12, Shanti Niwas, MG Road, Pune, Maharashtra, 411001, India." Anyone, anywhere in the world, can find it. Use absolute paths for things on OTHER websites.

### Relative path — directions from where you stand

The address relative to the **current file's location**:

```html
<img src="logo.png">              <!-- same folder as this HTML file -->
<img src="images/logo.png">       <!-- inside the 'images' folder next to this file -->
<img src="../logo.png">           <!-- one folder UP from this file -->
```

Like telling a neighbour: "two houses down the street." Short and convenient — but only works if you're standing on the right street. `../` means "go up one folder" (you can chain it: `../../`).

### Which to use?

- **Your own files** (your images, your other pages): relative paths. The whole project stays portable — move the folder anywhere, zip it, upload it to a server, and all links still work because files keep the same positions relative to each other.
- **Other websites' resources**: absolute URLs — you have no other option.

Classic bug: the image shows fine on your laptop but breaks after upload. Usually the `src` was an absolute path to your own hard disk, like `C:\Users\me\Desktop\photo.jpg`. The server has no such disk. Relative paths avoid this completely.

---

## Common mistakes

1. Choosing heading levels by size instead of meaning, or using five `<h1>`s on one page.
2. Using `<b>`/`<i>` everywhere when the emphasis is genuine — use `<strong>`/`<em>` for real importance.
3. Stacking `<br><br><br>` to create vertical space. Spacing is CSS's job.
4. Putting text directly inside `<ul>`/`<ol>` without an `<li>` wrapper.
5. Nesting a `<ul>` directly inside another `<ul>` instead of inside an `<li>`.
6. Typing numbers manually in an ordered list ("1. Boil water" inside the `<li>`)— the browser already numbers them, so you'd see "1. 1. Boil water".
7. Forgetting `alt` on images, or writing useless alt text like `alt="image123"`.
8. "Click here" as link text.
9. Forgetting the `#` when linking to an id (`href="contact"` goes looking for a *file* named contact).
10. Absolute paths to your own hard disk (`C:\...`) — breaks the moment the page leaves your machine.
11. Putting attributes in the closing tag, or forgetting the quotes around values.

---

## Quick recap

- `h1`–`h6` = structure, like newspaper headline levels. One `h1`, don't skip levels.
- `<p>` for paragraphs; `<br>` = line break, `<hr>` = topic-divider line; both have no closing tag.
- `<strong>`/`<em>` carry meaning (screen readers care); `<b>`/`<i>` are just looks.
- `<ul>` = bullets (order doesn't matter), `<ol>` = numbers (order matters), items always in `<li>`, nested lists go inside an `<li>` — like menu categories with dishes.
- `<a href="...">` makes links; `target="_blank"` + `rel="noopener"` for new tabs; `href="#id"` jumps to a section.
- `<img src alt>` — alt text is for screen readers, broken images, and search. Non-negotiable.
- Attributes = `name="value"` pairs in the opening tag; `id` must be unique.
- Absolute path = full postal address (other sites). Relative path = "two houses down" (your own files — keeps the project portable).
