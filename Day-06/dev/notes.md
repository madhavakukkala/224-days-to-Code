# Day 6 (Night) — Meta Tags, Favicon, Open Graph, W3C Validator

Tonight is about the invisible-but-important stuff in the `<head>` of a page. Users don't "see" these tags directly, but browsers, Google, and WhatsApp read them constantly.

---

## 1. Meta tags — the page's ID card

Meta tags live inside `<head>` and describe the page *about* itself. Like the label on a tiffin box — the food is inside, but the label tells you what it is without opening it.

### `charset` — which alphabet to use

```html
<meta charset="UTF-8">
```

**Charset** = character set, the encoding used to read the text bytes. UTF-8 covers basically every language — English, Hindi (नमस्ते), emoji, the ₹ symbol. Without it, some browsers may render junk like `à¤¨` instead of Hindi letters. Always the FIRST tag inside `<head>`.

### `viewport` — make the page mobile-friendly

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Without this, a phone pretends to be a ~980px desktop screen and shrinks the whole page — text becomes ant-sized and users pinch-zoom to read. This tag says: "render at the device's real width, at 100% zoom." One line, and the page respects mobile screens. Non-negotiable in 2026 — most Indian traffic is mobile.

### `description` — the line under your link on Google

```html
<meta name="description" content="Daily DSA and web dev learning tracker — one problem, one concept, every day.">
```

This is the grey text Google usually shows under your page title in search results. It does not directly boost ranking, but a good one makes people actually click. Keep it 150–160 characters, honest, and specific.

Full starter `<head>`:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Short honest summary of this page.">
  <title>My Page Title</title>
</head>
```

---

## 2. Favicon — the tiny logo on the browser tab

**Favicon** = "favorite icon", the small image on the browser tab, in bookmarks, and in history. It is how you spot your tab among 20 open ones — like spotting your bag by the keychain on the zip.

How to link one:

```html
<link rel="icon" type="image/png" href="favicon.png">
```

- `rel="icon"` tells the browser "this is my tab icon".
- Any small square image works: `.png`, `.ico`, even `.svg` in modern browsers. 32x32 or 48x48 px is enough for a tab.
- Old convention: a file literally named `favicon.ico` in the site's root folder gets picked up even without a `<link>` tag. The `<link>` tag is still the explicit, reliable way.

If no favicon: the tab shows a boring default globe/blank icon. Small thing, big polish.

---

## 3. Open Graph — why shared links show a preview card

Share a link on WhatsApp and sometimes you get a rich card — image, bold title, small description. Share another link and you get just plain blue text. The difference is **Open Graph (OG) tags**.

When you paste a link, WhatsApp/LinkedIn/Twitter's server visits the page, reads the `og:` tags from `<head>`, and builds the preview card from them. No tags → no card (or an ugly guess).

```html
<meta property="og:title" content="My DSA Learning Tracker">
<meta property="og:description" content="One problem a day. Follow the journey.">
<meta property="og:image" content="https://mysite.com/preview.png">
<meta property="og:url" content="https://mysite.com/">
<meta property="og:type" content="website">
```

- `og:title` — bold heading on the card.
- `og:description` — small text below the title.
- `og:image` — the picture on the card. Must be a **full absolute URL** (`https://...`), not a relative path like `preview.png` — WhatsApp's server can't resolve relative paths. Recommended size ~1200x630 px.
- `og:url` — the official (canonical) link for the page.
- `og:type` — usually `website` or `article`.

Why care: a link with a nice card gets tapped far more than a plain URL. It's the difference between a hand-written poster and a printed flex banner for the same shop.

Note: these use `property="og:..."` (not `name=`) — that's just how the Open Graph standard was defined.

---

## 4. W3C Validator — the pollution certificate for your HTML

**W3C** (World Wide Web Consortium) is the body that writes the official HTML rules. Their free validator at **https://validator.w3.org** checks whether your page follows those rules.

Think of it as the PUC (pollution) check for a vehicle. The bike may still run without the certificate, but passing means the engine is clean and legal. Same here: browsers are forgiving and will render broken HTML *somehow*, but validated HTML behaves predictably across browsers, is friendlier to screen readers, and looks professional.

### How to validate — mini walkthrough

1. Open https://validator.w3.org
2. Pick one of three tabs:
   - **Validate by URI** — if the page is live on the internet, paste its URL.
   - **Validate by File Upload** — upload the `.html` file (best for local files).
   - **Validate by Direct Input** — paste the raw HTML text into the box.
3. Click **Check**.
4. Read the report:
   - **Errors** (red) — actual rule violations. Fix every single one.
   - **Warnings** (yellow) — legal but questionable. Fix these too; aim for a clean sheet.
5. Each message gives a **line number** and a short explanation. Click through, open your file at that line, fix, save.
6. Re-upload and check again. Repeat until: **"Document checking completed. No errors or warnings to show."** That green message = certificate issued.

### Errors I should expect to see (and their fixes)

| Validator says | It means | Fix |
|---|---|---|
| "Element X not allowed as child of Y" | Wrong nesting, e.g. `<li>` outside `<ul>` | Restructure the tags |
| "Unclosed element" / "Stray end tag" | Opened a tag and never closed it (or vice versa) | Match every open with a close |
| "An img element must have an alt attribute" | Image without `alt` text | Add `alt="what the image shows"` |
| "Duplicate ID" | Same `id` value used twice | IDs must be unique per page; use `class` for repeats |
| "Obsolete attribute" (e.g. `align`, `bgcolor`) | Old-style styling in HTML | Move it to CSS |
| "Missing lang attribute" warning | `<html>` has no language | `<html lang="en">` |

Fix errors **top to bottom** — one early mistake (like an unclosed tag) often causes a cascade of fake errors below it. Fixing the first one can clear ten at once.

---

## Common mistakes

1. **Putting meta tags in `<body>`.** They only work inside `<head>`.
2. **Forgetting the viewport tag**, then wondering why the page looks tiny on a phone.
3. **Relative path in `og:image`.** WhatsApp needs the full `https://...` URL or the card shows no image.
4. **Testing OG tags only on localhost.** WhatsApp's server must be able to reach the page — it can't visit your laptop. OG previews need a live/hosted URL.
5. **Expecting an updated OG image to change instantly.** Platforms cache previews; the old card can stick around for a while.
6. **Ignoring validator warnings** because "the page still works". Warnings are tomorrow's cross-browser bugs.
7. **Fixing validator errors bottom-up.** Start from the first error — later ones are often side effects of it.
8. **Description tag stuffed with keywords.** Google may ignore it and write its own snippet; write one honest human sentence instead.

## Quick recap

- `<meta charset="UTF-8">` — read text correctly, first tag in `<head>`.
- `<meta name="viewport" ...>` — page renders properly on mobile.
- `<meta name="description" ...>` — the grey line under your Google result.
- Favicon: `<link rel="icon" href="favicon.png">` — the tab's tiny logo.
- Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) — turns a shared link into a preview card on WhatsApp/LinkedIn; `og:image` must be an absolute URL.
- W3C validator (validator.w3.org): upload page → fix every error and warning → green "no errors" message = clean HTML, like a fresh PUC certificate.
