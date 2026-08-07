# Day 3 — Functions (Zero to Hero) + Patterns 9–15 + Prime, GCD, LCM

Big day. Functions are the point where code stops being a script and starts being a toolbox. Everything later — recursion, sorting, trees — is built out of functions. So today I go from "what even is a function" all the way to interview-level details.

---

## 1. What is a function?

Think of mom's **chai recipe**. She wrote it once in her head — boil water, add tea leaves, milk, sugar, ginger, strain. Now anyone in the house can "run" that recipe any number of times. Nobody re-invents chai every morning.

A **function** is exactly that: a named block of code, written **once**, used **many times**.

Why bother?

- **No repetition.** Write the logic once, call it 100 times.
- **Naming.** `is_prime(29)` reads like English. The same 6 lines pasted inline do not.
- **Fixing bugs in one place.** If the recipe is wrong, you fix the recipe — not 50 copies of it.

---

## 2. `def` and calling

```python
def make_chai():
    print("Boil water")
    print("Add tea, milk, sugar, ginger")
    print("Chai ready!")

make_chai()   # runs the recipe
make_chai()   # runs it again
```

Two separate moments:

- **`def`** means "define" — I am *writing down* the recipe. Python reads it, remembers it, runs **nothing**.
- **`make_chai()`** — the brackets `()` mean "run it **now**". This is called **calling** the function.

Writing a recipe on paper never made chai. Only cooking does. The number one beginner confusion: defining a function, running the file, and wondering why nothing printed. Answer: it was never called.

Also: the body must be **indented** (shifted right, usually 4 spaces). Indentation is how Python knows which lines belong inside the function.

---

## 3. Parameters vs arguments

The recipe can take inputs: "make chai for `n` cups".

```python
def make_chai(cups):
    print("Making", cups, "cups of chai")

make_chai(2)   # Making 2 cups of chai
make_chai(5)   # Making 5 cups of chai
```

Two words that sound same but are not:

- **Parameter** — the *placeholder name* in the definition. Here: `cups`. It is the empty labelled bowl waiting on the counter.
- **Argument** — the *actual value* you pass while calling. Here: `2` or `5`. It is what you actually put into the bowl.

Parameters live in the `def` line. Arguments live in the call. In interviews people use them interchangeably, but knowing the difference makes error messages ("missing 1 required positional argument") suddenly readable.

Multiple parameters work left to right by position:

```python
def make_chai(cups, sugar_spoons):
    print(cups, "cups,", sugar_spoons, "spoons sugar")

make_chai(2, 3)              # positional: 2 -> cups, 3 -> sugar_spoons
make_chai(sugar_spoons=3, cups=2)   # keyword arguments: order no longer matters
```

`name=value` in a call is a **keyword argument** — you name the bowl yourself, so order stops mattering.

---

## 4. Default parameters

Most days, chai has 2 spoons of sugar. Why say it every time? Set a **default**:

```python
def make_chai(cups, sugar_spoons=2):
    print(cups, "cups,", sugar_spoons, "spoons sugar")

make_chai(3)      # 3 cups, 2 spoons sugar   (default used)
make_chai(3, 1)   # 3 cups, 1 spoons sugar   (default overridden)
```

Rule: parameters **with** defaults must come **after** parameters without defaults. `def f(a=1, b)` is a syntax error — Python cannot tell which argument goes where.

### Advanced note — the mutable default trap (interview favourite)

A **mutable** object is one that can be changed in place, like a list or dictionary. Never use one as a default:

```python
def add_item(item, box=[]):     # DANGER
    box.append(item)
    return box

add_item("roti")    # ['roti']
add_item("sabzi")   # ['roti', 'sabzi']  <- surprise! roti is still there
```

Why? The default `[]` is created **once**, when `def` runs — not fresh on every call. Every call without a `box` argument shares that *same* list, like a "fresh" tiffin box that never got washed — yesterday's roti is still inside.

