# Day 3 — Functions in Python + Patterns 9 to 15

Today is about **functions** — the single most important building block in programming. Once functions click, everything after this (recursion, sorting, trees) becomes easier. Then we use them to build patterns 9–15.

---

## 1. What is a function?

Think of your mom's **chai recipe**. She doesn't re-invent chai every morning. The recipe was written once — boil water, add tea leaves, milk, sugar, ginger — and now anyone in the house can "run" it any number of times.

A **function** is exactly that: a named block of code you write once and reuse many times.

```python
def make_chai():
    print("Boil water")
    print("Add tea, milk, sugar")
    print("Chai ready!")

make_chai()   # runs the recipe
make_chai()   # runs it again — no rewriting
```

Two parts:

- **`def`** — "define". You are *writing* the recipe. Nothing runs yet.
- **Call** — `make_chai()`. The brackets `()` mean "run it now".

Writing a recipe on paper does not make chai. Only *calling* it does. Beginners often define a function and wonder why nothing happened — they forgot to call it.

---

## 2. Parameters vs Arguments

Recipes take inputs. "Make chai for **4** people, **less** sugar."

```python
def make_chai(cups, sugar):     # cups, sugar = PARAMETERS
    print(f"Making {cups} cups, sugar: {sugar}")

make_chai(4, "less")            # 4, "less" = ARGUMENTS
```

- **Parameter** — the *name* in the definition. The empty cup waiting to be filled.
- **Argument** — the *actual value* you pass when calling. The chai you pour in.

Interviewers do ask this difference. Easy trick: **P**arameter = **P**laceholder, **A**rgument = **A**ctual value.

You can also pass by name (**keyword arguments**) so order doesn't matter:

```python
make_chai(sugar="less", cups=4)   # works fine
```

---

## 3. Default parameters

Most days you take 2 spoons of sugar. So make that the default — only mention sugar when it's different.

```python
def make_chai(cups, sugar=2):
    print(f"{cups} cups with {sugar} spoons sugar")

make_chai(3)        # 3 cups with 2 spoons sugar (default used)
make_chai(3, 1)     # 3 cups with 1 spoon sugar (default overridden)
```

Rule: **defaults must come after non-defaults**. `def f(sugar=2, cups)` is a syntax error — Python wouldn't know which value goes where.

**Danger zone (interview favourite):** never use a mutable (changeable) default like a list.

```python
def add_item(item, box=[]):    # BAD — same box reused across calls!
    box.append(item)
    return box

add_item("pen")    # ['pen']
add_item("book")   # ['pen', 'book']  <-- surprise! old pen is still there
```

The default list is created **once**, when the function is defined, not fresh on every call. Fix: use `box=None` and create a new list inside.

---

## 4. `*args` — the tiffin box

A **tiffin box** doesn't care what you pack — 2 rotis or 5 rotis, one sabzi or three. It takes *any number of items*.

`*args` lets a function accept any number of positional (unnamed) values. They arrive packed as a **tuple** (a read-only list).

```python
def total_bill(*items):
    print(items)          # a tuple, e.g. (30, 50, 20)
    return sum(items)

total_bill(30, 50)            # 80
total_bill(30, 50, 20, 100)   # 200 — same function, more items
```

The name `args` is just convention. The **`*` is the magic**, not the word. `*prices` works the same.

---

## 5. `**kwargs` — the labelled spice box

A **masala dabba** where every compartment has a label: haldi, jeera, dhania. Not just values — *named* values.

`**kwargs` accepts any number of **keyword** arguments (`name=value`). They arrive packed as a **dictionary** (label → value pairs).

```python
def student_info(**details):
    print(details)   # {'name': 'Rahul', 'city': 'Pune', 'marks': 92}

student_info(name="Rahul", city="Pune", marks=92)
```

Order of everything in one definition (memorise this):

```python
def f(normal, default=1, *args, **kwargs):
    ...
```

Plain parameters → defaults → `*args` (extra unnamed) → `**kwargs` (extra named).

---

## 6. `return` vs `print` — THE most important section today

This confuses everyone at first. Read it twice.

- **`print`** — shows the value on the *screen*. For humans. The function itself hands back nothing (`None`).
- **`return`** — hands the value *back to the caller*, so the program can use it further. For the code.

Analogy: you send your brother to buy milk.

