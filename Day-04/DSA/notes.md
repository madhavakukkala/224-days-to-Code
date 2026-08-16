# Day 4 — Big-O: Learning to Count Steps

No new problems today. Today I learn how to *measure* code. Then I go back and measure everything I have solved so far, myself.

---

## 1. Why count steps instead of seconds?

Same recipe, different stoves.

If I cook dal on a slow gas stove it takes 40 minutes. On an induction top, 20 minutes. The *recipe* did not change — the stove did. Timing my code in seconds is like judging a recipe by the stove. My laptop, my friend's laptop, and the online judge's server are all different stoves.

So instead of seconds, we count **steps** — the basic operations the code performs (an addition, a comparison, a print). Steps depend only on the recipe (the algorithm), not the stove (the machine).

**Big-O notation** is the standard way to write "roughly how many steps, as the input gets big." The `n` in Big-O is the **input size** — how big the thing we are processing is.

## 2. What does "grows with n" mean?

The real question Big-O answers is not "how many steps for n = 10?" It is:

> **If n doubles, what happens to my step count?**

- Stays the same? That's O(1).
- Doubles too? That's O(n).
- Goes up 4×? That's O(n²).
- Barely moves? That's O(log n).

Big-O describes the *shape* of growth, not the exact count.

## 3. The six shapes I must recognise

### O(1) — constant time — *UPI balance check*

Checking your bank balance on UPI takes the same 2 seconds whether you have ₹100 or ₹1 crore. The size of the amount does not matter. Work does not depend on n at all.

```python
def get_first(items):
    return items[0]      # one step, always
```

Doubling n changes nothing.

### O(log n) — logarithmic — *phone book search*

Finding "Ramesh Kulkarni" in a printed phone book: you don't read page 1 onwards. You open the **middle**, see you're in "M", so throw away half the book. Open the middle of the remaining half. Every step **halves** the problem.

"log n" (logarithm) just means: *how many times can I halve n before reaching 1?* For n = 1000, that's about 10 halvings. For n = 1,000,000, only about 20. Huge inputs, tiny work.

```python
def halving(n):
    steps = 0
    while n > 1:
        n = n // 2       # throw away half
        steps += 1
    return steps         # ~log₂(n)
```

Any loop that divides the problem by a fixed number each round (÷2, ÷10, whatever) is logarithmic.

### O(n) — linear — *serving chai to every guest*

Ten guests at home, ten cups of chai. Twenty guests, twenty cups. Work grows in a straight line with n. Double the guests, double the work.

```python
def total(items):
    s = 0
    for x in items:      # runs once per item → n times
        s += x
    return s
```

One loop that touches each input item once = O(n).

### O(n log n) — *sorting exam papers into merge piles*

A teacher sorting 100 answer sheets by roll number: split the stack into small piles, sort each small pile, then repeatedly **merge** pairs of sorted piles into bigger sorted piles.

- Merging one full "level" of piles touches all n sheets → O(n) work per level.
- The number of levels is how many times you can halve the stack → log n levels.
- Total: n work × log n levels = **O(n log n)**.

```python
def merge_levels(n):
    work = 0
    size = n
    while size > 1:              # log n levels of piles
        for sheet in range(n):   # each level touches all n sheets
            work += 1
        size = size // 2
    return work                  # ≈ n × log n
```