The standard fix:

```python
def add_item(item, box=None):
    if box is None:
        box = []        # a genuinely new list, every call
    box.append(item)
    return box
```

---

## 5. `*args` — the tiffin box

Sometimes I don't know how many inputs are coming. A **tiffin box** doesn't demand exactly 3 items — you pack whatever mom gives: 2 rotis today, roti-sabzi-achar-sweet tomorrow.

`*args` (star-args) collects **any number of positional arguments** into a **tuple** (a fixed, ordered collection):

```python
def pack_tiffin(*items):
    print("Packed", len(items), "items:", items)

pack_tiffin("roti")                       # Packed 1 items: ('roti',)
pack_tiffin("roti", "sabzi", "achar")     # Packed 3 items: ('roti', 'sabzi', 'achar')
```

The magic is the `*`, not the name — `*items`, `*args`, `*stuff` all work. `args` is just the convention everyone uses.

Real use: Python's own `print("a", "b", "c")` accepts any count of values — that is `*args` at work. You can also loop over it: `for item in items:`.

---

## 6. `**kwargs` — the labelled masala dabba

A **masala dabba** is that round steel box with small labelled bowls — haldi here, jeera there, mirchi in the corner. Every item has a **name**.

`**kwargs` (keyword-args) collects **any number of `name=value` arguments** into a **dictionary** (a name → value store):

```python
def masala_dabba(**spices):
    for name, qty in spices.items():
        print(name, "->", qty)

masala_dabba(haldi="1 tsp", jeera="2 tsp", mirchi="half tsp")
# haldi -> 1 tsp
# jeera -> 2 tsp
# mirchi -> half tsp
```

So:

- `*args` = tiffin box: any number of items, **no labels**, order matters → tuple.
- `**kwargs` = masala dabba: any number of items, **each labelled**, accessed by name → dictionary.

Full parameter order (worth memorising for interviews):

```python
def f(normal, default=1, *args, **kwargs):
```

normal params → defaults → `*args` → `**kwargs`. Any other order errors out.

---

## 7. `return` vs `print` — the most important section today

- **`print`** *shows* a value on the screen. For humans. The value then evaporates.
- **`return`** *hands the value back* to whoever called the function. For code. Now the caller can store it, add to it, pass it on.

Analogy: `print` is the chaiwala **shouting** "chai ready!" across the street — you heard it, but you have no cup in hand. `return` is him **handing you the glass** — now you can drink it, share it, put it down for later.

```python
def add_print(a, b):
    print(a + b)          # only shows

def add_return(a, b):
    return a + b          # hands back
```

### The classic bug

Every function in Python gives back *something*. If there is no `return`, it gives back **`None`** — a special value meaning "nothing here". So:

```python
result = add_print(2, 3)   # screen shows 5 ... but that was print doing its thing
print(result)              # None  <- the function returned nothing!
total = result + 10        # TypeError: unsupported operand ... 'NoneType'
```

It *looked* like it worked because 5 appeared on screen. But `result` holds `None`, and math on `None` crashes. Meanwhile:

```python
result = add_return(2, 3)  # screen shows nothing
total = result + 10        # 15 — the value actually came back
```

Two more things:

- `return` **immediately exits** the function. Lines after it never run. (Useful: return early when the answer is known.)
- Rule of thumb for DSA: functions should **return** answers. Printing is only for the final display step. `lcm` can only reuse `gcd` if `gcd` *returns* its answer.

---

## 8. Local vs global scope

**Scope** = the region of code where a variable exists.

What happens in the kitchen stays in the kitchen. Variables created **inside** a function are **local** — they are born when the function is called and destroyed when it ends. The outside world cannot see them.

```python
def kitchen():
    secret_masala = "kasuri methi"   # local
    print(secret_masala)             # works here

kitchen()
print(secret_masala)   # NameError: name 'secret_masala' is not defined
```

Variables created at the top level of the file are **global** — every function can *read* them:

