[<< Day 02](../../Day-02/dev/notes.md) | [🏠 Today's tasks](../task.md) | [Day 04 >>](../../Day-04/dev/notes.md)

# Day 3 (Night) — HTML Forms and Tables

## So far → Tonight

Every page I've built so far only talks **AT** the visitor — headings, paragraphs, images, links. The visitor reads, clicks, leaves. Tonight the conversation becomes two-way: **forms** let visitors talk **BACK** — type a name, pick a city, press submit. And **tables** let me show rows-and-columns data properly — exam results, train timetables, price lists.

---

## 1. What is a form?

Think of a **bank challan**. It has boxes for name, account number, amount — you fill them, sign, and hand it over at the counter. The clerk (the server) processes it.

An HTML form is the digital challan. `<form>` is the paper, inputs are the boxes, the submit button is handing it to the clerk.

```html
<form action="/register" method="post">
  <!-- input boxes go here -->
  <button type="submit">Register</button>
</form>
```

- **`action`** — *where* the filled data goes (a URL on the server).
- **`method`** — *how* it travels. One-liner: **GET sticks data onto the URL** (`?name=Rahul&city=Pune` — visible, bookmarkable, for searches); **POST hides it in the request body** (for passwords, registrations, anything sensitive or anything that *changes* data).

Rule of thumb: reading data → `get`, sending/changing data → `post`.

---

## 2. The `name` attribute — why submission needs it

This one trips everyone. When the form is submitted, data travels as `name=value` pairs:

```html
<input type="text" name="city">   <!-- user types "Pune" → server gets city=Pune -->
```

**An input without a `name` is simply not sent.** It's a challan box with no label — the clerk has no idea what the number means, so it goes in the dustbin. Every input that should reach the server needs a `name`.

(`name` also does a second job: radio buttons sharing the same `name` become one group where only one can be picked.)

---

## 3. `<input>` and its types

One tag, many disguises — the `type` attribute decides which box appears:

```html
<input type="text"     name="username">           <!-- one-line text -->
<input type="password" name="pin">                <!-- dots instead of letters -->
<input type="email"    name="mail">               <!-- browser checks for @ -->
<input type="number"   name="age" min="1" max="120">
<input type="date"     name="dob">                <!-- calendar picker -->
<input type="checkbox" name="veg">                <!-- ZERO or MORE choices -->
<input type="radio"    name="size" value="s">     <!-- exactly ONE of a group -->
<input type="submit"   value="Send">              <!-- old-style submit button -->
```

- **checkbox** = "tick all that apply" (like choosing toppings).
- **radio** = "pick exactly one" (like choosing S/M/L — same `name` makes them one group; give each a different `value`).

Quick list of the remaining useful types — recognise them on sight:

| Type | What it gives |
|---|---|
| `tel` | phone number box (mobile shows the number keypad) |
| `url` | website address box |
| `file` | a "Choose file" upload button |
| `hidden` | invisible box — data the site sends along without showing the user |
| `range` | a slider (volume-control style) |
| `color` | a colour picker |

---

## 4. `<label>` — and why placeholder is NOT a label

```html
<label for="mail">Email</label>
<input type="email" id="mail" name="mail" placeholder="you@example.com">
```

- The `for` of the label matches the `id` of the input — they become linked. Clicking the label focuses the box (a big deal for tiny checkboxes), and screen readers announce the label when a blind user reaches the field.
- Note the three different attributes doing three different jobs: `id` links to the label, `name` travels to the server, `placeholder` is the faint hint inside the box.

**Placeholder ≠ label.** The placeholder vanishes the moment you type — mid-form you forget what the box was for, and screen readers may skip it entirely. Placeholder is the faint pencil example inside a challan box; the label is the printed heading beside it. Always give a real `<label>`; placeholder is optional extra help.

---

## 5. `<select>`, `<option>`, `<optgroup>` — dropdowns

```html
<label for="city">City</label>
<select id="city" name="city">
  <optgroup label="Maharashtra">
    <option value="mum">Mumbai</option>
    <option value="pun" selected>Pune</option>
  </optgroup>
  <optgroup label="Telangana">
    <option value="hyd">Hyderabad</option>
  </optgroup>
</select>
```

- `<select>` is the dropdown, each `<option>` a choice; `selected` pre-picks one.
- The `value` is what the server receives; the text between the tags is what the human sees.
- `<optgroup>` draws grouped headings inside the list — like a menu card split into "Veg" and "Non-veg".
- Related cousins to recognise: `<textarea>` (next), `<datalist>` (a text box with suggestions), `<fieldset>` + `<legend>` (a titled box grouping related fields), `<output>` (shows a calculated result).

---

## 6. `<textarea>` — the big text box

```html
<label for="msg">Your message</label>
<textarea id="msg" name="msg" rows="4" cols="40"></textarea>
```

For multi-line text — feedback, address, complaint. `rows`/`cols` set the starting size. Unlike `<input>`, it has a closing tag; anything between the tags becomes pre-filled text.

---

## 7. `<button>` and the default-submit trap

```html
<button type="submit">Send</button>   <!-- submits the form -->
<button type="reset">Clear</button>   <!-- wipes all fields -->
<button type="button">Hi</button>     <!-- does nothing until JavaScript arrives -->
```

**The trap:** inside a form, a `<button>` with no `type` defaults to `type="submit"`. So that innocent "Show password" button you added? Clicking it submits the whole form and reloads the page. Rule: **inside a form, always write the `type` explicitly.**

---

## 8. `required` — the bare minimum check

```html
<input type="email" name="mail" required>
```

The browser refuses to submit while the box is empty, free of cost. Combined with `type="email"`, `type="number"` + `min`/`max`, you already get basic checking with zero JavaScript. Deeper validation (patterns, custom messages, styling invalid fields) comes on **Day 5** — tonight, just know `required` exists.

---

## 9. Tables — rows and columns done right

A **railway reservation chart**: rows of passengers, columns of Seat / Name / Age. That grid in HTML:

```html
<table>
  <caption>Class 10-B — Term Results</caption>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ananya</td>
      <td>92</td>
    </tr>
    <tr>
      <td>Rohan</td>
      <td>85</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Class average</td>
      <td>88.5</td>
    </tr>
  </tfoot>
</table>
```

- `<table>` — the whole grid. `<tr>` — one **row**. Cells go *inside* rows, never loose.
- `<th>` — a **header** cell (bold, and announced as a heading by screen readers). `<td>` — a normal **data** cell.
- `<thead>` / `<tbody>` / `<tfoot>` — label the header rows, the data rows, and the summary row. The page looks the same without them, but they give structure meaning — and long printed tables can repeat the `<thead>` on every page.
- `<caption>` — the table's title, first thing inside `<table>`. Like the heading printed on top of the reservation chart.

### `colspan` and `rowspan` — merged cells

```html
<td colspan="2">Total</td>   <!-- one cell stretching across 2 columns -->
<td rowspan="3">North</td>   <!-- one cell stretching down 3 rows -->
```

Exactly like merged cells in Excel. Careful: a cell spanning 2 columns means that row now writes one fewer `<td>` — count your cells per row or the grid goes crooked.

### Never use tables for page layout

In the 2000s people built whole page skeletons out of invisible tables. Never do this. Tables are for **data that is genuinely rows-and-columns** (results, timetables, prices). Page layout is CSS's job — coming soon. Screen readers read tables cell by cell; a layout-table becomes word salad for them.

---

## 10. Accessibility notes for tonight

- **Landmarks still apply** — the form sits inside `<main>`, navigation in `<nav>`, as learned on Day 2. Screen-reader users jump between landmarks like bookmarks.
- **Every input gets a `<label for>`** matched to its `id`. This is the single biggest accessibility win in forms.
- **`scope` on table headers** — `<th scope="col">` says "I head this column", `<th scope="row">` says "I head this row". A screen reader can then announce "Marks: 92" instead of a bare "92".
- Group related radio buttons/checkboxes in a `<fieldset>` with a `<legend>` question — the question gets read out with each option.

---

## Common mistakes I must not make

1. **Input without `name`** — the field silently never reaches the server.
2. **Placeholder used as the only label** — vanishes on typing, unreliable for screen readers. Real `<label>` always.
3. **`for`/`id` mismatch** (or missing `id`) — the label looks fine but is linked to nothing.
4. **Radio buttons with different `name`s** — they stop being a group, and all can be selected at once.
5. **`<button>` without `type` inside a form** — becomes a surprise submit button.
6. **GET for passwords** — the password lands in the URL, browser history, and server logs. Sensitive data → POST.
7. **`<td>` outside a `<tr>`** — cells must live inside rows.
8. **Wrong cell count after `colspan`/`rowspan`** — the grid shifts and looks broken.
9. **Tables for layout** — data only.

## Quick recap

- `<form action method>` is the challan; GET = data on the URL (reads), POST = data in the body (sensitive/changes).
- Data travels as `name=value`; no `name`, no data.
- `<input type>` picks the box: text, password, email, number, date, checkbox (many), radio (one per `name` group) — plus tel, url, file, hidden, range, color.
- `<label for>` ↔ `id`: clickable + screen-reader friendly. Placeholder is a hint, never a label.
- `<select>`/`<option>`/`<optgroup>` = dropdowns; `<textarea>` = multi-line; `<button>` needs an explicit `type` inside forms.
- `required` = free browser-side check; real validation on Day 5.
- Tables: `table > thead/tbody/tfoot > tr > th/td`, `caption` for the title, `colspan`/`rowspan` to merge, `scope` on `<th>` — and never for layout.

## Learn more

- HTML forms — https://www.w3schools.com/html/html_forms.asp
- Form elements — https://www.w3schools.com/html/html_form_elements.asp
- Input types (full list) — https://www.w3schools.com/html/html_form_input_types.asp
- Tables — https://www.w3schools.com/html/html_tables.asp
- MDN on `<form>` — https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form

---

## Tomorrow

Tomorrow night everything so far comes together: headings, lists, links, images, semantic landmarks, and tonight's forms and tables — combined into one real project: **a complete CV page**. My first page that actually looks like something worth shipping.

---

[<< Day 02](../../Day-02/dev/notes.md) | [🏠 Today's tasks](../task.md) | [Day 04 >>](../../Day-04/dev/notes.md)
