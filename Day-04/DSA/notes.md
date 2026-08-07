# Day 4 — Big-O Notation (Time & Space Complexity)

Today no new problems. Today I learn how to *measure* the problems I have already solved.

---

## 1. Why not just measure seconds?

Suppose I run my code on my laptop and it takes 2 seconds. My friend runs the same code on a faster machine and it takes 0.5 seconds. Same code, different times.

It is like a recipe. The same chai recipe takes 5 minutes on a gas stove and 8 minutes on an induction plate. The recipe did not change — the stove did.

So we do not measure **seconds**. We measure the **number of steps (operations)** the recipe needs. Steps stay the same no matter which stove (computer) you use.

- **Operation** = one small unit of work: an addition, a comparison, a print, an assignment.
- **n** = the size of the input (how many guests, how many digits, how big the number).

The question Big-O answers is: **if n grows, how fast does the number of steps grow?**

---

## 2. What does "grows with n" mean?

Say a function does `3n + 5` operations.

| n | operations |
|---|---|
| 10 | 35 |
| 1,000 | 3,005 |
| 1,000,000 | 3,000,005 |

The `+5` stops mattering very quickly. Even the `3×` in front does not change the *shape* of growth — it is still a straight line. Big-O only keeps the shape: `3n + 5` → **O(n)**.

**Big-O** is just a short way of writing "roughly how the step count grows as input grows".

---

## 3. The main complexity classes (with examples that actually make sense)

### O(1) — Constant time
Same number of steps no matter how big the input is.

> Checking your UPI balance. Whether you have ₹100 or ₹1 crore in the account, the app shows the balance in the same one tap. The *size* of the money does not add steps.

```python
def get_first(arr):
    return arr[0]   # 1 step, always
```

### O(log n) — Logarithmic time
Each step cuts the problem in **half**.

> Finding "Sharma" in a printed phone book. You do not read page 1, page 2, page 3... You open the **middle**. Sharma comes after M? Throw away the first half. Open the middle of the remaining half. Repeat. A 1,000-page book needs only about 10 openings, because 2¹⁰ ≈ 1000.

**log n** (log base 2 of n) = "how many times can I halve n before reaching 1". For n = 1,000,000 that is only ~20. Log time is *very* fast.

```python
# binary search: each loop iteration halves the search space
while low <= high:
    mid = (low + high) // 2
    ...
```

### O(n) — Linear time
You must touch every element once.

> Serving chai to every guest at home. 10 guests = 10 cups. 100 guests = 100 cups. Double the guests, double the work. There is no shortcut — everyone gets a cup.

```python
for i in range(n):   # runs exactly n times
    total += i
```

