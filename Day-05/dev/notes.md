# Day 5 (Night) — Forms That Validate Themselves

## Yesterday → Tonight

Last night the CV page got its structure — sections, headings, a proper skeleton. Tonight its **contact form grows a brain**: it learns to reject bad input *politely*, before anything is even sent. And the best part — all of it with pure HTML attributes. Zero JavaScript.

---

## 1. What "validation" means

Validation = checking that what the visitor typed makes sense BEFORE the form is submitted. An empty name, a phone number with 4 digits, an email without `@` — the browser can catch all of these for free, if you ask it to. You ask with **attributes** on `<input>`.

---

## 2. `required` — "this field cannot be empty"

```html
<input type="text" name="name" required>
```

Submit with this empty → the browser blocks the submit and shows a message near the field. Like the bank form counter clerk who slides the form right back: *"Naam toh likhiye, sir."* Nothing proceeds until the blank is filled.

Note: `required` has no value. Its presence alone is the instruction.

---

## 3. `minlength` / `maxlength` vs `min` / `max` — characters vs values

These two pairs look like twins. They are not.

### `minlength` / `maxlength` — count of CHARACTERS

```html
<input type="text" name="username" minlength="3" maxlength="20">
```

Nice detail: `maxlength` does not even complain — the browser simply **refuses to let you type** past the limit.

### `min` / `max` — the VALUE itself

For `type="number"`, `type="date"`, `type="range"`:

```html
<input type="number" name="age" min="18" max="100">
<input type="date" name="dob" max="2008-08-16">
```

The trap, spelled out:

- `minlength="2"` → "at least 2 **characters**" — `"99"` passes, `"5"` fails.
- `min="2"` → "the **number** must be 2 or bigger" — `5` passes, `1` fails.

Characters vs value. Read the attribute name twice before using it.

Bonus cousin: `step` sets the legal jumps for numbers — `step="500"` on a donation field allows 500, 1000, 1500...

---

## 4. `pattern` — describe the exact shape you accept

When the built-ins are not enough, `pattern` lets you give a **regular expression (regex)** — a mini-language for describing text shapes. The value must match the WHOLE pattern, checked at submit time.

```html
<input type="tel" name="phone" pattern="[0-9]{10}"
       title="Enter a 10-digit mobile number">
```

### Reading `[0-9]{10}` slowly

- `[0-9]` → "one character from this menu: any digit 0 to 9".
- `{10}` → "exactly 10 of the thing just before me".
- Together: **exactly ten digits, nothing else**. `9876543210` passes; `98765-43210` fails (the `-` is not on the menu); `987654321` fails (only 9).

### Level up: an Indian mobile number, `[6-9][0-9]{9}`

Indian mobile numbers start with 6, 7, 8 or 9. Read it character by character:

- `[6-9]` → the FIRST character must be 6, 7, 8 or 9.
- `[0-9]{9}` → then exactly nine more digits, any digits.
- Total: 1 + 9 = 10 digits, with a rule on the first one. `9876543210` passes; `1234567890` fails at the very first character.

A few more menu tricks for later: `[A-Za-z]{3}` = exactly three letters; `.{8,}` = any 8 or more characters (a minimum-length password); `https?://.+` = must start with `http://` or `https://`.

### Always pair `pattern` with `title`

The browser shows the `title` text in the error bubble. Without it, the visitor sees a useless *"Please match the requested format"* and has to guess. With it, they see *"Enter a 10-digit mobile number"*. One attribute, much kinder form.

---

## 5. Free validation from `type` itself

Some input types come with built-in checks — no `pattern` needed:

```html
<input type="email" name="email">   <!-- must look like an email: something@something -->
<input type="url"   name="site">    <!-- must look like a URL -->
<input type="tel"   name="phone">   <!-- NO validation! but mobiles show the number keypad -->
```

