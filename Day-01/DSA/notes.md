# Day 1 — Setup + Python Basics + First 5 Number Problems

Goal for today: get the machine ready, learn the absolute basics of Python, and understand the digit-play pattern that powers the first five practice problems. Zero to hero — no step skipped.

---

## 1. Setup checklist

- **VS Code** — the code editor. Install it, then add the official *Python* extension (it gives colours, error squiggles, and a Run button).
- **Python 3.12** — the language itself. After installing, check in the terminal: `python --version` should print `3.12.x`.
- **LeetCode account** — the site where interview problems live. Free account is enough.
- **GFG (GeeksforGeeks) account** — great for topic-wise practice and articles in simple language.
- Keep one folder per day (`Day-01`, `Day-02`, ...) with a `main.py` for solutions and these notes beside it.

---

## 2. Variables — labelled dabbas

A **variable** is a name that points to a value. Think of steel dabbas (tiffin boxes) in the kitchen with labels: the dabba labelled `sugar` holds sugar today; tomorrow you can put tea powder in it. The label stays, the content can change.

```python
runs = 74          # an integer (whole number)
price = 10.5      # a float (number with a decimal point)
name = "Rohit"    # a string (text, inside quotes)
is_out = False     # a boolean (only True or False)
```

Rules worth remembering:

- No need to declare a type. Python figures it out from the value. This is called **dynamic typing**.
- Names are case-sensitive: `Runs` and `runs` are two different dabbas.
- Names can't start with a digit: `1st_innings` is a SyntaxError; `innings_1` is fine. Letters, digits and underscores only — no spaces, no hyphens.
- Use snake_case: `total_price`, not `TotalPrice`.
- `type(x)` tells you what kind of value `x` holds.

```python
print(type(runs))   # <class 'int'>
print(type(price))  # <class 'float'>
```

### Multiple assignment — and the famous swap

Python can fill many dabbas in one line:

```python
a, b = 1, 2                       # a gets 1, b gets 2
runs, balls, fours = 82, 53, 9    # three at once
```

And swapping two variables needs no third dabba:

```python
a, b = b, a    # done! Python computes the whole right side first, then assigns
```

In most languages a swap needs a temporary variable — like needing an empty plate to exchange two ladoos between two plates. Python just exchanges them mid-air. Interviewers love that you know this one-liner.

---

## 3. print() and input()

**`print()`** shows things on the screen.

```python
print("Chai ready")
print("Score:", 74)     # comma adds a space automatically
```

`print()` also has two useful dials — `sep=` and `end=`:

```python
print("roti", "sabzi", "dal")             # roti sabzi dal   — default separator is a space
print("roti", "sabzi", "dal", sep=", ")   # roti, sabzi, dal — sep= changes the separator
print("Loading", end="")                  # end= replaces the newline at the end
print("...done")                          # → Loading...done  (same line!)
```

By default every `print()` ends by jumping to a new line. `end=""` stops that jump, so the next print continues on the same line.

**`input()`** asks the user to type something and waits.

```python
name = input("Enter your name: ")
```

### The #1 beginner trap: input() ALWAYS returns a string

Even if the user types `25`, Python receives it as the **text** `"25"`, not the number 25. Text and numbers behave very differently:

```python
age = input("Age: ")     # user types 25
print(age + 5)           # CRASH! Can't add text and a number
print(age + "5")         # "255" — string joining, not maths!
```

To do maths, convert first (next section).

---

## 4. Type casting — changing the container

**Type casting** means converting a value from one type to another. Like pouring chai from a kulhad into a steel glass — same chai, different container.

```python
int("25")      # 25       string → integer
float("10.5")  # 10.5     string → float
float(7)       # 7.0      int → float (always safe, nothing lost)
str(74)        # "74"     number → string
int(10.9)      # 10       float → int CHOPS the decimal, no rounding!
int("10.5")    # CRASH — "10.5" is not a whole-number string
int("abc")     # CRASH — letters can never become a number
```

If you really need `"10.5"` as a whole number, go in two steps: `int(float("10.5"))` → 10.

The standard pattern for reading a number:

```python
n = int(input("Enter a number: "))
```

Read inside-out: `input()` gives a string, `int()` converts it, `n` stores the result.

---

## 5. f-strings — filling blanks in a sentence

An **f-string** is a string with an `f` before the quote. Anything inside `{ }` gets replaced by its value. Like a wedding card template: "Shri ____ weds ____" with the blanks filled in.

```python
name = "Virat"
runs = 82
print(f"{name} scored {runs} runs")        # Virat scored 82 runs
print(f"Next year he'll want {runs + 18}") # expressions work inside {}
price = 33.333333
print(f"Chai split: Rs {price:.2f} each")  # Rs 33.33 — .2f = 2 decimal places
```

Forget the `f` and Python prints the braces literally: `{name} scored {runs} runs`. Classic mistake.

---

## 6. The two heroes of digit problems: % and //

Every one of today's problems plays with the digits of a number. Two operators do all the work. Learn these two and Day 1 is 80% done.

