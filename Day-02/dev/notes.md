# Day 2 — HTML Flesh: Text, Lists, Links, Images

**Yesterday → Today:** Yesterday you built the skeleton — the boilerplate, `head` vs `body`, and semantic tags that give a page its bones. Today we put flesh on that skeleton: real text with proper headings, lists that organise, links that connect pages, and images that bring it alive.

---

## 1. Headings — `<h1>` to `<h6>`

Six levels of headings, from loudest to softest:

```html
<h1>India</h1>
<h2>Telangana</h2>
<h3>Hyderabad</h3>
<h4>Charminar Area</h4>
<h5>Laad Bazaar</h5>
<h6>Shop No. 12</h6>
```

Think of a newspaper: `<h1>` is the front-page headline, `<h2>` the section titles, `<h3>` the article titles inside a section. Rules that matter:

- **One `<h1>` per page.** It's the page's main title. Two headlines on one front page confuses both readers and Google.
- **Never skip levels for looks.** Don't jump `h1 → h4` because `h4` "looks the right size". Headings carry *meaning* (structure), not styling — size is CSS's job (coming soon).
- Search engines and screen readers use headings as the page's table of contents. Break the hierarchy and you break their map.

## 2. Paragraphs — `<p>`

```html
<p>Hyderabadi biryani is layered, not mixed. That is the whole secret.</p>
<p>The second secret is patience. Dum means slow.</p>
```

Each `<p>` is one paragraph — the browser adds a gap between them automatically. Important: the browser **collapses whitespace**. Ten spaces or five Enter presses inside your HTML file become ONE space on screen. Layout comes from tags, not from your spacebar.

## 3. `<strong>`/`<b>` and `<em>`/`<i>` — same look, different meaning

```html
<p><strong>Warning:</strong> platform 3 changed to platform 7.</p>
<p>The train is <em>actually</em> on time today.</p>
<p><b>Menu</b> — <i>Paneer Butter Masala</i></p>
```

- `<strong>` = **importantly bold** — "this matters, pay attention". Screen readers stress it.
- `<b>` = bold with **no extra meaning** — just visually thick.
- `<em>` = *emphasised* — spoken with stress ("the train is *actually* on time" vs plain "actually").
- `<i>` = italic with no extra meaning — book titles, foreign words, dish names.

They *look* identical in the browser, so beginners think they're the same. They're not — one speaks meaning, the other only paints pixels. Prefer `<strong>` and `<em>` when the emphasis is real.

## 4. `<br>` and `<hr>` — small breaks

```html
<p>Flat 402, Sri Sai Residency<br>Madhapur<br>Hyderabad - 500081</p>
<hr>
<p>Next section starts here.</p>
```

- `<br>` = line break *within* text — perfect for addresses and song lyrics. It has no closing tag (an "empty" element).
- `<hr>` = horizontal rule — a full-width line marking a thematic shift, like the line a shopkeeper draws in the ledger after each day's accounts.

Don't use `<br><br><br>` to create spacing — that's the spacebar habit again. Spacing is CSS's job.

## 5. `<div>` vs `<span>` — plain boxes

```html
<div>
  <h2>Chai Corner</h2>
  <p>Best cutting chai in the <span>whole</span> colony.</p>
</div>
```

- `<div>` = a **block** container — takes the full width and starts on a new line. A big carton you pack other things into.
- `<span>` = an **inline** container — sits within a line of text without breaking it. A highlighter stroke over a few words.

Both are meaning-less on their own — they exist to be grouped and styled with CSS later. Prefer the semantic tags from yesterday (`header`, `section`...) when one fits; reach for `div`/`span` when nothing semantic applies.

## 6. Lists — `<ul>`, `<ol>`, `<li>`

**Unordered list `<ul>`** — order doesn't matter, browser shows bullets. A shopping list:

```html
<ul>
  <li>Tomatoes</li>
  <li>Onions</li>
  <li>Coriander</li>
</ul>
```

**Ordered list `<ol>`** — order IS the point, browser numbers them. A recipe:

```html
<ol>
  <li>Boil water</li>
  <li>Add tea powder</li>
  <li>Add milk and sugar</li>
</ol>
```

Every item — in both — is an `<li>` (list item). Only `<li>` elements go directly inside `<ul>`/`<ol>`.

### Nesting lists

A list inside a list item — note the inner list lives *inside* an `<li>`, before its closing tag:

```html
<ul>
  <li>South Indian
    <ul>
      <li>Dosa</li>
      <li>Idli</li>
    </ul>
  </li>
  <li>North Indian
    <ul>
      <li>Chole Bhature</li>
    </ul>
  </li>
</ul>
```

### `<ol>` extras — `start` and `type`

```html
<ol start="5">          <!-- numbering begins at 5: 5, 6, 7... -->
  <li>Fifth step</li>
  <li>Sixth step</li>
</ol>

<ol type="A">           <!-- A, B, C like exam options -->
  <li>Option one</li>
  <li>Option two</li>
</ol>
```

`type` accepts `1` (default), `A`, `a`, `I`, `i` (Roman numerals — like book chapter numbering).

*(Bonus for the curious: there's also a description list — `<dl>` with `<dt>` terms and `<dd>` definitions — handy for glossaries.)*

## 7. Links — `<a href="...">`

The `<a>` (anchor) tag is what makes the web a *web*:

```html
<a href="https://www.wikipedia.org">Visit Wikipedia</a>
```

`href` = the destination. The text between the tags is what the visitor clicks. Four kinds of destinations:

```html
<!-- 1. Absolute URL — full address, goes anywhere on the internet -->
<a href="https://leetcode.com">LeetCode</a>

<!-- 2. Relative URL — another page of YOUR site, relative to this file -->
<a href="about.html">About me</a>
<a href="../Day-01/dev/index.html">Yesterday's page</a>

<!-- 3. #id — jump to a section ON THIS PAGE (a bookmark) -->
<a href="#recap">Jump to recap</a>
...
<h2 id="recap">Quick recap</h2>

<!-- 4. mailto: — opens the visitor's email app -->
<a href="mailto:hello@example.com">Email me</a>
```

The `#id` trick is how "Back to top" and table-of-contents links work — the `id` attribute is a name-tag you pin on any element, and `#thatname` scrolls to it.

### `target="_blank"` + `rel="noopener"`

```html
<a href="https://leetcode.com" target="_blank" rel="noopener">LeetCode (new tab)</a>
```

- `target="_blank"` opens the link in a **new tab** — the default `_self` replaces the current page.
- Always pair it with `rel="noopener"`: without it, the new page gets a handle back to your page (`window.opener`) and a shady site can misuse it. Habit: `_blank` and `noopener` travel together, like helmet and bike.

Use new tabs for *external* sites (so visitors don't lose your page); keep internal navigation in the same tab.

*(You can also add `title="..."` to any link — a tooltip appears on hover.)*

## 8. Images — `<img>`

```html
<img src="charminar.jpg" alt="Charminar monument at night" width="400" height="300">
```

`<img>` is an empty element — no closing tag. Its attributes do all the work:

- **`src`** — the path to the image file (rules in Section 10). Wrong path = broken-image icon.
- **`alt`** — text shown if the image can't load, and read aloud by screen readers for blind users. Describe *what's in* the picture ("Charminar monument at night"), not "image" or "photo123". Every image needs an `alt`. Non-negotiable.
- **`width` / `height`** — size in pixels. Giving both lets the browser reserve the space *before* the image downloads, so the page doesn't jump around while loading. Keep the original proportion, or the Charminar becomes a squashed Charminar.

Extras worth knowing:

```html
<!-- external image from another server — needs the full absolute URL -->
<img src="https://example.com/photos/tajmahal.jpg" alt="Taj Mahal at sunrise">

<!-- clickable image: img wrapped inside a link -->
<a href="gallery.html"><img src="thumb.jpg" alt="Open the photo gallery"></a>
```

Common formats: `.jpg` (photos), `.png` (screenshots, transparency), `.gif` (animations — yes, GIFs are just `<img>` too), `.svg` (logos/icons that scale without blurring).

## 9. Attributes — the recap

You've now used a pile of attributes. The universal shape:

```html
<tagname attribute="value">content</tagname>
```

- Always written in the **opening tag**, as `name="value"` pairs separated by spaces.
- Always put the value in **quotes** (technically optional sometimes, always safer).
- Met so far: `href`, `target`, `rel`, `title`, `src`, `alt`, `width`, `height`, `start`, `type`, `id`, and `lang` from yesterday's boilerplate.
- Some are boolean-ish or element-specific; wrong attribute on wrong tag is silently ignored — HTML doesn't crash, it just quietly does nothing. That's why typos in HTML are sneaky.

## 10. File paths — where is that file?

Your `src` and `href` need addresses. Two families:

**Absolute path** — the complete public address, works from anywhere:

```html
<img src="https://www.example.com/images/pic.jpg" alt="...">
```

**Relative path** — directions from the *current file's* location, like telling a friend "from my house, two lanes left":

| Path | Meaning |
|---|---|
| `pic.jpg` or `./pic.jpg` | same folder as this HTML file (`./` = "start here") |
| `images/pic.jpg` | inside the `images` subfolder next to this file |
| `../pic.jpg` | one folder UP from here |
| `../../pic.jpg` | two folders up |
| `/images/pic.jpg` | from the website's ROOT folder (leading `/`) |

Example from this repo: from `Day-02/dev/`, reaching a file in `Day-01/dev/` is `../../Day-01/dev/index.html` — up out of `dev`, up out of `Day-02`, then walk down.

**Prefer relative paths for your own files.** They keep working when the site moves — localhost today, a real domain later. An absolute path to your own machine like `C:\Users\you\Desktop\pic.jpg` works ONLY on your computer — the number one reason beginners' images break the moment anyone else opens the page.

## 11. Common mistakes today

1. **Skipping heading levels** or using headings for font size — hierarchy is meaning, not styling.
2. **Multiple `<h1>`s** on one page.
3. **`<br>` spam for spacing** — use paragraphs and (soon) CSS.
4. **Forgetting `alt`** on images — broken for screen readers and for failed loads.
5. **`target="_blank"` without `rel="noopener"`.**
6. **Putting the nested `<ul>` *outside* the `<li>`** — it must sit inside the parent item, before `</li>`.
7. **Content directly inside `<ul>`/`<ol>`** that isn't wrapped in `<li>`.
8. **Backslashes in paths** — the web uses `/` always, even on Windows.
9. **Absolute local paths** (`C:\Users\...`) — works only on your machine.
10. **Spaces/capitals mismatch in filenames** — `Pic.JPG` vs `pic.jpg` are different files on real servers; use lowercase-with-hyphens names.

## 12. Quick recap

- `<h1>`–`<h6>`: one `<h1>`, never skip levels; `<p>` for paragraphs; browser collapses whitespace.
- `<strong>`/`<em>` carry meaning; `<b>`/`<i>` only paint.
- `<br>` breaks a line, `<hr>` breaks a topic; `<div>` = block box, `<span>` = inline box.
- `<ul>` bullets, `<ol>` numbers (`start`, `type`), everything in `<li>`; nest inside the `<li>`.
- `<a href>`: absolute, relative, `#id` bookmark, `mailto:`; `_blank` + `noopener` together.
- `<img src alt width height>`: alt always; sizes stop page-jump.
- Paths: `./` here, `../` up one, `/` from root; relative for your own files.

## 13. Learn more

- [W3Schools — HTML Lists](https://www.w3schools.com/html/html_lists.asp)
- [W3Schools — HTML Links](https://www.w3schools.com/html/html_links.asp)
- [W3Schools — HTML Images](https://www.w3schools.com/html/html_images.asp)
- [W3Schools — HTML File Paths](https://www.w3schools.com/html/html_filepaths.asp)

---

**Tomorrow:** so far the page only *talks* to the visitor. Day 3 flips the conversation — **forms**: text boxes, buttons, checkboxes — letting the visitor talk back.