A halving loop with a full n-loop inside it = O(n log n). This is the speed of good sorting algorithms (merge sort, and Python's built-in `sort()`). Slightly worse than O(n), massively better than O(n²).

### O(n²) — quadratic — *wedding handshakes*

At a wedding, every guest shakes hands with every other guest. 10 guests ≈ 100 handshakes. 100 guests ≈ 10,000 handshakes. Double the guests → **4×** the handshakes.

```python
def all_pairs(items):
    for a in items:          # n times
        for b in items:      # n times, for EACH a
            print(a, b)      # runs n × n = n² times
```

A loop **inside** a loop, both running about n times = O(n²).

### O(2ⁿ) — exponential — *the rumour*

One person hears a rumour. Every hour, everyone who knows it tells one new person. Knowers: 1 → 2 → 4 → 8 → 16... After 30 hours, over a **billion** people. Adding just one to n **doubles** the work.

The shape: every item has a yes/no choice — take it or leave it. n items → 2 × 2 × ... × 2 = 2ⁿ combinations.

```python
def count_combinations(n):
    total = 1
    for _ in range(n):
        total *= 2       # each new item DOUBLES the possibilities
    return total         # 2ⁿ combinations to try
```

Code that tries *every possible combination* (every subset, every yes/no choice) behaves like this. O(2ⁿ) is fine for n up to ~20 and hopeless beyond that. If your solution is exponential, the interviewer is waiting for a better idea.

### The pecking order

```
O(1)  <  O(log n)  <  O(n)  <  O(n log n)  <  O(n²)  <  O(2ⁿ)
fast  ────────────────────────────────────────────►  slow
```

For n = 1000: 1 step, ~10 steps, 1000 steps, ~10,000 steps, 1,000,000 steps, more-steps-than-atoms-in-your-body.

### Where the famous things sit — my reference map

When someone names an algorithm, this is the shelf it lives on:

| Task | Class | Why |
|---|---|---|
| Grab an item by index, check even/odd, use a formula | O(1) | No loop — n doesn't matter |
| **Binary search** (on *sorted* data only) | O(log n) | Throws away half each step, like the phone book |
| **Linear search**, one pass over a list | O(n) | Checks items one by one |
| Good sorting: **merge sort**, Python's built-in `sort()` | O(n log n) | log n levels × n work per level |
| Compare all pairs, simple sorts (bubble sort) | O(n²) | Every item against every item |
| Try **every subset** / brute-force every combination | O(2ⁿ) | Each item doubles the choices |

## 4. Rules of thumb for calculating Big-O

**Rule 1 — Drop constants.** O(2n), O(n/2), O(500n) are all just **O(n)**. Big-O cares about the shape of growth; a constant multiplier is just a faster or slower stove.

**Rule 2 — Drop smaller terms.** O(n² + n + 7) = **O(n²)**. When n = 10,000, the n² part is 100,000,000 and the n part is 10,000 — a rounding error. Keep only the biggest term.

**Rule 3 — Sequential loops ADD.**

```python
for i in range(n):   # n steps
    ...
for j in range(n):   # then n more steps
    ...
# total: n + n = 2n → O(n)
```

One loop *after* another: add them (then Rule 1 usually eats the constant).

**Rule 4 — Nested loops MULTIPLY.**

```python
for i in range(n):        # n times
    for j in range(n):    # n times per i
        ...
# total: n × n → O(n²)
```

A loop *inside* a loop: multiply them.

**Rule 5 — The triangle sum.** What if the inner loop runs `i` times instead of n?

```python
for i in range(n):
    for j in range(i):    # 0, then 1, then 2, ... then n-1 times
        ...
```

Total steps = 1 + 2 + 3 + ... + n = **n(n+1)/2** = n²/2 + n/2. Rule 1 drops the ½, Rule 2 drops the n/2 → still **O(n²)**. "The inner loop is shorter" does *not* save you from quadratic. Half the wedding's handshakes is still a wedding's worth of handshakes.

## 5. Best, average, worst case — the attendance register

I'm searching for my name in the college attendance register, page by page.

- **Best case:** my name is on the very first page. One step. O(1). Pure luck.
- **Average case:** my name is somewhere in the middle. About n/2 pages. Drop the constant → O(n).
- **Worst case:** my name is on the last page — or not in the register at all. All n pages. O(n).

When someone says "the complexity is X" with no qualifier, they almost always mean the **worst case** — the guarantee. Interviews want worst case unless they say otherwise. Best case is trivia; worst case is a promise.

### Advanced corner — words interviewers throw around (just recognise them)

- **Ω (Omega) and Θ (Theta).** Big-O technically means "at most this much" (an upper bound). Ω means "at least this much" (a lower bound). Θ means "exactly this shape" — both at once. When an interviewer asks for the **tight bound**, they mean Θ: the true growth shape, not a lazy over-estimate. In everyday interview talk, saying "it's O(n)" is usually already meant as the tight bound — I just need to recognise the symbols.
- **Amortized.** The average cost per operation over a long run. Python's `list.append` is **O(1) amortized** — once in a while the list must grow behind the scenes (an expensive step), but spread across many appends, each one averages out to constant. Like a yearly train pass: one big payment, tiny cost per ride.

## 6. Space complexity — the second question

**Space complexity** = how much *extra* memory my code creates, as a function of n. "Extra" (also called *auxiliary*) means: not counting the input itself.

- A fixed handful of variables (`i`, `count`, `total`) — same handful whether n is 5 or 5 million → **O(1) space**.
- Building a new list with one entry per input item → **O(n) space**.
- Printing to the screen does **not** count — printed characters are gone, not stored.

## 7. Self-audit: measuring MY OWN solved problems

Today's real task. For every problem from Day 1 to Day 3, I open my own code and derive its complexity myself. The method, step by step:

1. **Find the loops.** Loops are where all the work lives. No loop → almost certainly O(1).
2. **Ask: what makes this loop stop?** How many times does the body run as the input grows? Count it in terms of n — don't guess, count.
3. **Check how loops combine.** Side by side → add (Rule 3). One inside another → multiply (Rule 4). Inner loop depends on `i` → triangle sum (Rule 5).
4. **Simplify.** Drop constants, drop smaller terms.
5. **Then ask the space question:** what did I *create* that grows with the input? Any new list or string of size n? Or just a few loose variables?
6. **Write it down** in the table below, with a one-line "why". If I can't write the why, I don't actually know it yet.

### Hints for my problem *types* (not the answers — I derive those)

- **Digit-loop problems** (reverse, count digits, palindrome, Armstrong): the loop does `number //= 10` — it strips one digit per pass. So it runs once per **digit**, not once per value. A number n has about log₁₀(n) + 1 digits, so these are **O(number of digits) = O(log₁₀ n)** — a 15-digit number loops only ~15 times. Now check each of mine: any sequential second loop (add it), any extra memory?
- **Sum of first N with a loop:** how many times does that loop body run — per digit, or per value? Careful, this one is different from the others. And is there a famous formula that would make it O(1)?
- **Pattern problems (Striver 1–15):** a full n×n grid prints about n² characters → **O(n²) time**. Triangles print n(n+1)/2 — still O(n²) by Rule 5. Spaces count as prints too. Extra memory is usually just loop counters → **O(1) space**. Verify this holds for *each* of my 15 — especially any where I built a string before printing.

### My audit table (fill in myself)

| Problem | Time | Space | Why (one line) |
|---|---|---|---|
| Sum of first N | | | |
| Reverse a number | | | |
| Count digits | | | |
| Palindrome number | | | |
| Armstrong number | | | |
| Pattern 1 | | | |
| Pattern 2 | | | |
| Pattern 3 | | | |
| Pattern 4 | | | |
| Pattern 5 | | | |
| Pattern 6 | | | |
| Pattern 7 | | | |
| Pattern 8 | | | |
| Pattern 9 | | | |
| Pattern 10 | | | |
| Pattern 11 | | | |
| Pattern 12 | | | |
| Pattern 13 | | | |
| Pattern 14 | | | |
| Pattern 15 | | | |

## Common mistakes

- **Confusing the value of n with the size of n.** A digit-stripping loop on the number 1,000,000 runs ~7 times (7 digits), not a million times. Ask what one iteration *consumes*: one digit → O(log₁₀ n); one unit of the value → O(n).
- **Thinking two sequential loops are O(n²).** Loops one after another ADD. Only *nested* loops multiply.
- **Believing a shorter inner loop escapes O(n²).** 1 + 2 + ... + n = n(n+1)/2 is still quadratic.
- **Keeping constants and small terms.** O(3n² + 5n + 20) is just O(n²). Nobody writes the rest.
- **Reporting best case as "the" complexity.** "My search is O(1) if the item is first" — no. Default to worst case.
- **Counting the input or the printed output as space.** Space complexity is the *extra* memory the program holds. Loop counters → O(1), even if the program prints a million stars.
- **Assuming log means log base 2 only.** Halving loop → log₂, digit loop → log₁₀. Bases differ by a constant factor, and Big-O drops constants, so both are just O(log n).
- **Saying "binary search, so O(log n)" on unsorted data.** Binary search only works on **sorted** data. On an unsorted list you are stuck with linear search — O(n).

## Quick recap

- Count **steps**, not seconds — same recipe, different stoves.
- Big-O = how the step count **grows** when n grows.
- O(1) UPI balance · O(log n) phone book · O(n) chai for guests · O(n log n) merge piles of exam papers · O(n²) wedding handshakes · O(2ⁿ) rumour doubling.
- Drop constants, drop smaller terms. Sequential loops **add**, nested loops **multiply**, 1+2+...+n = n(n+1)/2 → O(n²).
- Best / average / worst = first page / middle / last page of the attendance register. Interviews mean **worst** case.
- Reference map: binary search (sorted!) → log n · linear search → n · good sorts → n log n · all pairs → n² · all subsets → 2ⁿ.
- Advanced words: **Θ (tight bound)** = the exact growth shape; **amortized** = average over many operations (`list.append` → O(1) amortized).
- Space = extra memory that grows with n. Loose variables → O(1).
- The two audit questions, forever: **how many times does each loop body run?** and **what did I create that grows with n?**
