# Day 6 — Python Lists: Zero to Hero

Today is all about lists. Almost every DSA problem I will ever solve uses an array, and in Python the array is (mostly) the list. So this needs to be rock solid.

---

## 1. What is a list?

A list is an ordered collection of items. Think of it as a **train with numbered coaches**.

- Each coach (item) has a number painted on it — that number is the **index**.
- The numbering starts at **0**, not 1. First coach = index 0.
- The coaches stay in order. Coach 2 is always between coach 1 and coach 3.
- A coach can carry anything — a number, a string, even another whole train (a list inside a list).

```python
marks = [45, 67, 89, 23, 90]
# index:   0   1   2   3   4
```

`marks[0]` is 45. `marks[4]` is 90. Length is `len(marks)` → 5, but the **last index is 4** (always `len - 1`). This off-by-one detail causes half of all beginner bugs.

### Ways to create a list

```python
marks = [45, 67, 89]        # literal — the usual way
empty = []                  # empty list, fill later
chars = list("abc")         # list() converts any iterable → ['a', 'b', 'c']
nums  = list(range(5))      # [0, 1, 2, 3, 4]
mixed = [1, "chai", 3.5, [2, 4]]   # mixed types allowed — even a list inside a list
```

Python does not force one type per list like C arrays do. Handy — but in DSA problems I will almost always keep one type per list anyway.

---

## 2. Indexing (including negative indexing)

Positive index: count from the front, starting at 0.

Negative index: count from the back, starting at **-1**. So `-1` is the **last coach**, `-2` is second last, and so on.

```python
marks = [45, 67, 89, 23, 90]
marks[0]    # 45  (first)
marks[-1]   # 90  (last)
marks[-2]   # 23  (second last)
```

Why negative indexing is great: to get the last item I never need `marks[len(marks) - 1]`. Just `marks[-1]`. Clean.

Going past the end (`marks[5]` or `marks[-6]`) crashes with an `IndexError`. Python does not silently give garbage — it complains loudly. Good.

---

## 3. Slicing — `list[start:stop:step]`

Slicing means cutting out a portion of the train and getting a **new smaller train** (a new list).

```python
a = [10, 20, 30, 40, 50, 60]
a[1:4]     # [20, 30, 40]
```

**The golden rule: `stop` is EXCLUDED.** `a[1:4]` gives indexes 1, 2, 3 — it stops *before* 4. Like a Mumbai local announcement "this train goes UP TO Dadar" — you get down before Dadar, Dadar itself is not included.

Handy defaults — leave a part empty and Python fills it in:

```python
a[:3]      # [10, 20, 30]        start defaults to 0
a[2:]      # [30, 40, 50, 60]    stop defaults to "till the end"
a[:]       # full copy of the list (important later!)
```

The third number is **step** — how many coaches to jump each time:

```python
a[::2]     # [10, 30, 50]   every 2nd item
a[1::2]    # [20, 40, 60]   every 2nd item, starting from index 1
a[::-1]    # [60, 50, 40, 30, 20, 10]   the whole list REVERSED
```