```python
shop_name = "Sharma Chai Corner"   # global

def board():
    print(shop_name)    # reading global: fine

board()
```

But *assigning* inside a function creates a **new local** variable — it does not touch the global:

```python
count = 0

def sell():
    count = count + 1   # UnboundLocalError!
```

Python sees `count = ...` inside the function and decides "count is local here" — then `count + 1` tries to read a local that doesn't exist yet. To really modify the global, declare it:

```python
def sell():
    global count
    count = count + 1
```

Use `global` rarely. Cleaner style: take the value as a parameter, return the new value.

### LEGB (light touch)

When Python meets a name, it searches in this order:

1. **L**ocal — inside the current function
2. **E**nclosing — inside any function wrapping this one (nested functions)
3. **G**lobal — top level of the file
4. **B**uilt-in — Python's own names (`print`, `len`, `range`)

First match wins. This is also why naming a variable `list` or `print` is a bad idea — it hides the built-in.

---

## Common mistakes

1. **Defining but never calling.** `def` alone runs nothing. Add `make_chai()`.
2. **Using a printed result.** `x = f()` where `f` only prints → `x` is `None` → crash later. Return the value.
3. **Forgetting `return` exits immediately.** Code placed after `return` is dead code.
4. **Mutable default (`def f(x=[])`).** Shared across calls. Use `x=None` and create inside.
5. **Default before non-default.** `def f(a=1, b)` is a syntax error.
6. **Confusing `*args` (tuple, positional) with `**kwargs` (dict, named).**
7. **Assigning to a global inside a function** without `global` → `UnboundLocalError`.
8. **Shadowing built-ins** — naming a variable `sum`, `list`, `max` and then wondering why the built-in stopped working.

---

## Patterns 9–15 (shapes + hints only — I solve them myself)

All shapes shown for `n = 5`. Reminders: `print(x, end="")` stays on the same line; a bare `print()` moves to the next row.

### Pattern 9 — Diamond

```
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
```

**Hint:** a diamond is just the pyramid (Day 2) with the inverted pyramid stacked directly under it — two outer loops, one after the other. Notice the widest row appears twice.

### Pattern 10 — Half diamond / hourglass of stars

```
*
**
***
****
*****
****
***
**
*
```

**Hint:** star counts go 1→n then n−1→1. Either two loops (grow, then shrink), or one loop of about `2n` rows with an `if` deciding which phase you're in.

### Pattern 11 — Binary 0-1 triangle

```
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```

**Hint:** each row's *first* digit depends on whether the row number is even or odd; after that, flip every step — and `1 - num` toggles 1↔0 without any `if`.

### Pattern 12 — Number palindrome pyramid

```
1        1
12      21
123    321
1234  4321
1234554321
```

**Hint:** every row = numbers counting **up** + a middle gap of spaces + the same numbers counting **down**; the gap shrinks by 2 each row so total width stays `2n`.

### Pattern 13 — Increasing-number triangle

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

**Hint:** one counter initialised **before** the outer loop and never reset — like bank token numbers, the next row continues where the last one stopped.

### Pattern 14 — Alphabet triangle

```
A
AB
ABC
ABCD
ABCDE
```

**Hint:** letters are numbers underneath — `chr(65)` is `'A'`, `chr(66)` is `'B'`; reset the code to 65 at the start of **every** row, then count up `i+1` times.

### Pattern 15 — Reverse alphabet triangle

```
ABCDE
ABCD
ABC
AB
A
```

**Hint:** identical to Pattern 14, only the row length shrinks — row `i` prints `n - i` letters, still starting from `'A'` each row.

---

## Prime check — approach only

A **prime** is a number with exactly two divisors: 1 and itself. So 2, 3, 5, 7, 11... Note: 0 and 1 are **not** prime — handle `n < 2` first.

### Why checking till √n is enough