- `type="email"` rejects `rahul-at-gmail` for free. Add `multiple` and it accepts comma-separated emails.
- `type="url"` rejects plain words that are not URL-shaped.
- `type="tel"` is the odd one out: phone formats differ wildly across countries, so browsers validate **nothing** — its gift is the numeric keypad on phones. Pair it with `pattern` for the actual checking (exactly what we did above).

---

## 6. WHEN does validation fire? (and how to switch it off)

Built-in validation runs at **submit time** — the moment the submit button is pressed. Not while typing. The browser checks every field, stops at the first failure, scrolls to it, and shows the bubble. Nothing leaves the page until all checks pass.

Like the counter clerk who checks your **completed** form when you hand it over — not peering over your shoulder at every letter.

### `novalidate` — the off switch

```html
<form action="/submit" novalidate>
```

Put `novalidate` on the `<form>` and the browser skips ALL checks on submit. Why would anyone want that? Mostly for **testing** — e.g. checking that your server also validates (it always must; browser validation is a courtesy, not a security wall — anyone can bypass it).

---

## 7. Instant feedback with two CSS pseudo-classes

Validation *fires* at submit, but the browser *knows* a field's validity every moment. CSS can peek at that live:

```css
input:valid   { border-color: green; }
input:invalid { border-color: red; }
```

