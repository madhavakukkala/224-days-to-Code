[<< Day 03](../../Day-03/DSA/notes.md) | [🏠 Today's tasks](../task.md) | [Day 05 >>](../../Day-05/DSA/notes.md)

# Day 4 — Big-O: The Day I Learn to Judge Code

## So far → Today

Three days of *writing* code:

- **Day 1** — variables, input/output, and my first digit loops (reverse, count digits, palindrome, Armstrong).
- **Day 2** — loops and conditions, Striver patterns 1–8.
- **Day 3** — functions, patterns 9–15, prime check, GCD, LCM.

Today I write **zero new code**. Today I learn to *judge* code — to look at any loop and say how expensive it is before running it. This is the skill that separates coders from engineers. A coder asks "does it work?". An engineer also asks "will it still work when the input is a crore times bigger?"

And my judging material is my own week: the digit loops from Day 1, the pattern grids from Days 2–3. By tonight I will have graded every one of them myself.

---

## 1. Why count steps, not seconds?

Same recipe, different stoves.

Dal on a slow gas stove takes 40 minutes. Same dal on induction takes 20. The **recipe** never changed — only the stove did. Timing code with a stopwatch is judging the recipe by the stove. My laptop, my friend's gaming rig, and LeetCode's server are all different stoves. The language, the compiler, the OS, even what else is running in the background — all change the seconds.

So instead of seconds we count **steps**: the basic operations the code performs. One comparison, one addition, one assignment — each counts as one step, because each takes a fixed tiny amount of time no matter how big the input is. Steps depend only on the algorithm. They are the honest measurement.

## 2. What is n?

**n is the size of the input** — the thing that can grow.

- Searching a list of 1,000 numbers → n = 1000.
- Printing a pattern with 5 rows → n = 5.
- Reversing the number 98765 → careful! n is the *value*, but the loop runs once per **digit**, and 98765 has 5 digits. (Digits of n ≈ log₁₀ n. Keep this in your pocket — it matters for your Day 1 problems.)

Big-O never asks "how many steps for n = 10, exactly?" It asks a sharper question:

> **When n doubles, what happens to my step count?**

- Stays the same → O(1)
- Goes up by just one or two steps → O(log n)
- Doubles too → O(n)
- Slightly more than doubles → O(n log n)
- Becomes 4× → O(n²)
- Squares itself into oblivion → O(2ⁿ)

Big-O describes the **shape of growth**, not the exact count. That is why we write O(n) and not "3n + 7 steps".

## 3. The six shapes I must recognise on sight

### O(1) — Constant. *The UPI balance check.*

Checking your bank balance on UPI takes the same 2 seconds whether the account holds ₹500 or ₹5 crore. The work does not depend on the size of anything.

```python
def get_first(items):
    return items[0]        # one step, always — even for a list of 10 lakh items
```

### O(log n) — Logarithmic. *The phone book.*

Finding "Sharma" in a phone book: open the middle, wrong half? — throw it away. Every flip discards **half** of what remains. A 1,000-page book needs about 10 flips. A 10-lakh-page book needs about 20. The input grew 1000×; the work grew 2×.

```python
while n > 1:
    n = n // 2             # throw away half each time -> about log2(n) passes
```

`log₂(n)` just means: *how many times can I halve n before hitting 1?* Nothing scarier than that.

### O(n) — Linear. *Chai for every guest.*

Ten guests arrive, you make ten cups of chai. Twenty guests, twenty cups. Work grows in a straight line with the input.

```python
for item in items:
    do_something(item)     # body runs exactly once per item
```

### O(n log n) — Log-linear. *The exam-paper merge.*

A teacher has 100 answer sheets to sort by roll number. Trick: split into small piles, sort the tiny piles (easy), then repeatedly **merge** pairs of sorted piles. Each merge round touches all n sheets, and there are about log n rounds of merging. Total: n × log n. This is the shape of every good sorting algorithm — merge sort, and Python's own `sorted()`.

```python
items.sort()               # Python's built-in sort: O(n log n)
```

### O(n²) — Quadratic. *Wedding handshakes.*

At a wedding, every guest greets every other guest. 10 guests → about 100 greetings. 100 guests → about 10,000. Double the guests, **quadruple** the greetings. This is any loop inside a loop where both run n times.

```python
for i in range(n):
    for j in range(n):
        greet(i, j)        # n * n = n² steps
```

Your pattern grids live here — n rows × n columns of printing.

### O(2ⁿ) — Exponential. *The rumour that doubles.*

One person tells a rumour to 2 people, each tells 2 more... After 10 rounds: ~1,000 know. After 30 rounds: over 100 crore — more than the population of India. Each +1 to n **doubles** the work. Code that tries every possible subset of n items has 2ⁿ subsets to try. These solutions die before n even reaches 40.

```python
def all_subsets(items):    # every item: either IN or OUT -> 2^n combinations
    ...
```

### The speed ladder (fast → slow)

```
O(1)  <  O(log n)  <  O(n)  <  O(n log n)  <  O(n²)  <  O(2ⁿ)
```

Feel the difference at n = 1,000,000:

| Shape | Steps (roughly) | If 1 step = 1 microsecond |
|---|---|---|
| O(1) | 1 | instant |
| O(log n) | 20 | instant |
| O(n) | 10⁶ | 1 second |
| O(n log n) | 2 × 10⁷ | 20 seconds |
| O(n²) | 10¹² | **11 days** |
| O(2ⁿ) | astronomical | longer than the universe |

## 4. Famous algorithms — the reference map

Memorise this table. It is the multiplication table of DSA.

| Algorithm / operation | Big-O | One-line why |
|---|---|---|
| Access `arr[i]` by index | O(1) | Jump straight to the address |
| Binary search — **sorted data only!** | O(log n) | Halve the search space each check |
| Linear search | O(n) | May have to look at everything |
| Merge sort / Python's `sorted()` | O(n log n) | log n merge rounds × n items each |
| Compare all pairs (bubble sort, handshakes) | O(n²) | Every item vs every item |
| Generate all subsets | O(2ⁿ) | Each item doubles the possibilities |

The binary search warning deserves bold letters: on **unsorted** data binary search is not slow — it is **wrong**. Sorting is the fee you pay to unlock O(log n) searches.

## 5. The rules for computing Big-O

**Rule 1 — Drop constants.** 2n steps, 5n steps, n/2 steps — all O(n). Big-O cares whether growth is a line or a curve, not how steep the line is. O(2n) → O(n). O(500) → O(1).

**Rule 2 — Drop lower-order terms.** n² + n + 10 → O(n²). When n = 10,000, the n² part is 100,000,000 and the n part is 10,000 — a rounding error. Keep only the biggest bully.

**Rule 3 — Sequential loops ADD.** One loop *after* another: n + n = 2n → O(n). Making chai for all guests, then serving biscuits to all guests — still one pass each.

**Rule 4 — Nested loops MULTIPLY.** One loop *inside* another: n × n → O(n²). For each guest, greet every guest.

**Rule 5 — The triangle sum.** When the inner loop runs `i` times (like your patterns!):
1 + 2 + 3 + ... + n = **n(n+1)/2** ≈ n²/2 → drop the ½ (Rule 1) → **O(n²)**.
Your right triangle prints "only half" the square, but half of n² is still O(n²).

**Rule 6 — Log base doesn't matter.** log₂ n, log₁₀ n differ only by a constant multiplier (log₂ n ≈ 3.3 × log₁₀ n), and constants get dropped. So we just write O(log n). Your digit loops (`num //= 10`) and the halving loops (`n //= 2`) belong to the same family.

## 6. Best, average, worst case — the attendance register

The teacher calls roll to find one student, top to bottom.

- **Best case** — the student is roll number 1. One call. Lucky. Written with **Ω** (Omega): linear search is Ω(1).
- **Worst case** — the student is last, or absent. All n calls. Written with **O**: linear search is O(n).
- **Average case** — over many days, the student is somewhere in the middle on average → about n/2 calls → still O(n) after dropping the ½.

**Interviews and this course mean the worst case when they say Big-O**, unless stated otherwise. Why? Because a promise is only useful if it holds on the bad days. "The train is usually on time" is not a guarantee; "the train is never more than 10 minutes late" is.

Note: some algorithms don't vary at all — merge sort does its n log n work whether the data arrives sorted, reversed, or shuffled. Best = worst. Others swing wildly (quicksort behaves badly on a poorly chosen pivot).

### A gentle Omega/Theta corner (30 seconds, don't fear it)

- **O (Big-O)** = upper bound. "It takes *at most* this much." The ceiling.
- **Ω (Omega)** = lower bound. "It takes *at least* this much." The floor.
- **Θ (Theta)** = tight bound. Ceiling and floor match. "It takes *exactly* this shape."

Merge sort is Θ(n log n) — always. Linear search is O(n) and Ω(1) — depends on luck. In casual use everyone says "Big-O" for all of it; now you know the precise words.

### Amortized, in one line

Python's `list.append()` occasionally does an expensive internal resize, but averaged over many appends each one costs O(1) — that averaged cost is called **amortized O(1)**. (More on this tomorrow.)

## 7. Space complexity — the other half (preview)

Time asks "how many steps?" **Space asks "how much extra memory do I create?"** — extra, meaning beyond the input itself.

- A few loop counters and variables → **O(1)** space. (All your problems so far!)
- Building a new list of n items → **O(n)** space.
- Printed output does **not** count as stored space.

```python
def total(nums):
    s = 0                  # one variable, however long nums is -> O(1) space
    for x in nums:
        s += x
    return s

def doubled(nums):
    return [x * 2 for x in nums]   # new list of size n -> O(n) space
```

Tomorrow this becomes a full lesson. Today, just carry the question into your audit: *"what did my code create?"*

## 8. Today's real task — the self-audit

Now open your own solutions from this week and grade them yourself. **No copying complexities from the internet — the derivation is the exercise.**

### The method (run it on every problem)

1. **Find the loops.** No loop at all → almost certainly O(1).
2. **Count how often each loop body runs as n grows.** Trap to respect: a loop doing `num //= 10` runs once per **digit** — that's O(log₁₀ n), not O(n).
3. **Combine.** Loops in sequence → add. Loops nested → multiply. Inner loop bound depends on the outer counter → triangle sum → O(n²).
4. **Simplify.** Drop constants and lower terms.
5. **Space.** What did the code create that grows with input? Counters only → O(1).
6. **Write the why in one line.** If you cannot write the why, you do not know the answer yet — go back to step 1.

### Type-level hints (verify against your own code, don't assume)

- Digit-loop problems (reverse, count digits, palindrome, Armstrong) — the loop consumes one digit per pass. How many digits does a number n have?
- Sum of first N — does your loop run once per *value* up to N, or once per digit? Very different answers. And there is a famous O(1) formula — do you know it?
- Pattern grids — roughly how many characters (spaces included) does an n-row pattern print? Full square vs triangle — does the answer's Big-O differ?
- Prime check till √n — the loop bound itself is smaller than n. What's the class? (It's not one of the six! O(√n) sits between O(log n) and O(n). Big-O has more shapes than the famous six.)
- GCD by Euclid — hard one; the values shrink fast, like halving. Which family does fast shrinking suggest?