- `print` brother: comes back and **announces** "milk costs 30 rupees!" — but his hands are empty. You can't make chai.
- `return` brother: quietly **hands you the milk packet**. Now you can actually use it.

```python
def add_print(a, b):
    print(a + b)          # shows 7, returns None

def add_return(a, b):
    return a + b          # hands back 7, shows nothing

x = add_print(3, 4)       # screen shows 7, but x is None
y = add_return(3, 4)      # screen shows nothing, y is 7
print(y * 10)             # 70 — we could USE the value
print(x * 10)             # CRASH — None * 10 makes no sense
```

Key facts:

- A function with no `return` (or a bare `return`) gives back `None`.
- `return` immediately **exits** the function. Code after it never runs.
- You can return multiple values: `return a, b` (comes back as a tuple).
- In DSA problems / LeetCode, you almost always **return**. `print` is only for pattern problems and debugging.

---

## 7. Local vs Global scope

**Scope** = the area of the program where a variable is visible.

*What happens in the kitchen stays in the kitchen.* A variable created **inside** a function (local) dies when the function ends. A variable created **outside** (global) is visible everywhere.

```python
city = "Mumbai"            # global — everyone can see it

def trip():
    ticket = 500           # local — exists only inside trip()
    print(city)            # reading a global? Allowed.

trip()
print(ticket)              # NameError — ticket died when trip() ended
```

The tricky part — **assigning** to a global inside a function:

```python
count = 0

def bump():
    count = count + 1      # UnboundLocalError!

```

The moment Python sees `count =` inside the function, it treats `count` as a **new local** — and you're reading it before it exists. If you truly must modify a global, declare it:

```python
def bump():
    global count
    count += 1
```

But in real code (and interviews), avoid `global`. Pass values in as arguments, hand results out with `return`. Clean in, clean out — like a dabbawala: tiffin in, empty dabba out, nothing lost in between.

Lookup order Python follows: **LEGB** — Local → Enclosing (outer function) → Global → Built-in. First match wins.

---

## 8. Patterns 9–15 (Striver) — quick notes

All are in `main.py`, tested with `n = 5`. Full line-by-line dry runs are in `notes.ipynb`.

### Pattern 9 — Diamond
Pattern 7 (pyramid) stacked on top of pattern 8 (inverted pyramid). Two separate loops, one after another.
- Top: `n-i-1` spaces, then `2i+1` stars.
- Bottom: `i` spaces, then `2n-2i-1` stars.
- The widest row (9 stars) appears **twice** — once as top's last row, once as bottom's first.

### Pattern 10 — Half diamond (grow then shrink)
Stars go `1 2 3 4 5 4 3 2 1`. One loop of `2n+1` rows with an `if`:
- Rows `0..n` (going up): print `i` stars.
- Rows above `n` (coming down): print `2n - i` stars.
- Note: row 0 and row 2n print **0 stars** — blank lines. That's fine.

### Pattern 11 — Binary triangle (1-0 alternation)
Each row alternates 1 and 0. The trick is the **starting digit**:
- Even row (`i % 2 == 0`) starts with 1, odd row starts with 0.
- Inside the row, flip with `num = 1 - num` (1 becomes 0, 0 becomes 1 — no `if` needed).

### Pattern 12 — Number crown
Three jobs per row: count up `1..i+1`, print `2*(n-i-1)` spaces (the shrinking gap), count down `i+1..1`. Row 1: `1        1`. Last row: `1234554321` (gap becomes 0).

### Pattern 13 — Counting triangle
One counter `num = 1` declared **before** the row loop, so it never resets. Each row just prints and increments: `1 / 2 3 / 4 5 6 / ...`

