[<< Day 02](../../Day-02/DSA/notes.md) | [🏠 Today's tasks](../task.md) | [Day 04 >>](../../Day-04/DSA/notes.md)

# Day 3 — Functions (Zero to Hero) + Patterns 9–15 + Prime, GCD, LCM

## Yesterday → Today

By the end of Day 2 my code could **decide** (`if`) and **repeat** (loops). That is real power. But look at my files honestly: they are one long script, top to bottom, like a kitchen where every dish is cooked in one giant pot. If I want the same star pattern twice, I copy-paste the loop. If the loop has a bug, I fix it in five places.

Today that ends. Today I learn to pack logic into small **reusable machines** called functions. The loops from Day 2 don't disappear — they move *inside* functions and get a name, a doorbell, and a delivery slot.

---

## 1. What is a function, and why should I care?

Think of mom's **chai recipe**. She figured it out once — boil water, add tea, milk, sugar, ginger, strain. Now anyone in the house can "run" the recipe any number of times. Nobody re-invents chai every morning.

A **function** is exactly that: a named block of code, written **once**, used **many times**. It only runs when somebody *calls* it.

Why functions matter:

- **No repetition.** Write the logic once, call it 100 times.
- **Names that read like English.** `is_prime(29)` tells me instantly what is happening. The same six lines pasted inline do not.
- **Fix bugs in one place.** Wrong recipe? Fix the recipe — not 50 copies of it.
- **Building blocks.** Everything ahead — recursion, sorting, trees — is functions calling functions. Today is the foundation of the next 221 days.

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

Three things to burn into memory:

1. `def` **defines** but does not run. Writing the recipe on paper cooks nothing.
2. The parentheses `()` are the "go" button. `make_chai` (no brackets) just *points at* the function; `make_chai()` *runs* it.
3. Everything indented under `def` is the function's body — same indentation rule as `if` and `for` from Day 1 and 2.

Naming rules are the same as variables: letters, numbers, underscores; can't start with a number; case-sensitive. Convention: `snake_case`, and the name should say what the function *does* — `calculate_bill`, not `cb`.

One small extra: if you want to reserve a name now and write the body later, `pass` is the official placeholder:

```python
def coming_soon():
    pass   # empty body, no error
```

---

## 3. Parameters vs arguments

```python
def greet(name):          # name  -> PARAMETER (the empty box in the definition)
    print("Namaste,", name)

greet("Priya")            # "Priya" -> ARGUMENT (the actual value you pass)
```

Easy memory trick: **P**arameter = **P**laceholder. **A**rgument = **A**ctual value. The parameter is the blank on the form; the argument is what you write in the blank.

A function can take many parameters, separated by commas — and then the call must supply a matching set of arguments.

---

## 4. Positional vs keyword arguments

```python
def chai_order(cups, sugar_spoons):
    print(cups, "cups,", sugar_spoons, "spoons sugar")

chai_order(3, 2)                          # POSITIONAL: matched by order
chai_order(sugar_spoons=2, cups=3)        # KEYWORD: matched by name, order free
```

- **Positional** — Python matches by position: first argument → first parameter. Swap them by mistake and you get 2 cups with 3 spoons of sugar. Python won't complain; your tea will.
- **Keyword** — you name each value. Order stops mattering, and the call becomes self-documenting.

Rule: in one call you can mix them, but **positional ones must come first**. `chai_order(3, sugar_spoons=2)` is fine; `chai_order(cups=3, 2)` is a `SyntaxError`.

---

## 5. Default values — and the famous trap

```python
def chai_order(cups, sugar_spoons=2):     # default: 2 spoons
    print(cups, "cups,", sugar_spoons, "spoons sugar")

chai_order(3)        # uses the default -> 2 spoons
chai_order(3, 1)     # overrides it     -> 1 spoon
```

Like the chaiwala who knows your "usual". Say nothing, you get the usual; say something, you get that instead. Parameters **with** defaults must come after parameters **without** defaults in the `def` line.

### The mutable-default trap (interview favourite)

```python
def add_item(item, box=[]):    # DANGER
    box.append(item)
    return box

print(add_item("roti"))        # ['roti']
print(add_item("sabzi"))       # ['roti', 'sabzi']  <- surprise!
```

Why? The default `[]` is created **once**, at `def` time — not fresh on every call. Every call that relies on the default shares that one list. It's a tiffin box that never gets washed: yesterday's roti is still inside.

The fix everyone uses:

```python
def add_item(item, box=None):
    if box is None:
        box = []               # genuinely new list each call
    box.append(item)
    return box
```

Rule of thumb: never use a list, dict, or set as a default. Use `None` and create it inside.

---

## 6. `*args` and `**kwargs` — "however many you bring"

Sometimes you don't know in advance how many arguments will come.

### `*args` — collects extra positional arguments into a **tuple**

```python
def pack_tiffin(*items):
    print("Packed", len(items), "items:", items)

pack_tiffin("roti")                       # Packed 1 items: ('roti',)
pack_tiffin("roti", "sabzi", "achar")     # Packed 3 items: ('roti', 'sabzi', 'achar')
```

A tiffin box that stretches: bring 1 item or 10, everything gets packed into one tuple called `items`.

### `**kwargs` — collects extra keyword arguments into a **dictionary**

```python
def masala_dabba(**spices):
    for name, qty in spices.items():
        print(name, "->", qty)

masala_dabba(haldi="1 tsp", jeera="2 tsp", mirchi="half tsp")
```

A masala dabba where every compartment carries a **label**. Inside the function, `spices` is a dict: `{'haldi': '1 tsp', ...}`.

The names `args` and `kwargs` are just convention — the magic is in `*` and `**`.

### The full ordering rule in a `def` line

```python
def f(a, b, /, c, d=4, *args, e, f=6, **kwargs):
```

Left to right, always this order:

1. **Positional-only** parameters, ended by a bare `/` (rare; you'll see it in `help()` output of built-ins).
2. **Normal** parameters (positional or keyword), defaults after non-defaults.
3. `*args` — soaks up any extra positional values. Writing a **bare `*`** here instead means "no extras allowed, but everything after me must be passed by keyword".
4. **Keyword-only** parameters — anything after `*args` or the bare `*`. Callers *must* name them: `f(..., e=5)`.
5. `**kwargs` — soaks up any extra keyword values. Always last.

You will mostly write `def f(a, b=1, *args, **kwargs)`. But now nothing in this line can scare you.

```python
def transfer(amount, *, confirm):     # bare *: confirm is keyword-only
    ...

transfer(5000, confirm=True)   # works
transfer(5000, True)           # TypeError — a safety feature, on purpose
```

---

## 7. `return` vs `print` — the most important section today

This confuses every beginner, so slowly:

- `print` **shows** a value on the screen. For human eyes only. The program itself cannot use what was printed.
- `return` **hands the value back** to whoever called the function. The program can store it, add to it, pass it onward.

The dosa-stall picture: `print` is the cook *announcing* "dosa ready!" — you heard it, but your plate is empty. `return` is the cook actually *placing the dosa on your plate*.

```python
def add_print(a, b):
    print(a + b)          # announces 5, hands back nothing

def add_return(a, b):
    return a + b          # hands 5 back

r1 = add_print(2, 3)      # screen shows 5, but...
print(r1)                 # None  <- the function returned nothing
r2 = add_return(2, 3)
print(r2 + 10)            # 15   <- usable value
```

Three facts:

1. A function without `return` (or with a bare `return`) gives back **`None`**. That's where the classic bug `TypeError: unsupported operand ... 'NoneType'` comes from — you tried `r1 + 10` on a `None`.
2. `return` **exits the function instantly**. Lines after it never run. (We'll use this as an early exit in prime checking today.)
3. A function may have **multiple `return` statements** — e.g. one in the `if` branch, one at the end — but only one ever fires per call.

### Returning multiple values — tuple unpacking

```python
def min_max(nums):
    return min(nums), max(nums)     # the comma packs ONE tuple

print(min_max([4, 9, 1, 7]))        # (1, 9)
lo, hi = min_max([4, 9, 1, 7])      # unpacked into two names
```

Secretly it is still one return value — a tuple. The comma on the `return` line packs; the commas on the left of `=` unpack. Counts must match, or `ValueError`.

---

## 8. Docstrings, `help()`, and a one-line look at type hints

A **docstring** is a triple-quoted string as the *first* statement of the body — the label on the pickle jar saying what's inside:

```python
def chai_bill(cups, price_per_cup=10):
    """Return the total bill for the given cups of chai."""
    return cups * price_per_cup

help(chai_bill)     # prints the signature + your docstring
```

`help()` works on your functions exactly like it works on `print` — same mechanism. Write a one-line docstring for every non-trivial function; future-you is the main beneficiary.

**Type hints in one line:** `def chai_bill(cups: int, price: int = 10) -> int:` — optional notes saying what types go in and come out. Python does **not** enforce them; they help humans and editors. Know the syntax, use them when ready.

---

## 9. Scope — who can see which variable

```python
shop_name = "Sharma Chai Corner"    # GLOBAL: whole file can read it

def kitchen():
    secret_masala = "kasuri methi"  # LOCAL: exists only inside kitchen()
    print(shop_name)                # reading a global: allowed

kitchen()
print(secret_masala)                # NameError!
```

- **Local** variable: born inside a function, dies when the function ends. What happens in the kitchen stays in the kitchen.
- **Global** variable: created at file level; every function can *read* it.

But **re-assigning** a global inside a function needs a declaration:

```python
count = 0

def sell():
    global count        # without this: UnboundLocalError
    count = count + 1
```

Without `global`, Python assumes `count = ...` creates a *new local* — and then panics because you read it before assigning.

**LEGB** — the order Python searches for a name:

1. **L**ocal — inside the current function
2. **E**nclosing — the function wrapping this one (nested functions)
3. **G**lobal — file level
4. **B**uilt-in — Python's own names (`print`, `len`, ...)

Like looking for your keys: your pocket → your room → the house → the neighbourhood. First match wins.

For the Enclosing layer there is a cousin of `global` called `nonlocal` — it lets an inner function re-assign a variable of its *outer function*. File it away; it matters when we meet closures and decorators later.

---

## 10. Lambda — the one-line throwaway function

```python
square = lambda x: x * x     # same as: def square(x): return x * x
```

Shape: `lambda inputs: expression`. No name, no `return` keyword — the expression's value *is* the return. Any number of inputs, exactly **one** expression.

Like borrowing a pen just to sign one form — you don't take it home. Lambdas shine when a function needs a tiny rule *passed into* another function:

```python
students = [("Rahul", 82), ("Priya", 95), ("Aman", 74)]
students.sort(key=lambda s: s[1])        # sort by marks, not name
print(list(map(lambda x: x * 2, [1, 2, 3])))   # [2, 4, 6]
```

`filter(lambda x: x % 2 == 0, nums)` is the third classic teammate.

**When NOT to use lambda:** the moment logic needs two steps, an `if/elif` chain, or a name you'll reuse — write a proper `def`. Assigning a lambda to a variable just to reuse it (like `square` above, shown only for teaching) defeats the point; `def` gives better error messages and a docstring slot.

---

# Practice targets — patterns 9–15 (shapes + hints only)

I solve these myself in `main.py`. All shapes use `n = 5`. Day 2 reminders: `print(x, end="")` stays on the line; bare `print()` ends a row. New rule for today: **each pattern becomes a function** taking `n` — the loops from Day 2 now live inside functions.

## Pattern 9 — Diamond

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

**Hint:** Day 2's pyramid + inverted pyramid stacked — two outer loops back to back. The widest row appears twice.

## Pattern 10 — Half diamond

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

**Hint:** star counts climb 1→n then fall n−1→1. Either two loops, or one loop of about 2n rows with an `if` picking the phase.

## Pattern 11 — Binary 0-1 triangle

```
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```

**Hint:** odd-numbered rows start with 1, even-numbered rows with 0. Inside a row, `1 - num` flips 1↔0 with no `if` needed.

## Pattern 12 — Number palindrome pyramid

```
1        1
12      21
123    321
1234  4321
1234554321
```

**Hint:** each row = count up + a shrinking middle gap of spaces + count back down. The gap shrinks by 2 per row, so every row is exactly `2n` characters wide.

## Pattern 13 — Increasing-number triangle

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

**Hint:** one counter created **before** the outer loop and never reset — bank-token style, each row continues where the last stopped.

## Pattern 14 — Alphabet triangle

```
A
AB
ABC
ABCD
ABCDE
```

**Hint:** characters are numbers underneath — `ord('A')` is 65, `chr(65)` is `'A'`. Reset a code to `ord('A')` at the start of each row, print `chr(code)` and step +1; row `i` holds `i + 1` letters.

## Pattern 15 — Reverse alphabet triangle

```
ABCDE
ABCD
ABC
AB
A
```

**Hint:** same machinery as Pattern 14; only the row length changes — row `i` prints `n − i` letters.

---

# Practice targets — prime, GCD, LCM (approach only, no code here)

These are functions that **return** answers — today's lesson applied.

## Prime check — and why √n is enough

A prime has exactly two divisors: 1 and itself. So 0 and 1 are **not** prime — handle `n < 2` first.

The naive way checks every number from 2 to n−1. The smart way rests on one observation: **divisors come in pairs** that multiply back to n. For 36: 2×18, 3×12, 4×9, 6×6. In every pair, the smaller partner is at most √36 = 6. So if n had *any* divisor, one member of its pair sits at or below √n — checking beyond √n re-finds pairs we already saw.

**Approach in words:** if n is below 2, answer no. Otherwise try each candidate i starting from 2, continuing while i×i is still at most n (that *is* the √n check, with no square-root function needed). The moment a candidate divides n with remainder 0, return "not prime" immediately — `return` exits on the spot. If the loop finishes with no divisor found, return "prime".

Test set: 1 (no), 2 (yes), 9 (no — catches a wrong loop boundary), 25 (no — catches missing the i×i = n case), 29 (yes).

## GCD — Euclid's algorithm

GCD of two numbers = the biggest number dividing both. School method: list all divisors of each, pick the largest common one. Works, but slow.

**Euclid's insight (~2300 years old):** `gcd(a, b) == gcd(b, a % b)`. Replacing the bigger number by the remainder doesn't change the gcd — anything dividing both a and b also divides `a % b` — but the numbers shrink *fast* (this is why it runs in about log(min(a, b)) steps).

**Change-making picture:** you owe someone ₹48 and only have some ₹18 notion of "notes". Give two 18s (₹36), a remainder of ₹12 is left. Now settle 18 using 12: one 12, remainder 6. Now settle 12 using 6: exactly two 6s, remainder **0**. The last non-zero remainder — **6** — measures both numbers perfectly. That's the gcd.

**Trace of gcd(48, 18)** — do this by hand before coding:

```
(48, 18) -> 48 % 18 = 12 -> (18, 12)
(18, 12) -> 18 % 12 =  6 -> (12, 6)
(12,  6) -> 12 %  6 =  0 -> (6, 0)
second number is 0 -> answer = 6
```

**Approach in words:** while b is not zero, replace the pair (a, b) with (b, a % b). When b hits zero, a is the gcd. Edge check: start with (18, 48) — the first step swaps them automatically, no special case needed.

## LCM — via GCD, no loop

The smallest number divisible by both. Don't hunt for it with a loop; use the identity:

> a × b = gcd(a, b) × lcm(a, b)

**Approach in words:** lcm = (a × b) divided by gcd(a, b), using integer division. Reuse the gcd function you just wrote — possible *only* because gcd **returns** its answer instead of printing it. Today's whole lesson in one line.

Tests: (4, 6) → 12; (7, 5) → 35 (co-prime numbers: gcd is 1, so lcm is just the product).

---

## Common mistakes I must not make

1. **`return` vs `print` confusion** — storing the "result" of a printing function and getting `None`. If the value is needed later, `return` it.
2. **Forgetting `()`** — `make_chai` does nothing visible; `make_chai()` runs it.
3. **Code after `return`** — unreachable, silently never runs.
4. **Mutable default (`def f(x, box=[])`)** — shared across calls. Default to `None`, create inside.
5. **Positional after keyword** — `f(cups=3, 2)` is a `SyntaxError`; positionals go first.
6. **Assigning to a global without `global`** — gives `UnboundLocalError`, not the change you wanted.
7. **Prime loop stopping at `i * i < n`** instead of `<=` — declares 25 prime. Test with a perfect square.
8. **Multi-line logic crammed into a lambda** — if it doesn't fit one honest expression, it wants a `def`.
9. **Indentation drift** — a line accidentally un-indented falls out of the function body.

## Quick recap

- Function = named, reusable block; `def` defines, `name()` runs.
- Parameter = placeholder in the def; argument = actual value in the call.
- Positional args match by order; keyword args match by name; positionals first.
- Defaults make arguments optional; never default to a mutable — use `None`.
- `*args` → tuple of extra positionals; `**kwargs` → dict of extra keywords; ordering: positional-only `/`, normal, `*args` (or bare `*`), keyword-only, `**kwargs`.
- `print` shows; `return` hands back. No return → `None`. `return` exits instantly. `return a, b` packs a tuple; unpack with `lo, hi = ...`.
- Docstring = first-line label; read it back with `help()`. Type hints are optional notes.
- Scope: local dies with the function; LEGB is the lookup order; `global`/`nonlocal` allow re-assignment upward.
- Lambda = one-expression nameless function; great as `key=`/`map`/`filter` rules, wrong for anything bigger.
- Prime: check divisors only up to √n (divisor pairs). GCD: Euclid, `(a, b) → (b, a % b)`. LCM: `a*b // gcd`.

## Learn more

- Python functions — https://www.w3schools.com/python/python_functions.asp
- Lambda — https://www.w3schools.com/python/python_lambda.asp
- `*args` / `**kwargs` — https://www.geeksforgeeks.org/python/args-kwargs-python/
- Euclidean algorithm — https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended/
- Official tutorial on defining functions — https://docs.python.org/3/tutorial/controlflow.html#defining-functions

---

## Tomorrow

Now that I can *write* real code — decisions, loops, functions — the next question is unavoidable: **is my code fast or slow?** Two solutions can both be "correct" and yet one finishes in a blink while the other takes an hour. Day 4 = **Big-O**: the language for judging code speed before ever running it.

---

[<< Day 02](../../Day-02/DSA/notes.md) | [🏠 Today's tasks](../task.md) | [Day 04 >>](../../Day-04/DSA/notes.md)