### My audit table (fill every row)

| Problem | Time | Space | Why |
|---|---|---|---|
| Sum of first N (Day 1) | | | |
| Reverse a number (Day 1) | | | |
| Count digits (Day 1) | | | |
| Palindrome number (Day 1) | | | |
| Armstrong number (Day 1) | | | |
| Pattern 1 (Day 2) | | | |
| Pattern 2 (Day 2) | | | |
| Pattern 3 (Day 2) | | | |
| Pattern 4 (Day 2) | | | |
| Pattern 5 (Day 2) | | | |
| Pattern 6 (Day 2) | | | |
| Pattern 7 (Day 2) | | | |
| Pattern 8 (Day 2) | | | |
| Pattern 9 (Day 3) | | | |
| Pattern 10 (Day 3) | | | |
| Pattern 11 (Day 3) | | | |
| Pattern 12 (Day 3) | | | |
| Pattern 13 (Day 3) | | | |
| Pattern 14 (Day 3) | | | |
| Pattern 15 (Day 3) | | | |
| Prime check (√n) (Day 3) | | | |
| GCD by Euclid (Day 3) | | | |
| LCM via GCD (Day 3) | | | |

## 9. Common mistakes

1. **"Two loops = O(n²)."** No — only *nested* loops multiply. Two loops one after the other add up to O(n).
2. **Calling a digit loop O(n).** `num //= 10` runs per digit, not per value. 1,00,00,000 has only 8 digits.
3. **Using binary search on unsorted data.** It silently returns wrong answers. Sorted first, always.
4. **Keeping the constants.** Writing O(2n) or O(n²/2) in an answer. Big-O has already thrown those away.
5. **Confusing best case with the answer.** "My linear search found it at index 0, so it's O(1)!" Big-O reports the worst day, not the lucky day.
6. **Ignoring space entirely.** Interviewers ask both. Get in the habit now: every time answer has two parts.
7. **Thinking O(1) means fast.** O(1) means *constant* — it could be a constant 5 seconds. It just doesn't get worse as n grows.

