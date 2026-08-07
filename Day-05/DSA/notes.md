# Day 5 — Space Complexity, Recursion Stack, Python Traps, Patterns 16–22

Till now I only asked "how much TIME does my code take?". Today the other half: **how much MEMORY does it take?** Interviewers always ask both together.

---

## 1. What is Space Complexity?

Space complexity = how much **extra memory** an algorithm needs, and how that grows when the input grows.

Key word: **extra**. We do not blame the algorithm for the input it was handed. We only count what it *creates* while working — variables, new lists, the recursion stack, etc.

Just like time complexity, we write it in Big-O:

- `O(1)` space → uses a fixed handful of variables, no matter how big the input is.
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

---

## 2. Auxiliary Space vs Total Space

Two words that confuse everyone once. Analogy first.

You run a tiffin service. A customer hands you his own big **dabba** (steel tiffin box) full of food to repack. You bring your **own small tiffin** with your tools and spare containers.

- **Auxiliary space** = only YOUR tiffin. The scratch space *you* brought — extra variables, temp lists, the recursion stack.
- **Total space** = your tiffin **+ the customer's dabba**. Everything in the kitchen, including the input itself.

So:

> **Total space = input space + auxiliary space**

For the `total(arr)` function above:

- Auxiliary space: `O(1)` (just `s` and `x`)
- Total space: `O(n)` (the input list `arr` is sitting in memory too)

### The interview convention

When an interviewer says *"solve it in O(1) space"*, they mean **auxiliary space**. The input is always allowed to exist — nobody expects you to make the customer's dabba disappear. If you are ever unsure, say it out loud: *"O(1) auxiliary space, O(n) total including the input"*. That one sentence sounds very polished.

---

## 3. Recursion Has a Hidden Space Cost

Recursion = a function calling itself. Each call that has **started but not finished** must wait somewhere. That "somewhere" is the **call stack** — a special area of memory where Python keeps one frame (a small record: parameters, local variables, where to resume) per unfinished call.

Think of the **hostel mess plate stack**. Every new call puts one more plate on top. Plates come off only from the top, in reverse order — last one placed, first one removed. Nothing below can leave until everything above it is done.

My own tiny example:

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

This is the classic trap: a recursive function with no arrays still costs O(n) *auxiliary* space because of the stack.

### Python's recursion limit

Python refuses to stack plates forever. The default limit is around **1000** frames. Go deeper and you get `RecursionError: maximum recursion depth exceeded`. So `countdown(5000)` crashes — not because the logic is wrong, but because the plate stack hit the ceiling. Check it with:

```python
import sys
print(sys.getrecursionlimit())   # usually 1000
```

Lesson: for very deep work in Python, prefer a loop. A loop reuses the *same* frame → O(1) auxiliary space.

---

## 4. Python Trap 1: `list.insert(0, x)` is O(n)

`insert(0, x)` puts `x` at the **front** of a list. Looks innocent. It is not.

Python lists store items in one continuous block of memory, in order. To squeeze a new passenger into **seat 1** of a fully occupied train berth row, *every* passenger already seated must shift one seat to the right. One insert at the front = n shifts = **O(n)**.

`append(x)` adds at the **end** — the last seat is free, nobody moves — **O(1)**.

### The O(n²) loop trap

```python
# BAD: builds a reversed list, but each insert shifts everything
result = []
for x in data:
    result.insert(0, x)    # O(n) shift, done n times → O(n²) total
```

n inserts × n shifts each ≈ n² work. For n = 100,000 that is ~10 billion shift operations. Your "simple" loop crawls.

### The fixes

```python
# Fix 1: append (O(1) each), reverse once at the end if needed
result = []
for x in data:
    result.append(x)
result.reverse()             # one O(n) pass, total O(n)

# Fix 2: collections.deque — a "double-ended queue",
# a structure built to accept items at BOTH ends in O(1)
from collections import deque
d = deque()
d.appendleft(x)              # O(1), no shifting
```

Rule of thumb: **never `insert(0, ...)` inside a loop.**

---

## 5. Python Trap 2: `x in list` is O(n)

`in` asks "is this value present?". On a **list**, Python checks item by item, front to back — like finding your friend in a hotel by **knocking on every room door** one by one. Worst case: n knocks → **O(n)**. Do that inside a loop over n items → O(n²) again.

A **set** is different. A set uses **hashing** — a math trick that converts a value into a number that says exactly *which shelf* it lives on. So `x in my_set` is like asking the **hotel reception register**: one lookup, straight answer → **~O(1)** on average.

```python
rooms_list = ["Amit", "Bala", "Chitra", "Deepak"]
rooms_set  = set(rooms_list)     # one-time O(n) conversion

"Chitra" in rooms_list   # knocks door by door → O(n)
"Chitra" in rooms_set    # asks the register  → ~O(1)
```

### The space-for-time trade-off

