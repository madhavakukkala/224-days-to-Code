# Day 5 (Night) — HTML Forms Deep-Dive

Yesterday I learned that a form is how a webpage collects information. Today: how to make forms that **validate themselves**, are **grouped properly**, and are **usable by everyone** — all before writing a single line of JavaScript.

---

## 1. Built-in Validation Attributes

Validation = checking that what the user typed makes sense BEFORE the form is submitted. HTML gives you this for free with attributes on `<input>`.

### `required`

The field cannot be empty. Try to submit an empty required field and the browser blocks the submit and shows a message.

```html
<input type="text" name="name" required>
```

### `minlength` / `maxlength`

Minimum and maximum number of CHARACTERS allowed.

```html
<input type="text" name="username" minlength="3" maxlength="20">
```

Nice detail: `maxlength` doesn't just complain — the browser simply won't let you type past it.

### `min` / `max`

Same idea but for NUMBERS (works with `type="number"`, `type="date"`, `type="range"`).

```html
<input type="number" name="age" min="18" max="100">
```

`minlength` counts characters; `min` compares values. `minlength="2"` means "at least 2 characters"; `min="2"` means "the number must be 2 or bigger". Easy to mix up.

### `pattern` — match a shape

`pattern` takes a **regex** (regular expression — a mini-language for describing text shapes). The input must match the whole pattern.

The classic Indian example — a 10-digit mobile number:

```html
<input type="tel" name="mobile" pattern="[0-9]{10}"
       title="Enter a 10 digit mobile number">
```

Reading the regex: `[0-9]` means "any one digit from 0 to 9", and `{10}` means "exactly 10 of the previous thing". So: exactly ten digits, nothing else. `9876543210` passes; `98765` fails; `98765-43210` fails (the dash is not a digit).

The `title` text shows up in the browser's error bubble, so always add a human hint alongside `pattern`.

Slightly stricter version (Indian mobiles start with 6–9): `pattern="[6-9][0-9]{9}"` — one digit from 6–9, then nine more digits.

### `type="email"` — free email checking

```html
<input type="email" name="email" required>
```

The browser itself rejects things like `rahul@`, `rahul.com`, or `@gmail.com` — no code from me. Bonus: on mobile phones, `type="email"` opens a keyboard with `@` and `.` handy. Same trick family: `type="tel"` opens the number pad, `type="url"` expects a web address.

---

## 2. Why Built-in Validation Beats JavaScript-First

It's tempting to think "real developers validate with JavaScript". But start with HTML validation, always:

1. **It's free.** Zero lines of code. Less code = fewer bugs.
2. **It speaks the user's language.** The browser shows the error message in whatever language the user's browser is set to — Hindi, Tamil, Marathi — automatically. My hand-written JavaScript message would be English-only unless I translate it myself.
3. **It works even when JavaScript fails.** Slow network, script error, JS blocked — HTML validation still works because the browser itself does it.
4. **Consistent look.** Error bubbles match every other site on that browser, so users already know them.

The right mental model: HTML validation is the **ticket checker at the station gate** — cheap, always on duty, catches the obvious cases. JavaScript is for the EXTRA checks HTML can't do (like "do these two password fields match?"). And the golden rule: **the server must validate again anyway** — anyone can bypass the browser, so the browser check is for user convenience, the server check is for safety.

---

## 3. Grouping with `<fieldset>` and `<legend>`

Long forms need sections — exactly like an exam OMR sheet has separate boxes for "Personal Details", "Exam Centre Choice", etc. You don't dump 30 blanks in one heap.

- `<fieldset>` draws a box around a group of related inputs.
- `<legend>` is the group's title, sitting on the box's border.

```html
<fieldset>
  <legend>Personal Details</legend>
  <label for="name">Name</label>
  <input type="text" id="name" name="name">

  <label for="email">Email</label>
  <input type="email" id="email" name="email">
</fieldset>

<fieldset>
  <legend>Preferences</legend>
  <label><input type="checkbox" name="newsletter"> Send me updates</label>
</fieldset>
```

Two real benefits beyond looks:

- **Screen readers** (software that reads pages aloud for blind users) announce the legend before each field — "Personal Details, Name" — so users always know which section they're in.
- Radio button groups belong in one fieldset with the question as the legend, so the question and the options stay logically tied together.

---

## 4. `autocomplete` — help the browser help the user

The `autocomplete` attribute tells the browser exactly WHAT a field is, so it can auto-fill saved values. One tap instead of typing your address for the 50th time.

```html
<input type="text"  name="name"   autocomplete="name">
<input type="email" name="email"  autocomplete="email">
<input type="tel"   name="mobile" autocomplete="tel">
<input type="text"  name="pin"    autocomplete="postal-code">
```