### O(n log n) — Linearithmic time
The time of good sorting algorithms (merge sort, and Python's built-in `sort`).

> Sorting a bundle of exam papers by roll number. Split the bundle in half, sort each half, then merge the two sorted piles. Splitting in half again and again gives the **log n** levels; merging at each level touches all **n** papers. Total: n work × log n levels = **n log n**.

For n = 1,000,000: n² would be 10¹² steps (too slow), but n log n is only ~2×10⁷. That is why sorting a million items feels instant.

### O(n²) — Quadratic time
Every element interacts with every other element. Usually a **loop inside a loop**.

> A wedding with n guests where every guest shakes hands with every other guest. 10 guests → ~45 handshakes. 100 guests → ~4,950 handshakes. 10× more guests, ~100× more handshakes. It explodes fast.

```python
for i in range(n):
    for j in range(n):   # n × n = n² iterations
        ...
```

### O(2ⁿ) — Exponential time
The work **doubles** every time n grows by 1.

> A rumor in a colony: one person tells 2 people, each of them tells 2 more, every hour. After 1 hour → 2 people know. After 10 hours → ~1,000. After 30 hours → over 1 crore. Growth doubles at every step.

Classic example: naive recursive Fibonacci — each call spawns two more calls. n = 50 is already unbearable. Exponential = usually a sign to find a better algorithm.

### Speed ladder (fastest → slowest)

```
O(1)  <  O(log n)  <  O(n)  <  O(n log n)  <  O(n²)  <  O(2ⁿ)
```

---

## 4. Rules of thumb (how to simplify)

1. **Drop constants.** `O(3n)` → `O(n)`. `O(n/2)` → `O(n)`. Big-O cares about shape, not the multiplier.
2. **Drop smaller terms.** `O(n² + n + 10)` → `O(n²)`. For big n, the n² term eats everything else.
3. **Loops in sequence add.** Loop of n, then another loop of n → `O(n + n)` = `O(n)`.
4. **Loops nested multiply.** A loop of n *inside* a loop of n → `O(n × n)` = **O(n²)**.
5. **Inner loop up to `i` is still n².** `1 + 2 + 3 + ... + n = n(n+1)/2` ≈ n²/2 → still **O(n²)** (rule 1: drop the ½).

---

## 5. Best case, average case, worst case

Take **linear search**: finding my name in the class attendance register by reading names one by one from the top.

- **Best case** — my name is the first entry (surname starts with 'A'). Found in 1 step → **O(1)**.
- **Worst case** — my name is the last entry, or not there at all. Read all n names → **O(n)**.
- **Average case** — on a random day, my name is somewhere in the middle. Roughly n/2 steps → still **O(n)** (drop the ½).

**In interviews, if someone says just "the complexity", they almost always mean the worst case.** We plan for the worst — like carrying an umbrella in Mumbai monsoon even if it *might* not rain.

---

## 6. Space complexity

**Time complexity** = how many steps. **Space complexity** = how much *extra* memory the algorithm needs (not counting the input itself). This extra memory is called **auxiliary space**.

- A few variables (`sum`, `i`, `digit`) → **O(1)** space. It stays a handful of variables whether n is 10 or 10 lakh.
- Making a copy of a list of n items → **O(n)** space.

Printing does not count as stored space — once printed, it is gone from memory.

---

## 7. Complexity audit — every problem solved so far

### Day 1 — Maths problems

A key idea first: for these problems, the loop runs once **per digit**, not once per value of the number. A number `n` has about **log₁₀(n) + 1 digits** (1,082,945 has 7 digits, and log₁₀ of it is ~7). So "O(number of digits)" is written **O(log n)**. Even a 18-digit number loops only 18 times — very fast.

| Problem | Time | Space | Why |
|---|---|---|---|
| `Sum_of_first_N(n)` | O(n) | O(1) | Loop runs n times, one addition each. (Fun fact: the formula n(n+1)/2 does it in O(1).) |
| `reverse_a_number(num)` | O(log₁₀ n) | O(1) | One loop iteration per digit; a d-digit number loops d ≈ log₁₀ n times. |
| `count_digits(num)` | O(log₁₀ n) | O(1) | Same: strips one digit per iteration. |
| `palindrome_number(num)` | O(log₁₀ n) | O(1) | Reverses the number digit by digit, then one comparison. |
| `armstrong_number(num)` | O(log₁₀ n) | O(1) | Two digit-loops one after another → O(log n + log n) = O(log n). |

### Day 2–4 — Patterns 1 to 18

All patterns share one shape: an outer loop over rows and inner loop(s) over columns. The honest way to count operations = **count the characters printed**. A triangle prints 1+2+...+n = n(n+1)/2 characters → **O(n²)**. A full square prints n×n → **O(n²)**. Pyramids print spaces + stars, still ≤ 2n per row over n rows → **O(n²)**.

Space: every pattern uses only loop counters and maybe one `num`/`char` variable → **O(1)** auxiliary space.

| Problem | Time | Space | Note |
|---|---|---|---|
| `pattern01` (solid square) | O(n²) | O(1) | Exactly n×n stars. |
| `pattern02` (star triangle) | O(n²) | O(1) | 1+2+...+n = n(n+1)/2 stars. |
| `pattern03` (123 triangle) | O(n²) | O(1) | Same triangle count, prints j. |
| `pattern04` (row-number triangle) | O(n²) | O(1) | Same triangle count, prints i. |
| `pattern05` (inverted star triangle) | O(n²) | O(1) | n + (n−1) + ... + 1 — same sum, reversed. |
| `pattern06` (inverted number triangle) | O(n²) | O(1) | Same as 05 with numbers. |
| `pattern07` (star pyramid) | O(n²) | O(1) | Each row: spaces + stars ≈ 2n chars, n rows. |
| `pattern08` (inverted pyramid) | O(n²) | O(1) | Mirror of 07. |
| `pattern09` (diamond) | O(n²) | O(1) | Pyramid + inverted pyramid = O(n²) + O(n²) = O(n²). |
| `pattern10` (half diamond) | O(n²) | O(1) | 2n+1 rows, up to n stars per row. |
| `pattern11` (binary triangle) | O(n²) | O(1) | Triangle of 1s and 0s. |
| `pattern12` (number crown) | O(n²) | O(1) | Numbers + gap + numbers ≈ 2n per row. |
| `pattern13` (counting triangle) | O(n²) | O(1) | Prints 1..n(n+1)/2, one per slot. |
| `pattern14` (ABC triangle) | O(n²) | O(1) | Triangle of letters. |
| `pattern15` (inverted ABC triangle) | O(n²) | O(1) | Reversed triangle of letters. |
| `pattern16` (AA BB CC triangle) | O(n²) | O(1) | Triangle, repeated row letter. |
| `pattern17` (alpha pyramid ABA) | O(n²) | O(1) | Spaces + 2i+1 letters per row. |
| `pattern18` (reverse letter triangle) | O(n²) | O(1) | Triangle from the end letter. |

**One-line summary of the audit:** digit problems are O(log n), the counting sum is O(n), every pattern is O(n²) time — and all of them use O(1) extra space.

---

## Common mistakes

- **Confusing the value of n with the digits of n.** `reverse_a_number(1000000)` does NOT loop a million times. It loops 7 times — once per digit. Digit loops are O(log₁₀ n).
- **Thinking two loops always means n².** Two loops *one after another* is O(n + n) = O(n). Only *nested* loops multiply.
- **Thinking "inner loop only goes up to i, so it is less than n²".** 1+2+...+n = n(n+1)/2 is still O(n²) after dropping constants.
- **Reporting O(n/2) or O(2n).** Constants are always dropped: both are just O(n).
- **Counting the input as space.** Space complexity means *extra* (auxiliary) memory. Loop variables = O(1), even if the input is huge.
- **Mixing up best and worst case.** Default answer in an interview = worst case, unless asked otherwise.
- **Thinking O(log n) needs base 2 vs base 10 care.** Log bases differ only by a constant factor, and constants are dropped. O(log₂ n) = O(log₁₀ n) = O(log n).

---

## Quick recap

- Big-O counts **steps, not seconds** — same recipe, different stoves.
- Ladder: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ).
- Drop constants, drop smaller terms, nested loops multiply.
- Best/average/worst: interviews want the **worst case** by default.
- Space complexity = *extra* memory; a few variables = O(1).
- My scoreboard so far: digit tricks → O(log n), sum loop → O(n), all 18 patterns → O(n²) time and O(1) space.
