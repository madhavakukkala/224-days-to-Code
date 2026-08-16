# Day 3 (Night) — HTML Forms and Tables

Two big topics tonight: **forms** (how a webpage collects information from the user) and **tables** (how it displays rows-and-columns data). Both are everywhere — login pages, railway booking, exam results.

---

## 1. What is a form?

Think of a **bank challan**. It has boxes for your name, account number, amount, date — you fill them, sign, and submit it at the counter. The clerk (the server) then processes it.

An HTML **form** is the digital challan. `<form>` is the paper, inputs are the boxes, and the submit button is handing it to the clerk.

```html
<form action="/register" method="post">
  <!-- input boxes go here -->
  <button type="submit">Submit</button>
</form>
```

- **`action`** — *where* the filled data is sent (a URL on the server).
- **`method`** — *how* it travels:
  - `get` — data is stuck onto the URL (`?name=Rahul&city=Pune`). Visible, bookmarkable. For searches and filters.
  - `post` — data goes hidden inside the request body. For passwords, registrations, payments — anything sensitive or anything that *changes* data.

Rule of thumb: reading data → `get`, sending/changing data → `post`.

---

## 2. `<input>` and its types

`<input>` is one box on the challan. One tag, but its `type` attribute completely changes its behaviour — same actor, different roles.

```html
<input type="text" name="username" placeholder="Enter username">
```

- **`name`** — the label under which the value travels to the server (`username=rahul21`). No `name` = the value is NOT sent at all. Most common beginner bug.
- **`placeholder`** — the grey hint text inside the box. It disappears when you type — so it is *not* a replacement for a label.

The important types:

| type | what it does |
|------|--------------|
| `text` | plain single-line text |
| `email` | text, but the browser checks for a valid email shape (`a@b.c`) on submit; phone keyboards show `@` |
| `password` | hides typing as dots — like covering your ATM PIN with your hand |
| `number` | numbers only, gives up/down arrows; supports `min`, `max`, `step` |
| `date` | opens a calendar picker; no more "is it DD/MM or MM/DD" confusion |
| `checkbox` | on/off boxes; user can tick **many** — like choosing toppings: cheese AND paneer AND corn |
| `radio` | pick exactly **one** from a group — like an OMR answer sheet, one bubble per question |

**Radio grouping trick:** radios become one group by sharing the same `name`. That's how the browser knows ticking one should untick the others.

```html
<input type="radio" name="payment" value="upi" id="upi">
<input type="radio" name="payment" value="cod" id="cod">
```

Same `name="payment"`, different `value`. The chosen `value` is what reaches the server.

Useful extras: `required` (browser blocks submit if empty), `checked` (pre-ticked), `value` (pre-filled / what gets sent). `required` is just the trailer — the full validation story (`pattern`, `minlength`, styling invalid fields) comes on Day 5.

Other types worth recognising (no need to master today): `tel` (phone — shows the number keypad on mobiles), `url` (checks for a link shape), `file` (upload a file), `hidden` (travels with the form but user never sees it — e.g. an order ID), `range` (a slider), `color` (a colour picker).

---

## 3. `<label>` — and why clicking it should focus the input

A **label** is the visible caption for an input ("Email address:"). But it's not just decoration — it must be *connected* to its input using the **`for`/`id` pairing**:

```html
<label for="email">Email address</label>
<input type="email" id="email" name="email">
```

`for` on the label = `id` on the input. Same value. Once paired:

1. **Clicking the label focuses (or toggles) the input.** Huge for checkboxes and radios — the tiny box becomes a big clickable area. Try ticking a checkbox on a phone without this; it's like threading a needle in a moving local train.
2. **Screen readers announce the label** when a blind user reaches the input. Without the pairing, they hear only "edit text" — a box with no clue what to type. With it: "Email address, edit text".

Alternative: wrap the input inside the label (`<label>Email <input ...></label>`) — then no `for`/`id` needed. The explicit `for`/`id` version is the habit to build.

`placeholder` is not a label. It vanishes on typing, is low-contrast, and screen reader support is unreliable. Always give a real `<label>`.

---

## 4. `<select>` + `<option>` — the dropdown

For choosing one item from a long list (like picking your state — 28+ options as radios would be madness):

```html
<label for="state">State</label>
<select id="state" name="state">
  <option value="">-- Choose --</option>
  <option value="MH">Maharashtra</option>
  <option value="KA" selected>Karnataka</option>
  <option value="TN">Tamil Nadu</option>
</select>
```

- `<select>` is the dropdown; each `<option>` is one choice.
- The user sees the text ("Maharashtra"), the server receives the `value` ("MH").
- `selected` pre-picks an option. `multiple` allows many selections.
- `<optgroup label="South">` can group related options under a heading.

---

## 5. `<textarea>` — the big text box

`<input type="text">` is one line. For a paragraph (address, feedback, complaint), use `<textarea>`:

```html
<label for="addr">Delivery address</label>
<textarea id="addr" name="address" rows="4" cols="40"></textarea>
```

- It has a **closing tag**, and any text between the tags becomes pre-filled content (unlike `<input>`, which is self-closing and uses `value`).
- `rows`/`cols` set the visible size (real sizing is better done with CSS).
- Careful: whitespace between `<textarea>` and `</textarea>` shows up inside the box. Keep the tags snug.

---

## 6. Button types — submit vs button

A `<button>` inside a form has a `type`, and the default surprises everyone:

```html
<button type="submit">Register</button>   <!-- sends the form -->
<button type="button">Show/Hide</button>  <!-- does nothing by itself; for JS -->
<button type="reset">Clear</button>       <!-- wipes all fields (rarely wanted) -->
```