One line each, zero JavaScript, and fields show live red/green borders as the visitor types. (Polish for later: `input:invalid:not(:focus)` waits until they leave the field, so it doesn't shout while they are mid-typing.)

---

## 8. `fieldset` + `legend` — group related fields

A long form is friendlier in labelled sections — like an **OMR exam form**, where the sheet has ruled boxes: "Personal details" here, "Exam centre choice" there. In HTML those printed boxes are `fieldset`, and the box's printed heading is `legend`:

```html
<fieldset>
  <legend>Contact details</legend>
  <label for="email">Email</label>
  <input type="email" id="email" name="email" required>

  <label for="phone">Mobile</label>
  <input type="tel" id="phone" name="phone" pattern="[6-9][0-9]{9}"
         title="10-digit Indian mobile number">
</fieldset>
```

The browser draws a border around the group with the legend sitting on the border. More than looks: **screen readers announce the legend** with each field inside, so "Email" is heard as "Contact details — Email". Structure that everyone benefits from.

---

## 9. `autocomplete` — help the browser help the visitor

The browser remembers what people have typed before and offers to fill it in — IF you tell it what each field is:

```html
<form autocomplete="on">
  <input type="text"  name="name"  autocomplete="name">
  <input type="email" name="email" autocomplete="email">
  <input type="tel"   name="phone" autocomplete="tel">
  <input type="text"  name="pin"   autocomplete="postal-code">
</form>
```

Standard values like `name`, `email`, `tel`, `street-address`, `postal-code`, `bday` are a fixed vocabulary — use the official words and the browser fills forms in one tap. `autocomplete="off"` turns suggestions off for one field (say, a one-time code). Filling one field in one tap instead of typing 40 characters on a phone — that is real kindness.

---

## 10. Accessibility — the part most people skip (don't)

### Every input needs a paired `<label>`

```html
<label for="email">Email</label>
<input type="email" id="email" name="email">
```

The `for` value must equal the input's `id`. Two gifts: clicking the label focuses the input (a bigger tap target on phones), and screen readers announce *"Email, edit text"* instead of just *"edit text"*.

### A placeholder is NOT a label

```html
<!-- BAD: label-less, placeholder doing a job it cannot do -->
<input type="text" placeholder="Your name">
```

The placeholder **vanishes the moment typing starts**. Halfway through a long form the visitor forgets what the field was — and the hint is gone. It is also low-contrast grey and often skipped by screen readers. Placeholder = a small extra hint (*"e.g. 500001"*). Label = the field's actual name. You need the label; the placeholder is optional garnish.

### Errors must be ANNOUNCED, not just coloured

Marking a bad field only by turning its border red fails twice: colour-blind visitors (roughly 1 in 12 men) may not see the difference, and screen readers do not read border colours at all. Every error needs **words** — visible text near the field saying what is wrong. The browser's built-in bubbles already do this, which is one more reason to lean on them (with good `title` texts) before reaching for custom JavaScript later.

---

## 11. Tonight's build: the contact-form checklist

Add a contact form to the CV page. Work down this list:

- [ ] `<form>` with `action` and `method="post"`
- [ ] Everything wrapped in a `<fieldset>` with a `<legend>` ("Contact me")
- [ ] Name: `type="text"`, `required`, `minlength="2"`, paired `<label>`
- [ ] Email: `type="email"`, `required`, `autocomplete="email"`, paired `<label>`
- [ ] Mobile: `type="tel"`, `pattern="[6-9][0-9]{9}"`, a helpful `title`, paired `<label>`
- [ ] Message: `<textarea>` with `required` and `maxlength="500"`, paired `<label>`
- [ ] Placeholders only as *extra* hints — never instead of labels
- [ ] Submit button; then TEST: submit empty, submit a 5-digit phone, submit `abc` as email — watch each polite rejection
- [ ] Optional shine: the `:valid` / `:invalid` CSS one-liners

---

## Common mistakes

- Using a placeholder as the label. It disappears on typing — always give a real `<label>`.
- `<label>` without `for`, or `for` not matching the input's `id` — the pairing silently does nothing.
- Mixing up `min`/`max` (value) with `minlength`/`maxlength` (character count).
- `pattern` without `title` — the visitor gets "please match the requested format" and no clue what format.
- Expecting `type="tel"` to validate the number. It doesn't — add `pattern`.
- Writing `pattern="[0-9]{10}"` and being surprised `+91 98765...` fails — spaces, `+`, `-` are not on the `[0-9]` menu. Decide the exact shape you accept first.
- Forgetting `name` on inputs — a field without `name` is not submitted at all, valid or not.
- Trusting browser validation as security. Anyone can bypass it (`novalidate`, or bypassing the browser entirely) — the server must re-check everything.
- Showing errors by colour only. Words, always.

---

## Quick recap

- HTML validates for free: `required` (must fill), `minlength`/`maxlength` (character count), `min`/`max`/`step` (value), `pattern` (exact shape).
- Regex reading: `[0-9]{10}` = ten digits exactly; `[6-9][0-9]{9}` = Indian mobile — first digit 6–9, then nine more. Always pair `pattern` with a human `title`.
- `type="email"` / `type="url"` validate their shapes for free; `type="tel"` only brings the keypad — bring your own `pattern`.
- Validation fires at **submit time**; `novalidate` on the form switches it off (for testing — the server must always validate anyway).
- `input:valid` / `input:invalid` in CSS give live red/green feedback in two lines.
- `fieldset` + `legend` = the OMR form's labelled boxes; screen readers announce the legend with every field inside.
- `autocomplete` with standard values (`name`, `email`, `tel`, `postal-code`) = one-tap form filling.
- Accessibility three: label paired via `for`/`id`, placeholder ≠ label, errors in words not colour alone.

---

## Learn more

- W3Schools — HTML form attributes: <https://www.w3schools.com/html/html_forms_attributes.asp>
- W3Schools — HTML input attributes: <https://www.w3schools.com/html/html_form_attributes.asp>
- W3Schools — the `pattern` attribute: <https://www.w3schools.com/tags/att_input_pattern.asp>
- MDN — Client-side form validation: <https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation>
- MDN — `autocomplete` values: <https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete>

---

## Tomorrow night

The page gets its **passport**: meta tags — the invisible lines in `<head>` that tell browsers, Google, and WhatsApp who this page is. Including the glow-up everyone notices: making your CV link unfurl into a **proper WhatsApp preview** with title, description and image. Same page, suddenly presentable everywhere it travels.