These values are standardized — `name`, `email`, `tel`, `street-address`, `postal-code`, `bday`, and many more. Use the standard word, not your own invention. `autocomplete="off"` asks the browser NOT to autofill (rarely needed; browsers sometimes ignore it for things like passwords anyway).

This is also an accessibility feature: people with motor difficulties or memory issues benefit hugely from not retyping.

---

## 5. Accessibility Essentials

Accessibility (often written **a11y**) = making the page usable by everyone, including people using screen readers, keyboard-only navigation, or with low vision.

### Every input needs a `<label>`. No exceptions.

```html
<label for="email">Email</label>
<input type="email" id="email" name="email">
```

The `for` attribute must match the input's `id`. Two things this buys:

1. A screen reader reads "Email" when the user reaches the box. Without a label it just says "edit text" — imagine filling a form blindfolded where every blank is unlabeled.
2. Clicking the label focuses/toggles the input — a much bigger tap target on mobile (great for checkboxes).

### Placeholder is NOT a label

```html
<!-- BAD: no label at all -->
<input type="text" placeholder="Enter your name">
```

Why placeholder-only fails:

- **It vanishes the moment you type.** Halfway through a long form you look back and can't remember what each filled box was asking. A label stays put.
- Placeholder text is usually low-contrast grey — hard to read for low-vision users.
- Some screen readers skip it entirely.

Placeholder's real job: an example of the FORMAT, next to a real label. Label says "Mobile number", placeholder says "9876543210".

### Small extras that matter

- Keep a sensible top-to-bottom order in the HTML — keyboard users move with Tab, and Tab follows the code order.
- Don't remove the focus outline (the ring around the active field) in CSS without replacing it — keyboard users navigate by it.
- The submit `<button>` should have real text ("Send message"), not just an icon.

---

## 6. Checklist — Adding a Contact Form to the CV Page

The plan for `index.html`: a contact section with name, email, mobile, message, and a submit button.

- [ ] `<form>` element with `action` and `method="post"` (even if the action is a dummy for now)
- [ ] Wrap the fields in a `<fieldset>` with `<legend>Contact Me</legend>`
- [ ] **Name**: `<input type="text">` + `<label>` + `required` + `autocomplete="name"` + `minlength="2"`
- [ ] **Email**: `<input type="email">` + `<label>` + `required` + `autocomplete="email"`
- [ ] **Mobile**: `<input type="tel">` + `<label>` + `pattern="[6-9][0-9]{9}"` + a `title` hint + `autocomplete="tel"` + placeholder showing the format only
- [ ] **Message**: `<textarea>` + `<label>` + `required` + `maxlength="500"` + `rows`/`cols` for size
- [ ] Every `label`'s `for` matches its input's `id`; every input also has a `name` (that's the key sent to the server)
- [ ] Submit: `<button type="submit">Send message</button>` with real text
- [ ] Test 1: submit empty → browser should block and point at the first required field
- [ ] Test 2: type `abc@` in email → browser should reject it
- [ ] Test 3: type a 5-digit mobile → pattern message (with my `title` text) should appear
- [ ] Test 4: unplug the mouse — fill the whole form with Tab + typing only

---

## Common mistakes

- Using placeholder as the label. It disappears on typing; screen readers may skip it. Always a real `<label>`.
- `<label>` whose `for` doesn't match any `id` — looks fine visually, but the link is broken for screen readers and clicks.
- Forgetting `name` on an input. Without `name`, the field's value is simply not sent when the form submits.
- Confusing `minlength` (characters) with `min` (numeric value).
- Writing a `pattern` but no `title` — the user gets a vague "match the requested format" with no clue what format.
- Trusting browser validation as security. It's convenience; the server must re-check everything.
- Regex too strict: `pattern="[0-9]{10}"` rejects `+91 98765 43210`. Decide the accepted format first, then write the pattern, and show the format in the placeholder.

## Quick recap

- HTML validates for free: `required`, `minlength`/`maxlength` (characters), `min`/`max` (values), `pattern` (regex, e.g. `[0-9]{10}` = exactly 10 digits), `type="email"`.
- Built-in beats JS-first: zero code, error messages in the user's own language, works even without JavaScript. JS only for checks HTML can't express; server always re-validates.
- `<fieldset>` + `<legend>` = sections of an OMR form; screen readers announce the section name.
- `autocomplete="name" / "email" / "tel"` lets the browser auto-fill from saved data.
- Every input gets a `<label for=...>` matched to its `id`. Placeholder is a format example, never a label — it vanishes when you type.
- Contact form checklist is ready — next session: build it into the CV page and run the four tests.