### % (modulo) — the remainder

`a % b` gives the **remainder** when `a` is divided by `b`.

Think of an auto ride costing Rs 47, paid with tens: 4 notes of Rs 10 go in, and Rs 7 is left over. That leftover is the modulo: `47 % 10 = 7`.

The magic case is `% 10`:

```python
453 % 10   # 3  — the LAST digit
88 % 10    # 8
7 % 10     # 7  (7 divided by 10: quotient 0, remainder 7)
```

**`num % 10` peels off the last digit** — like taking the bottom coin off a stack of coins, one at a time.

### // (floor division) — divide and drop the decimals

`a // b` divides and **throws away everything after the decimal point** (rounds down).

```python
47 / 10    # 4.7   normal division, gives a float
47 // 10   # 4     floor division, gives an int
453 // 10  # 45  — the number WITHOUT its last digit
7 // 10    # 0   — number smaller than 10 becomes 0
```

**`num // 10` chops off the last digit.**

### The universal digit loop

Combine them and you can visit every digit of any number:

```python
# skeleton — visits digits from LAST to FIRST
while num > 0:
    digit = num % 10   # look at the last digit
    # ... do something with digit ...
    num //= 10         # chop it off (same as num = num // 10)
```

Dry run with 453: see digit 3 (num becomes 45) → see digit 5 (num becomes 4) → see digit 4 (num becomes 0) → loop stops. Three digits, three rounds. This one loop, with different "do something" lines, solves problems 2–5 below.

One more friend: `**` means "to the power of". `5 ** 3` is 125.

### All the maths operators in one place

| Operator | Meaning | Example |
|---|---|---|
| `+` `-` `*` | add, subtract, multiply | `7 * 6` → 42 |
| `/` | division — **always gives a float** | `10 / 2` → `5.0`, not 5 |
| `//` | floor division — drops the decimals | `10 // 3` → 3 |
| `%` | remainder | `10 % 3` → 1 |
| `**` | power | `2 ** 10` → 1024 |

The one that surprises everyone: `/` gives a float even when the division is exact. `10 / 2` is `5.0`, not `5`. If you want an int, that's `//`'s job.

---

## 7. Practice problems — idea, approach, hints (NO solutions)

Solve each of these yourself in `main.py`. Notes below give the thinking, not the code.

Quick word on complexity before we start:

- **Time complexity** = how much work grows as input grows. **O(n)** means work grows in step with n. **O(1)** means fixed work no matter the input.
- A number `n` has roughly **log₁₀(n)** digits (1000 has 4 digits, not 1000 digits). So a loop that runs once per digit is **O(log n)** — very fast.
- **Space complexity** = extra memory used. A handful of variables = **O(1)**.

### Problem 1 — Sum of first N numbers

**What it asks:** given n, find 1 + 2 + 3 + ... + n. For n = 10, answer is 55.

**Key idea:** keep a running total, like a cricket scoreboard adding runs ball by ball.

**Approach in words:**
1. Start a total at 0.
2. Loop i from 1 to n (careful: `range(1, n+1)` — range stops one *before* the end).
3. Add i into the total each round.
4. Return the total.

**Dry run, n = 3:** total goes 0 → 1 → 3 → 6. Answer 6.

**Edge cases:** n = 0 should give 0. n = 1 should give 1.

**Complexity:** O(n) time, O(1) space.

**Interview bonus:** there is a famous formula that gives the same answer with zero looping — O(1) time. Gauss found it as a schoolboy. Look up "sum of first n natural numbers formula" *after* your loop version works, and code that too.

### Problem 2 — Reverse a number

**What it asks:** 453 → 354. 1200 → 21 (yes, leading zeros vanish — 0021 is just 21).

**Key idea:** peel the last digit off the old number, push it onto the *back* of a new number. The push trick: `new = new * 10 + digit`. Multiplying by 10 shifts existing digits left one place, making room in the ones place — like adding a zero to a price tag.

**Approach in words:**
1. Start a new number at 0.
2. While the old number > 0: peel the last digit with `% 10`, push it with `new * 10 + digit`, chop with `// 10`.
3. Return the new number.

**Dry run, 453 → 354:**

| old number | digit peeled | new number after push |
|---|---|---|
| 453 | 3 | 0×10 + 3 = 3 |
| 45 | 5 | 3×10 + 5 = 35 |
| 4 | 4 | 35×10 + 4 = 354 |
| 0 | — | loop stops |

**Edge cases:** single digit (returns itself), trailing zeros (120 → 21), 0 itself. Think: what would you do for a negative number if asked?

**Complexity:** O(log n) time — one round per digit. O(1) space.

### Problem 3 — Count digits

**What it asks:** how many digits in a number? 1082945 → 7.

**Key idea:** keep chopping the last digit and count the chops. Like counting how many rotis are in a stack by removing one at a time.

**Approach in words:**
1. Counter starts at 0.
2. While number > 0: add 1 to the counter, chop with `// 10`.
3. Return the counter.