`a[::-1]` is the famous one-line reverse trick. Note: it makes a **new reversed list**; the original `a` is untouched. (Today's problem 1 asks for *in-place* reverse, so this trick is banned there — but good to know.)

Slicing never crashes on out-of-range values: `a[2:100]` just gives whatever exists. Slices are forgiving; single indexes are strict.

---

## 4. Mutation — lists can change in place

**Mutable** = can be changed after creation. Lists are mutable. Strings are NOT.

```python
a = [1, 2, 3]
a[0] = 99        # works. a is now [99, 2, 3]

s = "abc"
s[0] = "z"       # TypeError! strings cannot be edited in place
```

Useful mutation tools:

```python
a.append(4)      # add at the end
a.insert(1, 7)   # squeeze 7 in at index 1
a.pop()          # remove and return last item
a.pop(0)         # remove and return first item (slow — everyone shifts)
a.remove(7)      # remove first occurrence of the VALUE 7
a[1], a[2] = a[2], a[1]   # swap two items — no temp variable needed!
```

That last swap line is pure gold for today's reverse problem.

---

## 5. More methods — and what each one costs

`append`, `insert`, `pop`, `remove` are above. These complete the toolbox.

### `extend` vs `append(list)` — the classic mix-up

```python
a = [3, 1, 2]
a.extend([4, 5])    # a is [3, 1, 2, 4, 5] — items poured in one by one
a.append([4, 5])    # a is [3, 1, 2, 4, 5, [4, 5]] — the WHOLE list as ONE item!
```

Two bags of laddoos: `extend` = pour one bag into the other. `append` = drop the entire bag in, bag and all. If the length grew by exactly 1 when I expected more — I appended when I meant to extend.

### `sort()` vs `sorted()` — in place vs photocopy

```python
a = [3, 1, 2]
a.sort()           # sorts a IN PLACE, returns None
b = sorted(a)      # returns a NEW sorted list, a untouched
```

`a.sort()` changes `a` itself and returns `None`. So `a = a.sort()` is a classic disaster — it throws away the list and stores `None`. `sorted(a)` is the safe photocopy version. Both accept `reverse=True` for descending.

Same pattern for reversing: `a.reverse()` flips in place (returns `None`); `a[::-1]` gives a reversed copy and leaves `a` alone.

### `index()` and `count()`

```python
a = [10, 20, 10, 30]
a.index(20)    # 1 — index of the FIRST match; ValueError if not found
a.count(10)    # 2 — how many times 10 appears
```

### Cost cheat-sheet (why DSA cares)

| Operation | Cost | Why |
|---|---|---|
| `a.append(x)` / `a.pop()` | O(1) | work at the end — nobody shifts |
| `a.insert(0, x)` / `a.pop(0)` | O(n) | everyone behind shifts one seat |
| `a.remove(x)` / `a.index(x)` / `x in a` | O(n) | must walk and search |
| `a.sort()` / `sorted(a)` | O(n log n) | full sorting work |

Rule of thumb: the **back of the list is the cheap end**. Anything at the front makes the whole train shuffle.

---

## 6. `in`, `not in`, `+` and `*`

Membership check reads like plain English:

```python
menu = ["idli", "dosa", "poha"]
"dosa" in menu        # True
"pizza" not in menu   # True
```

Note: `in` walks the whole list to check — O(n). Fine for small lists; for lakhs of lookups a set is the right tool (coming later in the plan).

`+` joins two lists into a NEW list. `*` repeats:

```python
[1, 2] + [3, 4]   # [1, 2, 3, 4]  — new list, originals untouched
[0] * 5           # [0, 0, 0, 0, 0]  — quick way to pre-fill
```

Trap for later: `[[0]] * 3` repeats the SAME inner list three times (aliasing again — see the big section below). For independent rows, use a comprehension.

---

## 7. Looping over a list — three ways

```python
prices = [40, 60, 25]

# Way 1: just the items (use this by default)
for p in prices:
    print(p)

# Way 2: by index (only when I need to WRITE into the list)
for i in range(len(prices)):
    prices[i] = prices[i] + 5

# Way 3: enumerate — index AND item together
for i, p in enumerate(prices):
    print(i, p)
```

**Why `enumerate` beats `range(len())`:** no `prices[i]` typing everywhere, no off-by-one risk, and it says what I mean — "give me position and value". Keep `range(len())` only for writing into the list by index (like today's rotate problem).

One-line bonus — `zip` walks two lists side by side:

```python
names, scores = ["Asha", "Ravi"], [91, 78]
for name, score in zip(names, scores):
    print(name, score)    # Asha 91, then Ravi 78
```

---

## 8. Free helpers: `min`, `max`, `sum`

```python
marks = [45, 67, 89, 23, 90]
min(marks)                 # 23
max(marks)                 # 90
sum(marks)                 # 314
sum(marks) / len(marks)    # average
```

All three walk the list once — O(n). On an empty list, `min`/`max` raise `ValueError`; `sum([])` is just 0.

Today's problem 2 asks me to build min/max **by hand** — the built-ins exist, but interviews want to see the loop.

---

## 9. THE BIG ONE — Aliasing vs Copy vs Deepcopy

This topic is where interviewers catch people. Slow down here.

### 5a. Aliasing: `b = a` is NOT a copy

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)   # [1, 2, 3, 4]  — a changed too!
```

Wait, why did `a` change? Because `b = a` does **not** create a new list. It just gives the **same list a second name**.

Analogy: one tiffin box at home. Mummy calls it "the steel dabba", I call it "my lunch box". Two names, **one box**. If I put a laddoo in "my lunch box", the laddoo is obviously also inside "the steel dabba" — it is the same box. That is aliasing.

Check with `id()` (the memory address of an object):

```python
id(a) == id(b)   # True — same object
a is b           # True — 'is' asks "same object?", '==' asks "same values?"
```

### 5b. Shallow copy: `a.copy()` or `a[:]`

```python
a = [1, 2, 3]
b = a.copy()     # or b = a[:]  or b = list(a)
b.append(4)
print(a)   # [1, 2, 3]  — safe! a untouched
```

Now there really are two boxes. Changing one does not touch the other. **For flat lists (no lists inside), this is all I need.**

But there is a trap. "Shallow" means: it copies the outer box only. If the list contains **inner lists**, the inner ones are still **shared**.

```python
a = [[1, 2], [3, 4]]
b = a.copy()          # new outer box, SAME inner boxes
b[0].append(99)
print(a)   # [[1, 2, 99], [3, 4]]  — surprise! a's inner list changed
```

Analogy: a big tiffin carrier with small dabbas inside. Shallow copy buys a **new outer carrier** but places the **same old small dabbas** inside it. Open a small dabba from either carrier — it is the same dabba.

(Note: `b[0] = [7, 8]` would NOT affect `a` — replacing a whole inner dabba in the new carrier is fine. The trap is only when you *modify the inside* of a shared inner dabba.)

### 5c. Deep copy: `copy.deepcopy(a)`

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
print(a)   # [[1, 2], [3, 4]]  — fully safe
```

Deep copy = new outer carrier AND brand-new duplicate small dabbas inside, all the way down. Completely independent. Costs more time and memory, so use it only when the list is nested and I truly need independence.

### One-line summary

| Code | What you get | Nested lists safe? |
|---|---|---|
| `b = a` | Same object, second name | No — nothing is safe |
| `b = a.copy()` / `a[:]` | New outer list, shared inner objects | No |
| `b = copy.deepcopy(a)` | Fully independent clone | Yes |

---

## 10. List comprehensions — the one-line list builder

The old way to build a list of squares:

```python
squares = []
for x in range(5):
    squares.append(x * x)
```

The comprehension way — same thing, one line:

```python
squares = [x * x for x in range(5)]   # [0, 1, 4, 9, 16]
```

Read it left to right as English: "give me `x*x` **for** every `x` **in** range(5)."

Add an `if` at the end to filter:

```python
evens = [x for x in range(10) if x % 2 == 0]        # [0, 2, 4, 6, 8]
words = ["chai", "vada pav", "dosa"]
caps  = [w.upper() for w in words if len(w) > 4]     # ['VADA PAV']
```

Pattern to remember: `[expression for item in iterable if condition]`.

### `if` at the end vs `if-else` at the front — two different jobs

```python
# if at the END = filter (some items get dropped)
passed = [m for m in [30, 80, 50] if m >= 35]              # [80, 50]

# if-else at the FRONT = transform (ALL items kept, in one of two forms)
result = ["pass" if m >= 35 else "fail" for m in [30, 80, 50]]
# ['fail', 'pass', 'pass']
```

The end-`if` decides *whether* an item enters the list. The front `if-else` decides *what form* it enters in — every item still enters.

### Advanced: nested comprehension (one example is enough)

```python
pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')] — the LEFT loop is the outer loop
```

### When NOT to use a comprehension

Use it whenever the loop's only job is "build a list". If the loop does printing, counting, or complex logic — keep the normal loop. And the moment a comprehension needs a second read to understand (nested loops AND conditions AND function calls), a plain loop with a good variable name wins. Clever is not the goal; clear is.

---

## 11. Bonus (advanced) — unpacking with `*`

```python
a, b = [10, 20]                 # a=10, b=20
first, *rest = [1, 2, 3, 4]     # first=1, rest=[2, 3, 4]
*rest, last = [1, 2, 3, 4]      # rest=[1, 2, 3], last=4
```

The starred name soaks up "everything left over" as a list. Handy for head-and-tail style problems. Not needed today — just know it exists.

---

## 12. Today's problems — approach and hints only

Solutions go in `main.py`. Notes only carry the thinking.

### Problem 1: Reverse an array IN PLACE

**In place** = modify the same list, no new list allowed. So `a[::-1]` and `reversed()` are cheating here.

**Idea — two pointers.** Imagine two friends in a train: one enters from the front coach, one from the last coach. They walk toward each other, and at every step they **exchange seats**, then move one step inward. When they meet (or cross), the whole train is reversed.

Hints:
- `left = 0`, `right = len(a) - 1`
- Loop while `left < right`
- Swap with `a[left], a[right] = a[right], a[left]`
- Move both pointers inward
- Time O(n), extra space O(1) — that O(1) is the whole point of "in place"

### Problem 2: Find min and max

**Idea — single pass, carry the best-so-far.** Like watching a full cricket innings and remembering the highest and lowest over score as it happens — no need to replay the match.

Hints:
- Start `mn = mx = a[0]` (NOT 0! If all numbers are negative, starting `mx = 0` gives a wrong answer)
- Walk through once; update `mn` if smaller found, `mx` if bigger found
- One loop, O(n). Don't sort — sorting is O(n log n) for a question that needs only one pass
- Think first: what should happen if the list is empty?

### Problem 3: Second largest WITHOUT sorting

**Idea — carry TWO best-so-fars:** `largest` and `second`. One pass.

Hints:
- For each number `x`: if `x > largest`, then the old largest gets demoted — `second = largest` FIRST, then `largest = x`. **The update order matters** — do it backwards and you lose the old champion.
- Else if `x > second` (and `x != largest`), update `second`
- **Duplicate gotcha:** in `[10, 10, 5]`, what is the second largest? If duplicates should not count, the check `x != largest` matters. Decide the rule before coding, test with `[10, 10, 5]` and `[5, 10, 10]`
- Initialize `largest`/`second` carefully (e.g. `float('-inf')`), and handle "no second largest exists" (like `[7]` or `[7, 7]`)

### Problem 4: Left rotate by one

`[1, 2, 3, 4, 5]` → `[2, 3, 4, 5, 1]`. Everyone shifts one step left; the first element goes to the back.

**Idea:** save the first passenger, shift everyone else one seat forward, seat the saved passenger at the end.

Hints:
- `first = a[0]`
- Loop `i` from 1 to end: `a[i - 1] = a[i]`
- Finally `a[-1] = first`
- Do NOT try to shift without saving `a[0]` first — it gets overwritten and lost
- One-liner `a.append(a.pop(0))` exists, but write the manual shift version — interviews want the mechanics

---

## Common mistakes

1. **Thinking `b = a` copies the list.** It only adds a second name. Use `a.copy()` for flat lists, `copy.deepcopy(a)` for nested ones.
2. **Forgetting `stop` is excluded in slices.** `a[0:3]` gives 3 items (indexes 0, 1, 2), not 4.
3. **`a[len(a)]` crashes.** Last valid index is `len(a) - 1`, or just use `a[-1]`.
4. **Trying to mutate a string like a list.** `s[0] = "x"` is a `TypeError`. Strings are immutable.
5. **Shallow-copying a nested list and getting "spooky" changes.** The inner lists are still shared.
6. **Wrong update order in second-largest.** Setting `largest = x` before `second = largest` destroys the old value.
7. **Initializing min/max with 0 instead of `a[0]`.** Breaks on all-negative or all-large inputs.
8. **Modifying a list while looping over it** (removing items mid-loop). Items get skipped. Loop over a copy, or build a new list.
9. **Using `a[::-1]` when the problem says "in place".** That creates a new list — different thing.
10. **`a = a.sort()` stores `None`.** `sort()` works in place and returns nothing. Either `a.sort()` alone, or `b = sorted(a)`.
11. **`append`-ing a list when you meant `extend`.** `a.append([4, 5])` adds ONE item (the whole list); `a.extend([4, 5])` adds two.
12. **`[[0]] * 3` for a grid.** All three rows are the SAME inner list — change one, all three change.

## Quick recap

- List = train with numbered coaches; index starts at 0, `-1` is the last coach.
- Create: literal `[...]`, `list()` on any iterable, mixed types allowed.
- Slice `a[start:stop:step]`; stop is excluded; `a[::-1]` = reversed copy; `a[:]` = shallow copy; slices never crash on out-of-range.
- Lists are mutable (editable in place); strings are not.
- Cheap end = back: `append`/`pop()` are O(1); `insert(0, x)`/`pop(0)` are O(n); `in`/`remove`/`index` are O(n); sorting is O(n log n).
- `sort()`/`reverse()` change in place and return `None`; `sorted()`/`[::-1]` give a new list.
- `extend` pours items in; `append` adds one item — even if that item is a whole list.
- Loop with `for item in a` by default; `enumerate(a)` when index + value are both needed; `range(len(a))` only for writing by index.
- `min`/`max`/`sum` — one-pass built-ins; `min`/`max` crash on an empty list.
- `b = a` → alias (same box, two names). `a.copy()` → new outer box, shared inner boxes. `copy.deepcopy(a)` → fully independent.
- Comprehension: `[expr for x in iterable if cond]`; end-`if` filters, front `if-else` transforms; keep it readable.
- Unpacking: `first, *rest = a` — the star soaks up the leftovers.
- Today's tools: two-pointer swap, single-pass best-so-far, track two maxima with careful order, save-shift-place for rotation.
