# Day 5 — Space Complexity, Recursion Stack, Python Traps, Patterns 16–18

Yesterday was all about "how much TIME does my code take". Today is the other half of the story: **how much MEMORY does it take**. Interviewers ask both. Always.

---

## 1. What is Space Complexity?

Space complexity = how much **extra memory** an algorithm needs as the input grows.

Same Big-O notation as time. Same rules (drop constants, keep the biggest term). Only the question changes:

- Time complexity asks: "How many steps?"
- Space complexity asks: "How many extra boxes of memory?"

Simple example:

```python
def total(arr):
    s = 0            # one variable, always
    for x in arr:
        s += x
    return s
```

No matter if `arr` has 10 items or 10 crore items, we only made **one** extra variable `s`. That is **O(1) space** — constant. The memory does not grow with input.

Now this:

```python
def doubled(arr):
    result = []
    for x in arr:
        result.append(2 * x)
    return result
```

For n items in, we build a new list of n items. Extra memory grows with n. That is **O(n) space**.

---

## 2. Auxiliary Space vs Total Space

Two words you will hear in interviews. The difference is simple.

- **Auxiliary space** = only the EXTRA scratch memory *you* created. Your own variables, your own lists, your recursion stack.
- **Total space** = auxiliary space **+** the input itself.

Dabbawala picture: a customer hands you a full dabba (the input). You also carry your own small tiffin with your lunch (your scratch space).

- Auxiliary space = just **your tiffin**.
- Total space = your tiffin **+ the customer's dabba**.

You did not create the dabba. It was given to you. So when someone says "solve it in O(1) space", they almost always mean **O(1) auxiliary space** — you may read the input, you just cannot build big new structures.

Example: reversing an array **in place** (swapping ends inward).

- Total space: O(n) — the array itself sits in memory.
- Auxiliary space: O(1) — you only used two index variables and a temp.

In interviews, when in doubt, report auxiliary space and say the word "auxiliary". It shows you know the difference.

---

## 3. Why Recursion Costs Memory

Here is the part people forget: **recursion is not free**, even if you create zero lists.

Every time a function calls itself, the current call cannot finish yet. It has to **wait**. Python parks that unfinished call — its variables, its position in the code — in a structure called the **call stack** (a stack = last in, first out pile).

Hostel mess analogy: every unfinished call is a **plate stacked in the mess**. Call `factorial(5)` and it stacks a plate, calls `factorial(4)`, which stacks a plate, calls `factorial(3)`... Only when `factorial(1)` returns do the plates start coming off the pile, top first.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

- `factorial(5)` → 5 plates stacked at the peak → **O(n) auxiliary space**, even though there is no list anywhere.
- `factorial(1000)` → 1000 plates. And here is the catch:

> **Python's default recursion limit is about 1000.** Cross it and you get `RecursionError: maximum recursion depth exceeded`. The mess ran out of vertical space for plates.

A loop version of factorial uses O(1) space — one running variable, no plate stack. Same answer, same O(n) time, but constant memory. This is exactly why interviewers ask "what is the space complexity of your recursion?" — the loop and the recursion look equally fast, but the recursion silently eats O(depth) memory.

Rule of thumb: **space of recursion = maximum depth of the call stack.**

---

## 4. Two Python Performance Traps

These two look innocent. Both are O(n). Both have burned many people in interviews.

### Trap 1: `list.insert(0, x)` is O(n)

`my_list.insert(0, x)` puts `x` at the front. Feels like one step. It is not.

A Python list is a row of consecutive seats in memory. To put a new passenger at **seat 1** of a full train berth row, **every single person already sitting must shift one seat to the right**. n people sitting = n shifts. So inserting at the front is O(n).

```python
# BAD: building a reversed list, O(n^2) total
result = []
for x in items:
    result.insert(0, x)   # each insert shifts everything: O(n)
```

- `append()` adds at the END — the last seat is free, nobody shifts — **O(1)** (amortised, meaning "on average").
- Need fast inserts at the front? Use `collections.deque` — its `appendleft()` is O(1).

### Trap 2: `x in my_list` is O(n), but `x in my_set` is O(1)

`in` on a **list** checks elements one by one from the start. Worst case it walks the whole list. O(n). Put that inside a loop and you have accidentally written an O(n²) program.

`in` on a **set** (or dictionary keys) is **O(1) on average**. A set uses hashing — it computes a number from the value that tells it directly where to look.

Hotel analogy: a list is a hotel with **no register** — to find a guest you knock on every room, one by one. A set is a hotel **with a register**: you say the name, the register instantly says "Room 204", you walk straight there.

```python
seen_list = [...]           # 'x in seen_list'  -> O(n), knocks every room
seen_set  = set(seen_list)  # 'x in seen_set'   -> O(1) avg, checks register
```

Classic interview move: "I'll keep a set of seen elements so each membership check is O(1)." That one line turns many O(n²) solutions into O(n). Cost of the trick: the set itself takes O(n) auxiliary space. Memory bought speed — a very common trade.

---

## 5. Patterns 16–18 (solved today)

All three are in `main.py`. Shapes for n = 5:

**Pattern 16 — Alpha-Repeat Triangle.** Row i prints the i-th letter, repeated (i+1) times. Row 0 is `A` once, row 1 is `B` twice... Key line: `char = 65 + i` fixes the letter per ROW (65 is the character code for `'A'`), and the inner loop just repeats it.

```
A
BB
CCC
DDDD
EEEEE
```

**Pattern 17 — Alphabet Hill.** Each row climbs up the alphabet then walks back down: `A`, then `ABA`, then `ABCBA`... Centered with spaces, like the star pyramid but with letters. The tricky part is ONE variable `chars` that goes up (+1) until the middle of the row, then comes down (−1). Full trace in `notes.ipynb`.