Divisors come in **pairs** that multiply to `n`. For 36: (1,36), (2,18), (3,12), (4,9), (6,6). In every pair, one partner is small and one is big — and the small one is always ≤ √36 = 6. If 36 had *any* divisor bigger than 6, its partner would necessarily be smaller than 6, and I'd have already met it. So if no divisor exists up to √n, none exists at all. This turns a 10-crore-step loop (for n = 10⁸) into a 10,000-step loop.

### Pseudocode in words

- If n is less than 2, answer is "not prime".
- Start a checker at 2. While checker × checker is ≤ n:
  - if n divides evenly by checker (remainder 0), return "not prime" immediately;
  - otherwise move checker up by 1.
- If the loop finishes with no divisor found, return "prime".

Tip: write `i * i <= n` instead of computing an actual square root — avoids decimal rounding issues. Test with 1 (no), 2 (yes), 9 (no — catches a wrong boundary), 25 (no), 29 (yes).

---

## GCD by Euclid — approach only

**GCD** (Greatest Common Divisor / HCF) of two numbers = the largest number dividing both. GCD(48, 18) = 6.

### The idea, with a change-making feel

Like breaking a big amount into smaller and smaller notes: keep replacing the pair with a smaller equivalent pair until one side hits zero. Euclid's identity:

> gcd(a, b) = gcd(b, a mod b)

(`a mod b` = remainder when a is divided by b, written `a % b`.) Why it works: any number that divides both `a` and `b` also divides the remainder `a - q·b` — so the set of common divisors never changes while the numbers shrink fast. When the second number becomes 0, the first **is** the answer, because gcd(x, 0) = x.

### Trace: gcd(48, 18)

| step | a  | b  | a % b |
|------|----|----|-------|
| 1    | 48 | 18 | 12    |
| 2    | 18 | 12 | 6     |
| 3    | 12 | 6  | 0     |
| 4    | 6  | 0  | —  → **answer 6** |

### Pseudocode in words

- While b is not zero: replace the pair (a, b) with (b, a % b) — in Python one swap line does both at once.
- When b is zero, return a.

Nice bonus: if the smaller number comes first, e.g. (18, 48), the very first step swaps them automatically — 18 % 48 is 18. No special case needed.

---

## LCM — approach only

**LCM** (Least Common Multiple) = the smallest number that both a and b divide into. LCM(4, 6) = 12.

No loop needed. Use the identity:

> a × b = gcd(a, b) × lcm(a, b)

So: **lcm = (a × b) ÷ gcd(a, b)**.

### Pseudocode in words

- Compute g = gcd(a, b) by *calling the gcd function I just wrote* — this only works because gcd **returns** its answer instead of printing it. Today's whole lesson in one line.
- Return (a × b) divided by g, using integer division (`//`) so the result stays a whole number.
- Slightly safer order for big numbers: divide first, multiply after — (a // g) × b.

Test: (4, 6) → 12; (7, 5) → 35 (co-prime, gcd = 1, so lcm = product).

---

## Quick recap

- Function = recipe written once, called many times. `def` writes it; `name()` runs it.
- **Parameter** = placeholder in `def`; **argument** = actual value in the call.
- Defaults fill in missing arguments; never use a mutable (list/dict) as a default.
- `*args` = tiffin box → tuple of unnamed extras. `**kwargs` = masala dabba → dict of named extras. Order: normal, defaults, `*args`, `**kwargs`.
- `return` hands the value back (usable); `print` only displays it and the function returns `None`. Storing a printed "result" is the classic bug.
- Locals live and die inside the function; globals are readable everywhere but need `global` to be reassigned. Lookup order: LEGB.
- Diamond = pyramid + inverted pyramid. One never-resetting counter → increasing triangle. `chr(65)` = `'A'` unlocks alphabet patterns.
- Prime: divisors pair up, so checking up to √n suffices. GCD: keep taking remainders till zero. LCM = (a×b) ÷ gcd — possible only because gcd *returns*.