### Pattern 14 — Alphabet triangle (A, AB, ABC...)
`chr(65)` is `'A'` (65 is A's ASCII code — the number computers use to store characters). Reset `char = 65` at the start of **every row**, increment inside the row.

### Pattern 15 — Reverse alphabet triangle
Same as 14 but the row length shrinks: `n - i` letters per row. `ABCDE / ABCD / ABC / AB / A`.

---

## 9. Concept prep — Prime, GCD, LCM (to solve next in main.py)

These three are still pending in `main.py`. Understand the *idea* now, write the code yourself. No solutions here — that's the point.

### Prime check — only go till √n

A **prime** number has exactly two divisors: 1 and itself. (Note: 1 is NOT prime.)

Naive way: try dividing `n` by everything from 2 to n-1. Works, but slow — O(n).

The insight: **divisors come in pairs**. If `36 = 4 × 9`, then 4 and 9 are partners. One partner is always ≤ √36 = 6, the other ≥ 6. So if `n` has *any* divisor, it has one at or below √n. No divisor till √n → guaranteed prime. This drops the work from O(n) to O(√n) — for n = 10^12, that's 10^6 checks instead of 10^12.

```
function is_prime(n):
    if n < 2:           return False
    i = 2
    while i * i <= n:          # same as i <= sqrt(n), no import needed
        if n % i == 0: return False
        i = i + 1
    return True
```

(`%` is modulo — the remainder after division. `10 % 3` is `1`.)

### GCD — Euclid's algorithm

**GCD** (Greatest Common Divisor / HCF) = the largest number that divides both. GCD(12, 18) = 6.

Euclid's 2300-year-old idea: **gcd(a, b) = gcd(b, a % b)**. Keep replacing the bigger number with the remainder, until the remainder is 0. The last non-zero number is the answer.

Like making change: you owe ₹48 and only have notes of 18. Give two 18s (36), remainder ₹12. Now settle 18 vs 12 → remainder 6. Now 12 vs 6 → remainder 0. Done — **6** is the answer. Keep breaking the bigger amount by the smaller until nothing is left over.

Trace of gcd(48, 18):

```
(48, 18) -> 48 % 18 = 12 -> (18, 12)
(18, 12) -> 18 % 12 = 6  -> (12, 6)
(12, 6)  -> 12 % 6  = 0  -> (6, 0)   b is 0 -> answer is 6
```

```
function gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

This is O(log(min(a, b))) — blazing fast even for huge numbers. The naive "loop from min(a,b) down and check both" is O(min(a, b)) — mention both in an interview, code Euclid.

### LCM — don't loop, use GCD

**LCM** (Least Common Multiple) = smallest number divisible by both. LCM(4, 6) = 12.

The golden formula: for any a, b —

```
a × b = gcd(a, b) × lcm(a, b)

therefore  lcm(a, b) = (a * b) // gcd(a, b)
```

Check: gcd(4, 6) = 2 → lcm = 24 // 2 = 12. Correct.

Use `//` (integer division) — the result is always a whole number since gcd divides a×b cleanly. Safer order to avoid huge intermediate values: `(a // gcd(a, b)) * b`.

So: write `gcd` once, get `lcm` in one line. Functions reused — today's whole lesson in action.

---

## Common mistakes

1. **Defining but never calling** — `def` alone runs nothing. `make_chai` without `()` is just the recipe's name.
2. **Using `print` when you need `return`** — then trying to use the result: `x = f(); x + 1` crashes because `x` is `None`.
3. **Code after `return`** — it silently never runs.
4. **Mutable default argument** (`def f(x=[])`) — the list is shared across all calls.
5. **Default before non-default** — `def f(a=1, b)` is a `SyntaxError`.
6. **Assigning to a global inside a function** without `global` → `UnboundLocalError`.
7. **Forgetting to reset per-row variables** — in pattern 14, `char = 65` must be *inside* the outer loop; in pattern 13, `num = 1` must be *outside*. Where you initialise decides everything.
8. **Prime check**: forgetting that 1 is not prime, or looping `i <= n` instead of `i * i <= n`.
9. **Euclid**: writing `a % b` when `b` is 0 → `ZeroDivisionError`. The loop must stop *when* `b == 0`.
10. Thinking `args`/`kwargs` are keywords — the `*` and `**` are what matter, the names are convention.

---

## Quick recap

- Function = recipe written once with `def`, run with `name()`.
- Parameter = placeholder in the definition; argument = actual value in the call.
- Defaults fill in missing arguments; keep them after normal parameters; never use mutable defaults.
- `*args` = tiffin box (any number of unnamed values, tuple). `**kwargs` = labelled spice box (any number of name=value, dict).
- `return` hands the value back so code can use it; `print` only shows it and gives `None`. `return` also exits the function.
- Local variables live and die inside the function. Read globals freely; avoid writing to them — pass in, return out. LEGB lookup order.
- Patterns 9–15: diamond = two pyramids; grow-shrink uses one `if i > n` split; binary triangle flips with `num = 1 - num`; `chr(65)` = 'A'.
- Prime: check divisors only till √n. GCD: Euclid — replace with remainder till 0. LCM = `(a*b) // gcd(a,b)`.