```
    A
   ABA
  ABCBA
 ABCDBCA   <- actually ABCDCBA
ABCDEDCBA
```

(For n=5 the last row is `ABCDEDCBA` — climb to the (i+1)-th letter, then descend.)

**Pattern 18 — Alpha Triangle.** Starts from the LAST letter and grows leftward each row: `E`, then `D E`, then `C D E`... Key idea: the row's first letter is `chr(64 + n - i)`, then count up to `E`.

```
E
D E
C D E
B C D E
A B C D E
```

All three: **O(n²) time** (n rows, up to ~n prints per row), **O(1) auxiliary space** (just loop counters and one char variable — nothing grows with n).

---

## 6. Pending Problems — Approach and Hints Only

These are next up (`main.py`'s last comment says so). No full solutions here — think first, then code.

### a) Patterns 19–22

- **Pattern 19:** two triangles stacked — top half shrinks (stars, gap in the middle grows), bottom half grows back. Think: each row = stars + spaces + stars.
- **Pattern 20:** the mirror of 19 — grows first, then shrinks. Same "stars-spaces-stars" skeleton, flipped.
- **Pattern 21:** hollow rectangle. Print `*` only when you are on a border: first row, last row, first column, or last column. One `if` with `or`s.
- **Pattern 22:** the number-square (for n=4, outermost ring is all 4s, then 3s inside, ...). Hint: the value at cell (i, j) is `n − min(distance to nearest edge)`. Compute `min(i, j, size−1−i, size−1−j)` where size = 2n−1.

### b) Trailing zeroes in n!

Question: how many zeros at the END of n factorial? (10! = 3628800 → 2 trailing zeros.)

**Do NOT compute n! and count zeros.** n! explodes — 100! has 158 digits. There is a pure counting trick.

Why do trailing zeros even appear? A trailing zero = one factor of **10** = one pair of **2 × 5** inside the product. Now, in 1×2×3×...×n, factors of 2 are everywhere (every second number gives one). Factors of **5 are rarer** — only every fifth number. So the 5s are the bottleneck: **count the 5s, and each is guaranteed a 2 to pair with.**

Counting the 5s:

- `n // 5` → numbers that contribute at least one 5 (5, 10, 15, ...)
- `n // 25` → numbers like 25, 50 contribute a SECOND 5 (25 = 5×5) — add them again
- `n // 125` → a third 5, and so on until the divisor exceeds n

So the answer is `n//5 + n//25 + n//125 + ...` — a tiny loop multiplying the divisor by 5 each round. Time O(log₅ n), space O(1). Check yourself: n = 100 should give 24.

### c) Digit sum

Sum of digits of n (e.g. 1234 → 10). Same two tools as Day 4's extract-digits problem:

- `n % 10` peels off the LAST digit (like taking the last coin off a stack of rupee coins).
- `n // 10` throws that digit away.

Loop while `n > 0`, keep adding `n % 10` into a total. O(number of digits) = O(log₁₀ n) time, O(1) space. Edge case to handle: negative n (take `abs` first) and n = 0 (answer is 0 — make sure your loop doesn't skip it).

### d) Count of digits WITHOUT a loop

Two one-liners; know both and why they work.

1. **String way:** `len(str(n))` — turn the number into text, count the characters. Honest and readable. (Careful: for negatives the minus sign gets counted — `abs` first.)
2. **Log way:** `floor(log10(n)) + 1`. The gentle idea: log₁₀(n) asks "10 to the power WHAT gives n?". Powers of 10 are exactly the digit boundaries — 10¹ = 10 (2 digits start), 10² = 100 (3 digits start), 10³ = 1000 (4 digits start). So any 3-digit number n sits between 100 and 999, meaning log₁₀(n) is between 2 and 2.99..., and `floor` of that is 2. Add 1 → 3 digits. In code: `math.floor(math.log10(n)) + 1`. Edge cases: n = 0 breaks it (log of 0 is undefined) — handle it separately; negatives need `abs`.

---

## Common mistakes

- Saying "O(1) space" for a recursive solution. The recursion stack counts! Depth d ⇒ O(d) auxiliary space.
- Mixing up auxiliary and total space. When an interviewer says "constant space", they mean auxiliary — the input does not count against you.
- Using `result.insert(0, x)` inside a loop and thinking it's O(1). Every insert-at-front shifts the whole list. Use `append` + reverse at the end, or a `deque`.
- Writing `if x in big_list` inside a loop → hidden O(n²). Convert to a set once, then check.
- Trying to actually compute n! to count trailing zeros. Count factors of 5 instead.
- Forgetting `n // 25`, `n // 125`... in the trailing-zeros formula (25 gives TWO fives, not one).
- `len(str(n))` on a negative number counts the `-` sign as a digit.
- Recursing ~1000 deep in Python and getting a `RecursionError` — the default limit is around 1000.

## Quick recap

- Space complexity = how the EXTRA memory grows with input. Same Big-O language as time.
- Auxiliary = your tiffin (scratch space). Total = your tiffin + the customer's dabba (input). Report auxiliary.
- Recursion space = max stack depth. `factorial(n)` recursion = O(n) space; the loop version = O(1).
- `list.insert(0, x)` → O(n) (everyone shifts a seat). `append` → O(1).
- `x in list` → O(n) (knock every room). `x in set` → O(1) avg (hotel register).
- Patterns 16–18: letter triangles/hill, all O(n²) time, O(1) space.
- Trailing zeros in n! = count of 5s = `n//5 + n//25 + ...` (5s are rarer than 2s).
- Digit sum: `% 10` to peel, `// 10` to drop. Digit count without loop: `len(str(n))` or `floor(log10(n)) + 1`.