- **`submit`** — fills the challan and hands it to the counter: the browser validates (`required`, `email` etc.) and sends the data to `action`.
- **`button`** — an inert button. It only does what your JavaScript tells it to. Use it for toggles, "show password", calculators.
- **The trap:** inside a `<form>`, a `<button>` with **no type is `submit` by default**. So your innocent "Show password" button reloads the whole page. Habit: *always* write the `type` explicitly.

---

## 7. Tables — the railway timetable

A **table** is for genuine rows-and-columns data. Picture the big timetable at the station: train number, name, departure, platform — columns with headings, one row per train.

```html
<table>
  <thead>
    <tr>
      <th>Train</th>
      <th>Departure</th>
      <th>Platform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Deccan Queen</td>
      <td>17:10</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Rajdhani Exp</td>
      <td>16:55</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
```

The tags, one by one:

- **`<table>`** — the whole board.
- **`<tr>`** — table **r**ow. One horizontal line.
- **`<th>`** — table **h**eader cell. Bold + centered by default, but the real value is *meaning*: "this cell names a column (or row)".
- **`<td>`** — table **d**ata cell. The actual values.
- **`<thead>` / `<tbody>`** — group the heading row(s) and the data rows. (`<tfoot>` exists too, for totals.) They add structure: styling hooks, sticky headers via CSS, and screen readers can tell headings from data.

Extras worth knowing:

- `<caption>` — a title for the table, placed right after `<table>`. Screen readers announce it first.
- `colspan="2"` / `rowspan="2"` — a cell stretching across columns/rows (like "SLEEPER CLASS" spanning several columns on a reservation chart).
- `scope="col"` or `scope="row"` on `<th>` — states exactly what the header describes. Helps screen readers say "Departure: 17:10" instead of just "17:10".

**Golden rule:** tables are for *data*, never for page layout. Layout is CSS's job (flexbox/grid). Using tables for layout is a 1999 habit that breaks accessibility and responsiveness.

---

## 8. Why semantics matter — accessibility

**Semantics** = choosing tags by *meaning*, not by looks. A `<div>` styled to look like a button *looks* the same but *means* nothing.

Who depends on the meaning:

1. **Screen readers** (software that reads pages aloud for blind users — NVDA, JAWS, TalkBack). They don't see the page; they read the tag structure. And their users don't move top-to-bottom line by line — they **jump by landmarks**: "list all headings", "jump to the form", "next table", "list all links". Semantic tags (`<header>`, `<nav>`, `<main>`, `<form>`, `<table>`, `<h1>`–`<h6>`) are the signboards that make those jumps possible. A page built only from `<div>`s is a station with no signboards — you can walk, but you can't *navigate*.
2. **Keyboard users** — real `<button>`, `<input>`, `<select>` are focusable with Tab and work with Enter/Space *for free*. A click-handler `<div>` gets none of that.
3. **Browsers** — free validation (`type="email"`, `required`), the right mobile keyboard (number pad for `number`, `@` for `email`), autofill for name/email/address.
4. **Search engines** — better understanding of the page, better results.

Concrete form checklist:

- Every input has a `<label>` paired via `for`/`id`.
- Correct `type` on every input (not `text` for everything).
- Related radios/checkboxes wrapped in `<fieldset>` with a `<legend>` caption:

```html
<fieldset>
  <legend>Payment method</legend>
  <label><input type="radio" name="pay" value="upi"> UPI</label>
  <label><input type="radio" name="pay" value="card"> Card</label>
</fieldset>
```

Without the `<legend>`, a screen reader user hearing just "UPI, radio button" has no idea what question is being answered.

Accessibility isn't charity work — it's correctness. And the semantic version is usually *less* code than the div-soup version.

---

## Common mistakes

1. **Forgetting `name` on inputs** — the field silently never reaches the server.
2. **Using `placeholder` instead of `<label>`** — hint vanishes while typing; screen readers may say nothing.
3. **`for` not matching `id`** (or duplicate `id`s on the page) — label clicks and announcements break. `for` pairs with `id`, NOT with `name`.
4. **Radios with different `name`s** — they stop being a group; the user can select all of them.
5. **`<button>` without an explicit `type` inside a form** — it defaults to `submit` and reloads the page.
6. **Using checkbox where only one choice is valid** (or radio where many are) — checkbox = many, radio = one.
7. **`<input type="text">` for passwords, emails, numbers** — you lose masking, validation, and the right mobile keyboard.
8. **Tables for page layout** — data only. CSS handles layout.
9. **Skipping `<th>`/`<thead>`** and making header cells with bold `<td>`s — looks the same, means nothing to assistive tech.
10. **`get` for sensitive data** — the password ends up printed in the URL and browser history.

---

## Quick recap

- Form = digital bank challan: `<form action method>` wraps inputs; `get` reads, `post` sends.
- `<input type>` decides behaviour: text, email, password, number, date, checkbox (many), radio (one — grouped by same `name`). Also exist: tel, url, file, hidden, range, color. `required` blocks empty submits; deeper validation is Day 5.
- Every input needs a `name` (to travel) and a `<label for>` ↔ `id` pairing (to be clickable and announced).
- `<select>`/`<option>` = dropdown; `<textarea>` = multi-line; content goes between its tags.
- Button types: `submit` sends, `button` is for JS, missing type = `submit` (trap!).
- Table = timetable: `table > thead/tbody > tr > th/td`; `caption` and `scope` for accessibility; never for layout.
- Semantics = meaning. Screen readers navigate by landmarks and labels; correct tags give focus, keyboards, validation and autofill for free.
