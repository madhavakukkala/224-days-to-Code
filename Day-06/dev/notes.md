[<< Day 05](../../Day-05/dev/notes.md) | [🏠 Today's tasks](../task.md) | [Day 07 >>](../../Day-07/dev/notes.md)

# Day 6 (Night) — The `<head>`: Meta Tags, Favicon, Open Graph, W3C Validation

## Where We Are

The CV page is built. The structure is solid — headings, lists, links, table, semantic tags. Tonight we don't add anything visible. Tonight the page gets its **paperwork**:

- its **passport** — meta tags that tell browsers and Google who this page is,
- its **photo-frame for WhatsApp** — Open Graph tags that control how the link looks when shared,
- its **official stamp** — a clean pass through the W3C validator.

Nothing on screen will change. Everything about how the *world* sees your page will.

---

## 1. What Are Meta Tags?

Everything inside `<body>` is FOR humans. Everything inside `<head>` is ABOUT the page — for machines: browsers, Google, WhatsApp.

A `<meta>` tag is one line of information about the page. It never renders on screen. Think of it like the details page of a **passport**: name, nationality, photo. The passenger (page content) is the same either way, but without the passport, airports (browsers, search engines) treat you badly.

Two shapes cover almost everything:

```html
<meta charset="UTF-8">                        <!-- special one-attribute form -->
<meta name="something" content="its value">   <!-- name/content pair -->
```

`<meta>` is a **void element** — no closing tag, like `<br>` and `<img>` from earlier days.

---

## 2. charset="UTF-8" — Teach the Browser to Read

```html
<meta charset="UTF-8">
```

Computers store text as numbers. The **charset** tells the browser which number-to-letter dictionary to use. UTF-8 is the dictionary that covers practically every script on Earth — English, हिन्दी, தமிழ், తెలుగు, emoji, the ₹ symbol, everything.

Skip it and one day your page shows `â‚¹500` instead of `₹500`. That garbled text is called *mojibake*, and this one line prevents it.

Rule: make it the **first** line inside `<head>`, before even `<title>`. The browser needs the dictionary before it reads anything else.

---

## 3. viewport — The Mobile Survival Tag

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Without this tag, a phone assumes your page was made for a desktop, renders it ~980px wide, then zooms out. Result: ant-sized text you must pinch-zoom to read. You've seen those sites. Tonight you learn why they're broken.

Piece by piece:

| Piece | Meaning |
|---|---|
| `name="viewport"` | "I'm giving instructions about the visible window" |
| `width=device-width` | "Make the page as wide as THIS device's screen" — 360px phone gets a 360px page |
| `initial-scale=1.0` | "Start at 100% zoom, no zooming out" |

One line, and your page respects every screen size. When we start CSS next week, responsive design *begins* with this tag.

---

## 4. description — Your Two Lines in Google

```html
<meta name="description" content="CV of Madhava Kukkala — aspiring software engineer learning DSA and web development, one day at a time.">
```

Look at any Google result: a blue title link, then 1–2 lines of grey text under it. That grey text is very often this tag.

- The blue link comes from your `<title>`.
- The grey snippet comes from your `description` (Google may rewrite it if it's poor, but a good one is usually used as-is).

It does not directly boost ranking — but it decides whether a human **clicks**. Treat it like the blurb on the back of a book. Keep it roughly 150–160 characters; longer gets cut with a "...".

(You may see `name="keywords"` in old tutorials. Google has ignored it for years. Skip it.)

---

## 5. robots — One Line

```html
<meta name="robots" content="index, follow">
```

Instructions for search-engine crawlers: "index this page, follow its links". That's also the default, so you rarely need it — but `content="noindex"` is how you hide a page from Google, and knowing this line exists is enough for today.

---

## 6. Favicon — The Face in the Browser Tab

Look at your browser tabs right now. Every site has a tiny icon next to its title. That's the **favicon** (favourite icon). Without one, your page shows a blank default — the web equivalent of no profile photo.

```html
<link rel="icon" href="favicon.ico">
```

Piece by piece:

- `<link>` — connects an external file to the page (same tag that will connect CSS next week).
- `rel="icon"` — the **relationship**: "this file is my icon".
- `href` — where the file lives.

### .ico vs .png

| Format | Story |
|---|---|
| `.ico` | The old classic. Can pack multiple sizes in one file. Browsers even auto-check for `/favicon.ico` if you declare nothing. |
| `.png` | The modern choice. Any image editor makes one. Declare the type: `<link rel="icon" type="image/png" href="favicon.png">` |

### sizes

You can offer different sizes so each device picks the sharpest:

```html
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png">
```

For today, ONE square image (32×32 or larger) is plenty. Favicon changed but browser shows the old one? Hard refresh with `Ctrl+F5` — favicons are cached aggressively.

---

## 7. Open Graph — Make Your Link Beautiful on WhatsApp

Paste a YouTube link into WhatsApp: a neat card appears — image, bold title, small description. Paste a plain page's link: just naked blue text. The difference is **Open Graph (OG) tags**.

When you share a link, WhatsApp's server visits the page, reads the `<head>`, looks for `og:` tags, and builds the preview card from them. You are literally designing that card:

```html
<meta property="og:title" content="Madhava Kukkala — CV">
<meta property="og:description" content="Aspiring software engineer. 224 days of DSA and web dev.">
<meta property="og:image" content="https://example.com/photo.jpg">
<meta property="og:url" content="https://example.com/cv.html">
<meta property="og:type" content="website">
```

Note: OG tags use `property=` instead of `name=` — that's just how the OG standard (created at Facebook, now used by WhatsApp, LinkedIn, Telegram, Discord...) defined it.

### How the card maps

| Card part | Tag |
|---|---|
| Big picture on top | `og:image` |
| Bold line | `og:title` |
| Small grey line | `og:description` |
| Link shown below | `og:url` |

### The absolute-URL trap ⚠️

```html
<meta property="og:image" content="photo.jpg">                      <!-- ✗ broken preview -->
<meta property="og:image" content="https://mysite.com/photo.jpg">   <!-- ✓ works -->
```

A relative path works for YOUR browser because it knows which folder the page came from. WhatsApp's server does not — it needs the complete address, starting with `https://`. This is THE most common reason a preview shows no image. Same rule for `og:url`.

(Which also means: full OG previews only work once your page is hosted on a real URL. Writing the tags now is still correct practice — they'll shine the day you deploy.)

### twitter:card — one line

Twitter/X reads OG tags too but likes one extra hint for the card style:

```html
<meta name="twitter:card" content="summary_large_image">
```

Add it and move on.

---

## 8. The W3C Validator — Your Page's Official Stamp

Think of a vehicle's **PUC certificate**. The bike may run fine without it — but the certificate is official proof it meets the standard, and problems surface at the worst time (a checkpoint) if you skip it. The [W3C validator](https://validator.w3.org) is the PUC test for HTML: browsers are forgiving and will render broken HTML *somehow*, but "renders somehow" is not "correct".

### Step by step

1. Open **https://validator.w3.org**.
2. Three ways to submit — for a local file, either:
   - **Validate by File Upload** → choose your `index.html`, or
   - **Validate by Direct Input** → paste your whole HTML source.
3. Click **Check**.
4. Read the results: **errors** (red — real rule violations) and **warnings** (yellow — advice). Each shows the line number and an explanation.
5. Fix the FIRST error in your editor, save, re-check. One early error (like an unclosed tag) often causes a chain of later ones — fixing the top one can clear ten.
6. Repeat until: **"Document checking completed. No errors or warnings to show."** That green message is your stamp. Screenshot-worthy.

### Common errors decoded

| Validator says | It means | Fix |
|---|---|---|
| "Element X not allowed as child of element Y" | Wrong nesting, e.g. `<li>` outside a list, `<p>` inside `<span>` | Restructure per the rules from Day 2–3 |
| "Unclosed element X" | You opened a tag and never closed it | Add the closing tag |
| "Stray end tag X" | A closing tag with no matching opening tag | Remove it or fix the pair |
| "An img element must have an alt attribute" | Image missing its text description | Add `alt="..."` (Day 3 lesson!) |
| "Duplicate ID X" | Same `id` used twice | ids must be unique — rename one |
| "Attribute X not allowed on element Y" | Typo or misplaced attribute | Check spelling and which tag it belongs on |
| "Section lacks heading" (warning) | A `<section>` with no `<h2>`-type heading | Add a heading or use `<div>` |

---

## 9. Common Mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| No `charset` line | ₹, emoji, Hindi text turn to garbage | `<meta charset="UTF-8">` first in `<head>` |
| No viewport tag | Tiny zoomed-out page on phones | Add the standard viewport line |
| Meta tags placed in `<body>` | Ignored by tools, validator errors | All metadata lives in `<head>` |
| Relative path in `og:image` | Blank WhatsApp preview | Full `https://...` URL |
| Description 300+ chars | Google chops it with "..." | Keep it ~150–160 characters |
| Writing `<meta ...></meta>` | Invalid — void element | No closing tag on `<meta>` or `<link>` |
| Old favicon still showing | Browser cached it | Hard refresh `Ctrl+F5` |
| Fixing validator errors bottom-up | Chasing ghost errors | Always fix the FIRST error, re-check |

---

## 10. Quick Recap

- `<head>` = machine-facing paperwork; `<body>` = human-facing content.
- `charset="UTF-8"` first — the reading dictionary.
- viewport = "fit MY screen, 100% zoom" — mobile survival.
- description = your two grey lines in Google; sells the click.
- favicon via `<link rel="icon">` — the tab's profile photo.
- OG tags design the WhatsApp/LinkedIn preview card; `og:image` and `og:url` must be **absolute** URLs.
- W3C validator = the PUC certificate; iterate until zero errors AND zero warnings.

---

## 11. Learn More

- [W3Schools — HTML Head](https://www.w3schools.com/html/html_head.asp)
- [W3Schools — Meta Tag Reference](https://www.w3schools.com/tags/tag_meta.asp)
- [The Open Graph Protocol](https://ogp.me/)
- [W3C Markup Validator](https://validator.w3.org)
- [MDN — What's in the head?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata)

---

## Next Week

The structure is complete and certified. Next week: **CSS** — colours, fonts, spacing, layout. The CV finally stops looking like a 1995 document and starts looking like *you*. The skeleton is done; time to dress it up.

---

[<< Day 05](../../Day-05/dev/notes.md) | [🏠 Today's tasks](../task.md) | [Day 07 >>](../../Day-07/dev/notes.md)
