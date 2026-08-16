[<< Day 04](../../Day-04/DSA/notes.md) | [🏠 Today's tasks](../task.md) | [Day 06 >>](../../Day-06/DSA/notes.md)

# Day 5 — Space Complexity, Recursion Stack, Python Traps, Patterns 16–22

## Yesterday → Today

Yesterday (Day 4) I learned to measure **TIME** — O(1), O(log n), O(n), O(n²), the whole Big-O family. But a computer has TWO limited resources, not one. Time is the first. **Memory is the second.**

Today is the other half of the same skill: instead of asking *"how many steps does my code take?"*, I ask *"how much extra memory does it grab while working?"* Same Big-O language, same growth-thinking, different resource. Interviewers always ask both together: *"what is the time AND space complexity?"*

Bonus reunion: the `%` and `//` friends from Day 1's digit loops return today in the practice problems. They never really left.

---

## 1. What is Space Complexity?

Space complexity = how much **extra memory** an algorithm needs, and how that grows when the input grows.

Key word: **extra**. We do not blame the algorithm for the input it was handed. We only count what it *creates* while working — variables, new lists, the recursion stack.

Same Big-O classes as yesterday, just measuring bytes instead of steps:

- `O(1)` space → a fixed handful of variables, no matter how big the input is.
- `O(n)` space → creates something (a list, a set, a call stack) that grows with the input.

```python
def total(arr):        # arr has n items
    s = 0              # one variable
    for x in arr:
        s += x
    return s           # extra memory used: just s and x → O(1)
```

```python
def doubled(arr):
    out = []           # NEW list that grows to n items
    for x in arr:
        out.append(2 * x)
    return out         # extra memory: O(n)
```

Both loops are O(n) **time**. But in space they are worlds apart. That is why we always report both.

---

## 2. Auxiliary Space vs Total Space

Two words that confuse everyone exactly once. Analogy first.

You run a tiffin service. A customer hands you his own big **dabba** (steel tiffin box) full of food to repack. You bring your **own small tiffin** with your tools and spare containers.

- **Auxiliary space** = only YOUR tiffin. The scratch space *you* brought — extra variables, temp lists, the recursion stack.
- **Total space** = your tiffin **+ the customer's dabba**. Everything on the kitchen counter, including the input itself.

> **Total space = input space + auxiliary space**

For `total(arr)` above:

- Auxiliary space: `O(1)` — just `s` and `x`.
- Total space: `O(n)` — the input list `arr` is sitting in memory too.

### The interview convention

When an interviewer says *"solve it in O(1) space"*, they mean **auxiliary space**. The input is always allowed to exist — nobody expects you to make the customer's dabba disappear. If ever unsure, say it out loud: *"O(1) auxiliary space, O(n) total including the input."* That one sentence sounds very polished.

---

## 3. In-place vs Extra-space — the Classic: Reverse a List

Many problems have two honest solutions. Reversing a list is THE textbook example.

```python
# Way 1: reverse into a COPY — easy, but O(n) extra space
def reversed_copy(arr):
    out = []
    for x in arr:
        out.append(x)
    out.reverse()
    return out          # a second full list now exists

# Way 2: reverse IN-PLACE — two pointers, O(1) auxiliary space
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # swap the ends
        left += 1
        right -= 1      # walk inward until the pointers meet
```

**In-place** = rearrange the input inside its own memory, using only a fixed few variables. Like rearranging furniture **inside your own room** instead of renting a second room to hold everything while you shuffle.

The trade-off, honestly:

- **Copy way:** the original stays safe and untouched. Cost: double the memory.
- **In-place way:** O(1) auxiliary space. Cost: the **original order is destroyed** — if other code still needed it, you just broke it.

Neither is "always right". When an interviewer asks *"can you do it in-place?"*, they are really asking: *can you reach O(1) auxiliary space?* Say the trade-off out loud; it shows you understand *why*, not just *how*.

### The `[::-1]` trap

`arr[::-1]` reverses in one line — but **slicing builds a brand-new list**. That is the copy way in disguise: O(n) space, NOT in-place. One-liners can hide costs; Big-O eyes see through them.

---

## 4. Recursion Has a Hidden Space Cost

Recursion = a function calling itself. Each call that has **started but not finished** must wait somewhere. That "somewhere" is the **call stack** — a memory area where Python keeps one *frame* (a small record: parameters, local variables, where to resume) per unfinished call.

Think of the **hostel mess plate stack**. Every new call puts one more plate on top. Plates come off only from the top, in reverse order — last placed, first removed. Nothing below can leave until everything above it is done.

```python
def countdown(n):
    if n == 0:          # base case — the stopping condition
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)    # this call WAITS here until the inner one finishes
```

Calling `countdown(3)`:

```
countdown(3)  → waits
  countdown(2)  → waits
    countdown(1)  → waits
      countdown(0)  → prints "Blast off!", returns
    countdown(1) finishes
  countdown(2) finishes
countdown(3) finishes
```

At the deepest moment, **4 plates** are on the stack at once. So:

> **Recursion space = O(maximum stack depth)** — here O(n), even though no list was created anywhere.

This is the classic trap: a recursive function with zero arrays still costs O(n) *auxiliary* space, because the stack IS memory.

### Python's ~1000-frame ceiling

Python refuses to stack plates forever. The default limit is around **1000** frames. Go deeper → `RecursionError: maximum recursion depth exceeded`. So `countdown(5000)` crashes — not because the logic is wrong, but because the plate stack hit the kitchen ceiling.

```python
import sys
print(sys.getrecursionlimit())   # usually 1000
```

Lesson: for very deep work in Python, prefer a loop. A loop reuses the *same* frame → O(1) auxiliary space.

---

## 5. The Strings-in-Loops O(n²) Trap

Python strings are **immutable** — once created, never changed. So `s += ch` does NOT extend `s`. It builds a **brand-new string**, copying every character of the old one plus the new one, then throws the old one away.

Like getting a wedding invitation card **reprinted from scratch** every time one more guest name is added. One name added → whole card reprinted. Do that n times and you have copied roughly 1 + 2 + 3 + ... + n characters → **O(n²) time**, plus a trail of throwaway strings for the garbage collector.

```python
# BAD: each += copies everything built so far
s = ""
for ch in parts:
    s += ch            # new string every single time → O(n²)

# GOOD: collect in a list (append is cheap), print the card ONCE
pieces = []
for ch in parts:
    pieces.append(ch)  # O(1) each
s = "".join(pieces)    # one O(n) pass — total O(n)
```

Rule of thumb: **many string additions in a loop → build a list, `join` once.**

---

## 6. Big Trap 1: `list.insert(0, x)` is O(n)

`insert(0, x)` puts `x` at the **front** of a list. Looks innocent. It is not.

Python lists store items in one continuous block of memory, in order. To squeeze a new passenger into **seat 1** of a fully occupied train-berth row, *every* passenger already seated must shift one seat over. One insert at the front = n shifts = **O(n)**.

`append(x)` adds at the **end** — the last seat is free, nobody moves — **O(1)**.

### The accidental O(n²) loop

```python
# BAD: builds a reversed list, but each insert shifts everything
result = []
for x in data:
    result.insert(0, x)    # O(n) shift, done n times → O(n²) total
```

n inserts × up to n shifts each ≈ n² work. For n = 100,000 that is ~10 billion shift operations. Your "simple" loop crawls.

### The fixes

```python
# Fix 1: append (O(1) each), reverse once at the end
result = []
for x in data:
    result.append(x)
result.reverse()             # one O(n) pass — total O(n)

# Fix 2: collections.deque — a "double-ended queue",
# built to accept items at BOTH ends in O(1)
from collections import deque
d = deque()
d.appendleft(x)              # O(1), no shifting
```

Rule of thumb: **never `insert(0, ...)` inside a loop.**

---

## 7. Big Trap 2: `x in list` is O(n), `x in set` is ~O(1)

`in` asks "is this value present?". On a **list**, Python checks item by item, front to back — like finding your friend in a hotel by **knocking on every room door** one by one. Worst case: n knocks → **O(n)**. Do that inside a loop over n items → O(n²) again.

A **set** is different. A set uses **hashing** — a maths trick that converts a value into a number saying exactly *which shelf* it lives on. So `x in my_set` is like asking the **hotel reception register**: one lookup, straight answer → **~O(1)** on average.

```python
rooms_list = ["Amit", "Bala", "Chitra", "Deepak"]
rooms_set  = set(rooms_list)     # one-time O(n) conversion

"Chitra" in rooms_list   # knocks door by door → O(n)
"Chitra" in rooms_set    # asks the register  → ~O(1)
```

### The space-for-time principle

The set is not free — it is a second copy of the data, **O(n) extra space**. You *spend memory to buy speed*. This trade is one of the most common moves in all of DSA: seen-before checks, duplicate detection, two-sum — all use it. Rule of thumb: **many membership checks → convert to a set first.**

The reverse trade exists too: the in-place reverse from section 3 *spends effort to save memory*. Time and space are two pans of a weighing scale — pressing one down often lifts the other. A good engineer chooses which pan to press, on purpose.

---

## 8. Cheat-Sheet: What Common Python Operations Really Cost

| Operation | Cost | Why |
|---|---|---|
| `arr.append(x)` | O(1) amortized* | last seat is free |
| `arr.pop()` (from end) | O(1) | remove last, nobody shifts |
| `arr.pop(0)` (from front) | O(n) | everyone shifts left |
| `arr.insert(0, x)` | O(n) | everyone shifts right |
| `x in arr` (list) | O(n) | door-to-door check |
| `x in s` (set/dict) | ~O(1) | hash → straight to the shelf |
| `arr.sort()` | O(n log n) | comparison sorting's proven floor |
| `len(arr)` | O(1) | Python stores the count, no counting |
| `arr[a:b]` (slicing) | O(k) | **copies** k items — new list! |

\* *Amortized* = averaged over many calls. Once in a while `append` must move the whole list to a bigger memory block (O(n) that one time), but it grabs extra room while doing so — spread across all appends, each averages O(1). Like a hostel warden who, when beds run out, shifts everyone to a hall with double the beds: a big move, but rare enough that the per-student cost stays tiny.

Two rows deserve a second look:

- `len()` being O(1) is why `while len(arr) > 0:` is fine — no hidden counting.
- Slicing being a **copy** is the quiet one: `arr[:]`, `arr[::-1]`, `arr[1:]` all allocate new lists. Inside a loop, that is an easy accidental O(n²) in both time and space.

---

## 9. Patterns 16–22 — Shapes + Hints Only

New tool for letter patterns: `chr()` and `ord()`. Every character has a standard code number (ASCII). **`chr(65)` is `'A'`**, `chr(66)` is `'B'` ... `chr(90)` is `'Z'`. `ord('A')` goes the other way and gives 65. So "the i-th capital letter" is simply `chr(65 + i)`. Everything else is the same row/column thinking from patterns 1–15.

For each pattern: the n = 5 shape, plus a one-line row-logic hint. No code — that is your job on paper first.

### Pattern 16 — Alphabet-repeat triangle

```
A
BB
CCC
DDDD
EEEEE
```

Hint: row `i` picks ONE letter, `chr(65 + i)`, and repeats it `i + 1` times — the letter is fixed per row, only the count grows.

### Pattern 17 — Alphabet hill (palindrome pyramid)

```
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
```

Hint: row `i` = `n - i - 1` spaces, then climb `A` up to the i-th letter, then walk back down without repeating the peak — go up while the column is at or before the middle of the `2i + 1` letters, come down after it.

### Pattern 18 — Reverse-alphabet triangle

```
E
D E
C D E
B C D E
A B C D E
```

Hint: every row ENDS at the last letter `chr(64 + n)`; row `i` just starts `i` letters earlier and counts up — the start code is `(64 + n) - i`.

### Pattern 19 — Hourglass of stars (shrink, then grow)

```
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
```

Hint: two triangles stacked; each row is stars + middle spaces + stars — in the top half row `i` has `n - i` stars each side and `2i` spaces between; the bottom half is the same rows in reverse.

### Pattern 20 — Butterfly

```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

Hint: mirror of 19 — wings grow to a full middle row then shrink; with `i` stars per side the gap is `2 * (n - i)` spaces, and there are `2n - 1` rows in total.

### Pattern 21 — Hollow rectangle

```
*****
*   *
*   *
*   *
*****
```

Hint: print `*` only when the cell is on a border — first/last row OR first/last column (one `if` with `or`s) — otherwise print a space.

### Pattern 22 — Number rings

```
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
```

Hint: a `(2n-1) × (2n-1)` grid where each cell's value = `n` minus its distance from the NEAREST edge — that distance is `min(i, j, size-1-i, size-1-j)`.

---

## 10. Maths Problems — Hints Only

Your Day-1 friends `%` and `//` are back. Told you they would return.

### Trailing zeroes in n! (factorial)

`n!` = 1 × 2 × 3 × ... × n. Question: how many zeroes at the END? Example: 10! = 3,628,800 → two trailing zeroes.

Do **NOT** compute n! — it explodes in size. Think instead:

- Every trailing zero is one factor of **10**, and 10 = **2 × 5**. So count (2, 5) pairs.
- Factors of 2 are everywhere (every second number). Factors of **5 are the rare ones** — so the answer = number of 5s hiding inside 1..n.
- Count them: `n//5 + n//25 + n//125 + ...` until the term becomes 0.
- Why the extra terms? **25 = 5 × 5 contributes TWO fives**, but `n//5` counted it only once — `n//25` adds its second five. Same idea: 125 gives a third five via `n//125`.
- Sanity check with n = 25: `25//5 = 5`, `25//25 = 1` → 6 trailing zeroes.

### Digit sum

Sum of digits of 5341 → 5 + 3 + 4 + 1 = 13.

- `n % 10` peels off the **last** digit.
- `n // 10` **removes** that last digit.
- Loop while `n > 0`: add the peel, then shrink. 5341 → 534 → 53 → 5 → 0.
- Time O(number of digits) = O(log₁₀ n) — each step chops the number to a tenth. Yesterday's O(log n) class, live in the wild.

### Count of digits WITHOUT a loop

Two ways:

1. **String way:** `len(str(n))` — turn the number into text, count the characters. Handle the minus sign for negatives.
2. **Maths way:** `floor(log10(n)) + 1`. The gentle idea: digit count changes exactly at **powers of 10**. Numbers 1–9 have 1 digit; 10–99 have 2; 100–999 have 3. `log10(n)` tells you which power-of-10 band `n` sits in: log10 of anything from 100 to 999 is between 2 and 2.99..., floor gives 2, plus 1 → 3 digits.
3. Edge cases for the log way: `n = 0` (log10(0) is undefined — answer is 1) and negatives (take `abs(n)` first).

---

## Common mistakes

- Saying an algorithm is O(1) space while ignoring the **recursion stack**. Recursion depth IS auxiliary space.
- Mixing up auxiliary and total space. "Space complexity" in an interview almost always means **auxiliary**.
- Claiming O(1) space after reversing with `arr[::-1]` — slicing **copies**, that is O(n) extra. In-place means the two-pointer swap.
- Using `insert(0, x)` inside a loop and wondering why the code crawls — that is an accidental O(n²).
- Writing `x in some_list` inside a loop. Many lookups → convert to a set first.
- Building a string with `+=` inside a loop — immutable strings mean a full reprint every time, O(n²). Collect in a list, `join` once.
- Forgetting the base case in recursion → infinite calls → `RecursionError` at depth ~1000.
- In pattern 17, printing the peak letter twice — the descent must start immediately *after* the middle column.
- In trailing zeroes, counting 2s or actually computing n! — count only 5s, with the `//25`, `//125` corrections.
- The `log10` method crashing on 0 or negatives — handle those separately.

---

## Quick recap

- Space complexity = growth of **extra** memory, in the same Big-O language as Day 4's time classes.
- Auxiliary = your scratch space (your tiffin); total = auxiliary + input (plus the customer's dabba). "O(1) space" in interviews = auxiliary.
- In-place = rearrange inside the input's own memory (two-pointer reverse, O(1) auxiliary) but the original is destroyed; the copy way is safe but doubles memory. `[::-1]` is secretly the copy way.
- Every unfinished recursive call is a plate on the mess stack. Space = **max depth**. Python's ceiling ≈ 1000 frames; deep work → prefer a loop.
- Strings are immutable → `s += ch` in a loop reprints the whole card each time, O(n²). Fix: list + `"".join()`.
- `insert(0, x)` shifts every passenger (train-berth seat 1) → O(n); in a loop → O(n²). Use `append` + one reverse, or `deque.appendleft`.
- `x in list` = knocking every room, O(n). `x in set` = hotel register via hashing, ~O(1), costing O(n) extra space. Space-for-time: spend memory to buy speed — and sometimes the reverse.
- Cheat-sheet: `append`/`pop()`/`len` O(1), `pop(0)`/`insert(0)`/`in list` O(n), `in set` ~O(1), `sort` O(n log n), slicing O(k) **and it copies**.
- Letter patterns run on `chr(65 + i)`; hill climbs then descends; butterfly/hourglass = stars + gap + stars; hollow rectangle = border `if`; rings = `n − min(distance to each edge)`.
- Trailing zeroes in n! = count of 5s: `n//5 + n//25 + ...`. Digit sum = `%10` and `//10`. Digit count without a loop = `len(str(n))` or `floor(log10(n)) + 1`.

---

## Learn more

- GeeksforGeeks — What does space complexity mean: <https://www.geeksforgeeks.org/dsa/g-fact-86/>
- GeeksforGeeks — Complexity cheat sheet for Python operations: <https://www.geeksforgeeks.org/python/complexity-cheat-sheet-for-python-operations/>
- Python wiki — Time complexity of built-ins: <https://wiki.python.org/moin/TimeComplexity>
- Python docs — `collections.deque`: <https://docs.python.org/3/library/collections.html#collections.deque>
- Striver's pattern playlist (patterns reference): <https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/>

---

## Tomorrow

Day 6 = our **first real data structure: the list**, properly. Everything priced today — the shifting seats, the door-to-door search, the copy-making slices — stops being theory and becomes daily practice. You now know the cost of every move before you make it. Tomorrow you make the moves.

---

[<< Day 04](../../Day-04/DSA/notes.md) | [🏠 Today's tasks](../task.md) | [Day 06 >>](../../Day-06/DSA/notes.md)
