# Day 01 — Python Basics: Variables, Input/Output, f-strings, Type Casting

Welcome! This is **Day 1 of 224**. You need **zero** prior knowledge to be here — if you have never written a line of code, you are in exactly the right place.

Here is how this repo works, every single day: open `task.md` first, **attempt** everything on your own (yes, even badly — badly is how everyone starts), and only then open these notes to check and fill the gaps.

Struggling before reading is the whole trick. That struggle is where learning actually happens. Let's begin.

---

## 1. What is programming, even?

Programming is writing **instructions** for a computer in a language it understands. The computer is like a very fast, very obedient, very literal-minded worker. It does *exactly* what you say — not what you *meant*. Python is one such language, and it is famous for reading almost like plain English. That is why we start with it.

---

## 2. Setup — your kitchen before cooking

Before making chai, you need a stove, a pan, and tea powder. Before coding, you need:

| Thing | What it is | Why you need it |
|---|---|---|
| **Python 3.12** | The language itself. A program that reads your `.py` files and runs them. | Without it, your code is just text. Download from [python.org](https://www.python.org/downloads/). While installing on Windows, **tick "Add Python to PATH"** — this lets you run `python` from anywhere. |
| **VS Code** | A free code editor from Microsoft. Like MS Word, but built for code. | It colours your code, points out typos, and runs programs with one click. Get it from [code.visualstudio.com](https://code.visualstudio.com/). Install the **Python extension** inside it (search "Python" in the Extensions panel). |
| **LeetCode account** | A website full of coding problems, used by companies for interviews. | This is your practice ground for the next 224 days. Interviews at almost every product company ask LeetCode-style questions. |
| **GeeksforGeeks account** | An Indian site with articles + problems for every CS topic. | Great explanations in simple language, and its own practice portal. When LeetCode feels hard, GFG articles rescue you. |

**Quick check:** open a terminal (in VS Code: `Terminal → New Terminal`) and type `python --version`. If you see `Python 3.12.x`, your stove is lit.

---

## 3. Variables — labelled dabbas

A **variable** is a name that points to a value. Think of your kitchen shelf: a steel dabba labelled `sugar` with sugar inside. The label is the variable name; the contents are the value.

```python
age = 25
name = "Priya"
```

The `=` here means "**store** the right side under the name on the left". It is *not* the maths "equals".

A variable is **created the moment you first assign to it**. No announcement needed. In languages like C or Java you must first declare "this box will hold an integer". Python skips that ceremony.

### Naming rules (Python will refuse otherwise)

- Must start with a **letter** or **underscore** `_` — never a digit. `1st_rank = 5` → error. `rank1 = 5` → fine.
- Can contain letters, digits, underscores. **No spaces, no hyphens**, no `@`/`#`.
- Cannot be a reserved keyword like `if`, `for`, `print`... Python already uses those words.
- Python is **case-sensitive**: `Age`, `age`, and `AGE` are **three different dabbas**. Mixing them up is a classic Day-1 bug.

### snake_case — the Python dress code

Multi-word names use lowercase with underscores: `total_price`, `student_name`, `runs_scored`. This style is called **snake_case** (the underscores look like a snake hugging the ground). Java folks write `totalPrice` (camelCase); in Python, snake_case is the convention. Follow it and your code looks professional from Day 1.

Also: choose names that **say what they hold**. `runs_scored = 97` is self-explaining. `x = 97` forces the reader to guess.

### Dynamic typing — the dabba doesn't care

In Python, the *value* has a type, not the box. The same dabba can hold sugar today and rice tomorrow:

```python
score = 100        # right now, an integer
score = "hundred"  # now the same name holds a string — Python is fine with this
```

This is called **dynamic typing**: a variable's type can change while the program runs. Convenient, but be careful — freedom means Python won't stop you from accidentally replacing a number with text.

---

## 4. The 4 basic types you meet today

| Type | Full name | What it holds | Example |
|---|---|---|---|
| `int` | integer | Whole numbers, positive or negative, no decimal point | `7`, `-42`, `2024` |
| `float` | floating-point | Numbers **with** a decimal point | `3.14`, `-0.5`, `99.0` |
| `str` | string | Text, inside quotes (single `'` or double `"` — both fine) | `"chai"`, `'Mumbai'` |
| `bool` | boolean | Only two values: `True` or `False` (capital T, capital F) | `is_raining = False` |

A "string" is just programmer-speak for **text** — a *string* of characters tied together like beads. Note that `"5"` (in quotes) is a string, and `5` (no quotes) is an int. They look alike but behave completely differently — this trips up every beginner, and we'll hit it again in the input() section.

---

## 5. Multiple assignment + the famous swap

Python lets you fill several dabbas in one line:

```python
a, b, c = 1, 2, 3        # three names, three values, in order
x = y = z = 0            # one value into three names
```

And the party trick — **swapping** two variables:

```python
a, b = 10, 20
a, b = b, a              # now a is 20, b is 10
```

In most languages you need a third "temporary" variable to swap (like needing an empty glass to exchange chai between two cups). Python evaluates the right side *first* (`b, a` → `20, 10`), then assigns. One line, no spills.

---

## 6. print() — how your program speaks

`print()` displays things on the screen. A **function** is a named, ready-made action — you "call" it by writing its name with brackets, and put inputs inside the brackets.

```python
print("Hello, India!")
print("Runs:", 97)        # commas print multiple things, separated by a space
```

### The two hidden settings: `sep` and `end`

- `sep` (separator) = what goes **between** items. Default: one space.
- `end` = what goes **after** the line. Default: `\n`, a newline (an invisible "press Enter" character).

```python
print("15", "08", "1947", sep="-")   # 15-08-1947  → nice for dates
print("Loading", end="...")          # next print continues on the SAME line
print("done")                        # Loading...done
```

---

## 7. input() — how your program listens (⚠️ big trap inside)

`input()` pauses the program and waits for the user to type something and press Enter. You can pass a prompt message:

```python
name = input("What is your name? ")
```

### The trap: input() ALWAYS returns a string

Even if the user types `25`, you get `"25"` — text, not a number. Always.

```python
age = input("Age? ")      # user types 25
print(age + 5)            # 💥 CRASH — can't add text and number
```

Why does Python do this? Because it cannot know in advance whether the user will type `25`, `25.5`, or `twenty five`. So it hands you raw text and says: *you decide what it is.* Which brings us to...

---

## 8. type() and type casting — checking and converting

`type()` tells you what type a value is:

```python
print(type(25))      # <class 'int'>
print(type("25"))    # <class 'str'>  ← see, quotes change everything
```

**Type casting** = converting a value from one type to another, using `int()`, `float()`, `str()`.

| Conversion | Example | Result | Notes |
|---|---|---|---|
| str → int | `int("42")` | `42` | Works only if the text is a clean whole number |
| str → float | `float("3.14")` | `3.14` | Works for whole numbers too: `float("7")` → `7.0` |
| int → float | `float(5)` | `5.0` | Always safe |
| float → int | `int(7.9)` | `7` | ⚠️ **Chops** the decimal, does NOT round. `int(7.9)` is 7, not 8 |
| int → str | `str(97)` | `"97"` | Always safe — anything can become text |
| float → str | `str(3.5)` | `"3.5"` | Always safe |

### The crash cases — learn these now, thank yourself later

```python
int("3.14")     # 💥 CRASH — int() won't parse a decimal STRING (do float("3.14") first, then int())
int("ten")      # 💥 CRASH — words are not numbers
int("")         # 💥 CRASH — empty text
float("abc")    # 💥 CRASH
```

The standard pattern for numeric input — memorize it, you'll use it daily:

```python
n = int(input("Enter a number: "))    # input gives "25", int() makes it 25
```

---

## 9. f-strings — the smart way to print

Gluing text and variables with `+` and `str()` is ugly. **f-strings** (formatted strings) fix it: put an `f` before the quote, and drop variables inside `{}` (curly braces act like windows into the string):

```python
name, runs = "Rohit", 264
print(f"{name} scored {runs} runs!")     # Rohit scored 264 runs!
```

### Expressions inside {} — not just variables

Any calculation, comparison, or function call works inside the braces:

```python
price = 40
print(f"3 cutting chai = ₹{price * 3}")          # 3 cutting chai = ₹120
print(f"Half-century? {runs >= 50}")             # Half-century? True
```

### `:.2f` — controlling decimals

After a colon `:` inside the braces, you can add a **format modifier**. `.2f` means "show as a float with exactly 2 digits after the point":

```python
bill = 1234.5678
print(f"Total: ₹{bill:.2f}")     # Total: ₹1234.57  (rounded, not chopped)
```

Perfect for money, percentages, and averages. `:.0f` gives no decimals, `:.3f` gives three. (There are more modifiers — commas for thousands, alignment — but `.2f` covers 90% of daily needs.)

---

## 10. Operators — your maths toolkit

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | addition | `7 + 3` | `10` |
| `-` | subtraction | `7 - 3` | `4` |
| `*` | multiplication | `7 * 3` | `21` |
| `/` | division | `7 / 2` | `3.5` ⚠️ **always float**, even `10 / 5` → `2.0` |
| `//` | floor division | `7 // 2` | `3` — divides and **drops** the decimal part |
| `%` | modulo | `7 % 2` | `1` — the **remainder** after division |
| `**` | power | `2 ** 10` | `1024` — 2 raised to 10 |

Note that `/` in Python 3 **always** returns a float. If you want a whole-number answer, use `//`.

### ❤️ A love letter to `%` and `//` — the digit-surgery twins

These two operators are the heart of *every* practice problem today. Understand them once, and reverse/count/palindrome/Armstrong all fall like dominoes.

Take `n = 1947`:

- **`n % 10` → 7** — remainder when dividing by 10 = the **last digit**. Like asking "after packing 1947 laddus into boxes of 10, how many laddus are loose?" Answer: 7.
- **`n // 10` → 194** — division by 10, decimal chopped = the number **with its last digit removed**. "How many full boxes?" 194.

So `% 10` **reads** the last digit, and `// 10` **deletes** it. Do both repeatedly and you eat a number digit by digit, right to left:

```
1947  → last digit 7, remaining 194
194   → last digit 4, remaining 19
19    → last digit 9, remaining 1
1     → last digit 1, remaining 0   ← 0 means: digits over, stop
```

This right-to-left munching loop is THE pattern of Day 1. Every problem below is this pattern wearing a different costume.

---

## 11. Practice problems — hints only, no solutions!

**Attempt each one in `main.py` first.** These notes give you the *idea*, the *approach in words*, a *dry run* (a table where you play computer and track variables by hand — the single best debugging skill you will ever learn), edge cases, and complexity. Never the code.

**Complexity, in plain words:** roughly "how does the work grow when the input grows?" All of today's problems do one small step *per digit*. A number `n` has about `len(str(n))` digits — around log₁₀(n) of them — so we call this **O(number of digits)**, which is tiny. Space is **O(1)**: a fixed handful of variables no matter how big `n` gets. (Formal Big-O comes on Day 5 — today, just feel it.)

---

### Problem 1: Sum of first N numbers

**Idea:** user gives `N`; find `1 + 2 + 3 + ... + N`. For `N = 5`: `1+2+3+4+5 = 15`.

**Approach A (loop):** keep a running total starting at 0 — like a shopkeeper's daily khata where each sale gets added to the day's total. Visit every number from 1 to N and add it in. (You may not have learnt loops yet — that's tomorrow. Try approach B, or peek ahead at `for` if you're curious.)

**Approach B (formula, one line):** young Gauss's trick — pair the first and last numbers: `1+5=6`, `2+4=6`... The sum of 1 to N is always `N * (N + 1) / 2`. For N=5: `5 * 6 / 2 = 15`. ✨

**Dry run (loop way, N = 5):**

| number visited | total before | total after |
|---|---|---|
| 1 | 0 | 1 |
| 2 | 1 | 3 |
| 3 | 3 | 6 |
| 4 | 6 | 10 |
| 5 | 10 | 15 |

**Edge cases:** `N = 1` → 1. `N = 0` → 0 (empty sum). What if the formula's `/` gives `15.0` instead of `15`? Hmm — which *other* division operator fixes that?

**Complexity:** loop = O(N) steps; formula = O(1) — same answer regardless of N. First taste of "a smarter idea beats a faster computer."

**Hints:** 🔸 total must start at 0, *before* any adding begins. 🔸 For the formula, guarantee a whole number with `//`.

---

### Problem 2: Reverse a number

**Idea:** `1234` → `4321`.

**Approach:** the digit-munching loop from Section 10, plus one insight: build the reversed number by *shifting and adding*. Keep `rev = 0`. Each round: `rev = rev * 10 + last_digit`. Multiplying by 10 shifts existing digits left (like adding a zero: 4 → 40), making room for the new digit at the ones place. Then delete the last digit of `n` with `//10`. Stop when `n` hits 0.

**Dry run (n = 1234):**

| round | n | last digit (n % 10) | rev = rev*10 + digit | n after //10 |
|---|---|---|---|---|
| 1 | 1234 | 4 | 0*10+4 = **4** | 123 |
| 2 | 123 | 3 | 4*10+3 = **43** | 12 |
| 3 | 12 | 2 | 43*10+2 = **432** | 1 |
| 4 | 1 | 1 | 432*10+1 = **4321** | 0 → stop |

**Edge cases:** single digit `7` → `7`. Trailing zeros: `1200` → `21` (the leading zeros vanish — `0021` isn't a number). Negative numbers — decide your behaviour (many solutions handle only positives on Day 1; that's okay).

**Complexity:** O(number of digits) time, O(1) space.

**Hints:** 🔸 loop condition: keep going **while n > 0**. 🔸 Don't touch strings/slicing even if you've seen that trick online — the maths version is what interviews and the next 4 problems need.

---

### Problem 3: Count digits of a number

**Idea:** `1947` → `4`.

**Approach:** same munching loop, but even simpler — you don't care *what* the last digit is. Just keep a counter at 0; each time you chop a digit with `//10`, add 1 to the counter. Like counting how many sips finish a glass of chai: sip (chop), count, repeat till empty (n becomes 0).

**Dry run (n = 1947):**

| round | n before | count | n after //10 |
|---|---|---|---|
| 1 | 1947 | 1 | 194 |
| 2 | 194 | 2 | 19 |
| 3 | 19 | 3 | 1 |
| 4 | 1 | 4 | 0 → stop |

**Edge cases:** `n = 0` — how many digits does 0 have? One! But a `while n > 0` loop runs zero times and answers 0. Classic trap — handle 0 specially or note it. `n = 5` → 1.

**Complexity:** O(number of digits) time, O(1) space.

**Hints:** 🔸 you only need `//` here, not `%`. 🔸 Cheeky alternative: `len(str(n))` — string-convert and measure. Works, but do the maths version first; it's the muscle the next two problems use.

---

### Problem 4: Palindrome number

**Idea:** a **palindrome** reads the same forwards and backwards — like the names *Malayalam* or *Anna*. For numbers: `121` yes, `1331` yes, `123` no.

**Approach:** you already built the tool! Reverse the number (Problem 2's exact machinery), then compare: `is reversed == original?` If yes → palindrome. One catch: reversing *destroys* your working copy of `n` (it gets chopped to 0). So **save the original in a separate variable before** you start munching.

**Dry run (n = 121):** save `original = 121`. Reverse: 121 → rev 1, n 12 → rev 12, n 1 → rev 121, n 0. Compare `121 == 121` → True ✅. For `n = 123`: reverse gives `321`, and `321 == 123` → False ❌.

**Edge cases:** single digit → always a palindrome. Negative numbers → usually "no" (`-121` reversed is `121-`... nonsense). Numbers ending in 0 (like `10`) → can never be palindromes (reversed drops to `01` = `1`).

**Complexity:** O(number of digits) time, O(1) space.

**Hints:** 🔸 three variables: the original (untouched), the copy you munch, the reverse you build. 🔸 Compare with `==` (asks "equal?") not `=` (stores!).

---

### Problem 5: Armstrong number

**Idea:** a number is an **Armstrong number** if the sum of each digit raised to the power of (number of digits) equals the number itself. `153` has 3 digits: `1³ + 5³ + 3³ = 1 + 125 + 27 = 153` ✅. `1634` has 4 digits: `1⁴ + 6⁴ + 3⁴ + 4⁴ = 1634` ✅. It's a boss-level combo of everything today.

**Approach:** three phases. (1) Count the digits — Problem 3. (2) Munch through the digits again, but this time raise each digit to that power (`**`) and add into a running sum. (3) Compare the sum with the saved original. You will loop through the number **twice** — once to count, once to sum — so you need the original saved safely, and a *fresh copy* to munch each time.

**Dry run (n = 153, digit count = 3):**

| round | n | digit | digit ** 3 | running sum | n after //10 |
|---|---|---|---|---|---|
| 1 | 153 | 3 | 27 | 27 | 15 |
| 2 | 15 | 5 | 125 | 152 | 1 |
| 3 | 1 | 1 | 1 | 153 | 0 → stop |

`153 == 153` → Armstrong ✅. Try `123`: `1+8+27 = 36 ≠ 123` ❌.

**Edge cases:** every single-digit number (0–9) is an Armstrong number (`7¹ = 7`). `153`, `370`, `371`, `407` are the 3-digit ones — test with these.

**Complexity:** two passes over the digits → still O(number of digits) time, O(1) space.

**Hints:** 🔸 the power is the digit *count*, not always 3 — compute it first, don't hardcode. 🔸 You'll chop `n` to 0 while counting; that's why the fresh copy matters. 🔸 Power in Python is `**`, not `^` (`^` exists but does something totally different — avoid).

---

## 12. Common mistakes (everyone makes these — now you won't)

1. **Forgetting `int()` around `input()`** → then `n + 5` crashes or `"5" * 3` gives `"555"`. Text multiplied is text repeated!
2. **`=` vs `==`** — one stores, the other compares. `if x = 5` is a syntax error.
3. **Case confusion** — creating `Total` then printing `total` → `NameError: name 'total' is not defined`. Python isn't being mean; those are genuinely different names.
4. **Expecting `/` to give an int** — `10 / 2` is `2.0`. Use `//` for whole-number division.
5. **Thinking `int(7.9)` rounds to 8** — it chops to `7`. Chops. Always.
6. **Missing the `f`** — `print("{name}")` prints the literal text `{name}`, braces and all. The `f` prefix is what switches the magic on.
7. **Not saving the original** before munching a number — then there's nothing left to compare against in palindrome/Armstrong.
8. **Starting your sum/counter at the wrong value** (or not at all) — running totals begin at 0, before the loop.

---

## 13. Quick recap

- A **variable** is a labelled dabba: created on first `=`, snake_case names, case-sensitive, can't start with a digit, type can change (dynamic typing).
- Four starter types: `int`, `float`, `str`, `bool`. Quotes make it a string — `"5"` ≠ `5`.
- `a, b = b, a` swaps in one line. `print()` has `sep` and `end`. **`input()` always returns a string.**
- Cast with `int()`, `float()`, `str()`; `int("3.14")` and `int("ten")` crash; `int(7.9)` chops to 7.
- f-strings: `f"{name} scored {runs}"`, expressions allowed inside `{}`, money with `{x:.2f}`.
- `/` always gives float; `//` floors; `%` gives remainder; `**` is power.
- **`n % 10` reads the last digit, `n // 10` deletes it** — the munching loop that solves all five problems today.

## 14. Learn more

- [W3Schools — Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [W3Schools — Python String Formatting (f-strings)](https://www.w3schools.com/python/python_string_formatting.asp)
- [GeeksforGeeks — Input and Output in Python](https://www.geeksforgeeks.org/python/input-and-output-in-python/)

---

## 🌄 Tomorrow (Day 2)

Today your programs ran top-to-bottom like a train on a single track. Tomorrow we teach the computer to **make decisions** ("if the number is even, do this; otherwise, do that") and to **repeat work** without you copy-pasting lines — **conditionals and loops**. That munching loop you dry-ran by hand today? Tomorrow you'll command Python to run it for you. See you at 06:50. 🌅