Notice: you never even need the digit's *value* here — only the number of chops. No `% 10` required.

**Dry run, 305:** 305 → 30 (count 1) → 3 (count 2) → 0 (count 3). Answer 3.

**Edge cases:** the sneaky one is **0**. The loop condition `> 0` never runs, so you'd return 0 — but 0 has 1 digit! Handle it separately if the interviewer asks.

**Complexity:** O(log n) time, O(1) space.

### Problem 4 — Palindrome number

**What it asks:** does the number read the same forwards and backwards? 121 yes, 32523 yes, 453 no. Like the word MADAM, or the station name "Malayalam" written in English.

**Key idea:** reverse the number (Problem 2's exact loop!) and check if reverse equals original.

**Approach in words:**
1. **Save a copy of the original first.** The reversing loop grinds its number down to 0 — if you don't keep a copy, you'll end up comparing the reverse against 0. This is the classic bug of this problem.
2. Reverse the copy using the Problem 2 loop.
3. Return whether reverse equals the saved original. (The comparison `a == b` itself produces `True`/`False` — a **boolean** — so you can return it directly. No if-else needed.)

**Dry run, 121:** reverse builds 1 → 12 → 121. Compare 121 == 121 → True.

**Edge cases:** single digits are always palindromes. 10 is not (reverse is 1). Negative numbers are usually defined as not palindromes (-121 reversed "looks like" 121-).

**Complexity:** O(log n) time, O(1) space.

### Problem 5 — Armstrong number

**What it asks:** a number with d digits is an **Armstrong number** if the sum of each digit raised to the power d equals the number itself. 153 has 3 digits: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153. Match → Armstrong. (Other examples to test: 370, 371, 9474. And 154 should fail.)

**Key idea:** two passes over the digits. Pass 1 = count the digits (Problem 3). Pass 2 = rebuild the power-sum using `digit ** count` and compare with the original.

**Approach in words:**
1. Copy the number, count its digits (Problem 3 loop). Call it `d`.
2. **Re-copy from the original** — pass 1 destroyed your working copy, so refill it.
3. Loop again: peel each digit, add `digit ** d` to a running sum, chop.
4. Return whether the sum equals the original number.

**Dry run, 153 (d = 3):** sum goes 27 (from 3³) → 152 (+5³=125) → 153 (+1³=1). Compare 153 == 153 → True.

**Edge cases:** all single-digit numbers are Armstrong (d=1, so digit¹ = digit). Test 9474 (4 digits, powers of 4).

**Complexity:** two passes over the digits is still O(log n) time, O(1) space.

---

## 8. Common mistakes

1. **Forgetting `int()` around `input()`** — then `n + 1` crashes or `n * 2` doubles the *text* (`"25" * 2` is `"2525"`!).
2. **`range(1, n)` instead of `range(1, n+1)`** — range stops one before the end, so n itself gets skipped.
3. **Not copying the original** before a destroying loop (palindrome, Armstrong) — you end up comparing against 0.
4. **Reusing a dead copy** — in Armstrong, the first loop leaves the copy at 0; refill it before loop two.
5. **Missing the `f`** in an f-string — `{name}` prints literally instead of the value.
6. **Confusing `/` and `//`** — `47 / 10` is `4.7` (float), `47 // 10` is `4` (int). Digit problems always want `//`.
7. **Naming a variable `sum`** — it works, but `sum` is also a built-in Python function; `total` is safer.
8. **Forgetting `num //= 10` inside a while loop** — the number never shrinks, the loop never ends (infinite loop). If your program hangs, check this first.
9. **Ignoring 0 as an input** — `while num > 0` skips entirely for 0; decide what the answer should be.
10. **Starting a variable name with a digit** — `1st_run = 5` is a SyntaxError. Put the digit at the end: `run_1`.
11. **Expecting `/` to give an int** — `10 / 2` is `5.0`. Exact division or not, `/` always hands you a float.

---

## 9. Quick recap

- Variable = labelled dabba; the label stays, contents can change.
- Swap without a third dabba: `a, b = b, a`.
- `print(..., sep=", ")` changes the separator; `end=""` keeps the next print on the same line.
- `input()` ALWAYS gives a string → wrap in `int()` for maths.
- f-string: `f"{name} scored {runs}"` — blanks filled in a template.
- Casting: `int()`, `float()`, `str()`; `int(10.9)` chops to 10, no rounding; `int("abc")` and `int("10.5")` crash.
- `/` always gives a float — even `10 / 2` is `5.0`. Want an int? Use `//`.
- `num % 10` → last digit (bottom coin off the stack). `num // 10` → number minus its last digit.
- Universal digit loop: peel with `%`, chop with `//`, stop at 0. Runs once per digit → O(log n).
- Reverse trick: `new = new * 10 + digit`.
- Palindrome = reverse and compare (save the original first!).
- Armstrong = count digits, then sum of digit^count, then compare.
- Sum 1..n: loop is O(n); a formula exists that is O(1) — find it yourself.