## 10. Quick recap

- Count **steps**, not seconds — steps judge the recipe, not the stove.
- **n** = input size; Big-O answers "what happens when n doubles?"
- Six shapes: O(1) UPI check, O(log n) phone book, O(n) chai for guests, O(n log n) exam-paper merge, O(n²) wedding handshakes, O(2ⁿ) rumour doubling.
- Rules: drop constants, drop lower terms, sequential adds, nested multiplies, triangle = n(n+1)/2 → O(n²), log base irrelevant.
- Big-O = worst case (ceiling), Ω = best case (floor), Θ = both match.
- Space complexity = extra memory created; your week so far is all O(1) space.
- The audit table is the day's real work. Fill every row with a *why*.

## Learn more

- GeeksforGeeks — Big-O analysis: <https://www.geeksforgeeks.org/dsa/analysis-algorithms-big-o-analysis/>
- W3Schools — Time complexity theory: <https://www.w3schools.com/dsa/dsa_timecomplexity_theory.php>
- GeeksforGeeks — Worst, average, best case: <https://www.geeksforgeeks.org/dsa/worst-average-and-best-case-analysis-of-algorithms/>
- Big-O Cheat Sheet (visual growth chart): <https://www.bigocheatsheet.com/>

---

## Tomorrow

Today was one half of the coin: **time**. Tomorrow, Day 5, is the other half — **memory**. Space complexity in full, plus Python's hidden costs: what a list *really* stores, why strings are sneakily expensive to build in a loop, and why `append` is cheap. Bring your audit table — the Space column gets an upgrade.

---

[<< Day 03](../../Day-03/DSA/notes.md) | [🏠 Today's tasks](../task.md) | [Day 05 >>](../../Day-05/DSA/notes.md)