The set is not free — it is a second copy of the data, so it costs **O(n) extra space**. You *spend memory to save time*. This trade is one of the most common moves in all of DSA: seen-before checks, duplicate detection, two-sum — all use it. Rule of thumb: **many membership checks → convert to a set first.**

---

## 6. Patterns 16–22

New tool for letter patterns: `chr()` and `ord()`. Every character has a standard code number (ASCII). **`chr(65)` is `'A'`**, `chr(66)` is `'B'` ... `chr(90)` is `'Z'`. `ord('A')` goes the other way and gives 65. So "the i-th capital letter" is simply `chr(65 + i)`. Everything else is the same row/column thinking from patterns 1–15.

For each pattern: the n = 5 shape, plus a one-line row-logic hint. No code — that is my job on paper first.

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

Hint: every row ENDS at the last letter `chr(64 + n)`; row `i` just starts `i` letters earlier and counts up — start code is `(64 + n) - i`.

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

## 7. Maths Problems — Approach + Hints Only

### Trailing zeroes in n! (factorial)

`n!` (n factorial) = 1 × 2 × 3 × ... × n. Question: how many zeroes at the END of that number? Example: 10! = 3,628,800 → two trailing zeroes.

Do **NOT** compute n! — it explodes in size. Think instead:

- Every trailing zero is one factor of **10**, and 10 = **2 × 5**. So count (2, 5) pairs.
- Factors of 2 are everywhere (every second number). Factors of **5 are the rare ones** — so the answer = number of 5s hiding inside 1..n.
- Count them: `n//5 + n//25 + n//125 + ...` until the term becomes 0.
- Why the extra terms? **25 = 5 × 5 contributes TWO fives**, but `n//5` counted it only once — `n//25` adds its second five. Same idea: 125 gives a third five via `n//125`.
- Sanity check with n = 25: `25//5 = 5`, `25//25 = 1` → 6 trailing zeroes.

### Digit sum

Sum of digits of 5341 → 5 + 3 + 4 + 1 = 13.

- `n % 10` (remainder on dividing by 10) peels off the **last** digit.
- `n // 10` (whole-number division) **removes** that last digit.
- Loop while `n > 0`: add the peel, then shrink. 5341 → 534 → 53 → 5 → 0.
- Time O(number of digits) = O(log₁₀ n) — each step chops the number to a tenth.

### Count of digits WITHOUT a loop

Two ways:

1. **String way:** `len(str(n))` — turn the number into text, count the characters. Handle the minus sign for negatives.
2. **Maths way:** `floor(log10(n)) + 1`. The gentle idea: digit count changes exactly at **powers of 10**. Numbers 1–9 (below 10¹) have 1 digit; 10–99 (below 10²) have 2; 100–999 have 3. `log10(n)` tells you which power-of-10 band `n` sits in: log10 of anything from 100 to 999 is between 2 and 2.99..., floor gives 2, plus 1 → 3 digits.
3. Edge cases for the log way: `n = 0` (log10(0) is undefined — answer is 1) and negative numbers (take `abs(n)` first).

---

## Common mistakes

- Saying an algorithm is O(1) space while ignoring the **recursion stack**. Recursion depth IS auxiliary space.
- Mixing up auxiliary and total space. When asked "space complexity" in an interview, they almost always mean **auxiliary**.
- Using `insert(0, x)` inside a loop and wondering why the code is slow — that is an accidental O(n²).
- Writing `x in some_list` inside a loop. Convert to a set first when there are many lookups.
- Forgetting the base case in recursion → infinite calls → `RecursionError` at depth ~1000.
- In pattern 17, printing the peak letter twice — the descent must start immediately *after* the middle column.
- In trailing zeroes, counting 2s or actually computing n! — count only 5s, with the `//25`, `//125` corrections.
- `log10` method crashing on 0 or negatives — handle those separately.

---

## Quick recap

- Space complexity = growth of **extra** memory. Auxiliary = your scratch space (your tiffin); total = auxiliary + input (plus the customer's dabba). "O(1) space" in interviews = auxiliary.
- Every unfinished recursive call is a plate on the mess stack. Space = **max depth**. Python's stack limit ≈ 1000.
- `insert(0, x)` shifts every element (train-berth seat 1) → O(n); in a loop → O(n²). Use `append` + one reverse, or `deque.appendleft`.
- `x in list` = knocking every room, O(n). `x in set` = hotel register via hashing, ~O(1), at the cost of O(n) extra space.
- Letter patterns run on `chr(65 + i)`; hill pattern climbs then descends; butterfly/hourglass = stars + gap + stars; hollow rectangle = border `if`; rings = `n − min(distance to each edge)`.
- Trailing zeroes in n! = count of 5s: `n//5 + n//25 + ...`. Digit sum = `%10` and `//10`. Digit count without loop = `len(str(n))` or `floor(log10(n)) + 1`.
