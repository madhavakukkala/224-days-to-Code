# Day 2 — Conditionals, Loops, and Pattern Problems (Striver Patterns 1–8)

Today's goal: get so comfortable with loops that printing star patterns feels like drawing rangoli — you see the shape in your head first, then the hand just follows.

---

## 1. Conditionals: if / elif / else

A **conditional** is how code makes a decision. "If this is true, do that."

Think of an auto-rickshaw meter:

- If distance is under 1.5 km → charge minimum fare.
- Else if distance is more → minimum fare + per-km charge.
- Else (meter broken) → argue politely.

```python
marks = 82

if marks >= 90:
    print("Topper")
elif marks >= 75:
    print("Distinction")
else:
    print("Keep practicing")
```

How Python reads this, top to bottom:

1. Check the `if` condition. True? Run its block, **skip everything else**.
2. False? Check the next `elif` (short for "else if").
3. Nothing matched? Run the `else` block.

Key points:

- Only **one** branch runs. Ever. Even if two conditions are true, the first true one wins.
- The colon `:` and the **indentation** (the spaces before a line) are not decoration. Indentation is how Python knows which lines belong to which block.
- `elif` and `else` are optional. A lone `if` is perfectly fine.
- Comparison uses `==` (is equal?), not `=` (assign a value). Mixing these up is the classic Day-1 bug.

```python
if marks = 90:   # ❌ SyntaxError — this is assignment
if marks == 90:  # ✅ comparison
```

---

## 2. Loops: doing something again and again

A **loop** repeats a block of code. Python gives you two kinds: `for` and `while`.

### for — when you KNOW how many rounds

A T20 match has exactly 20 overs. You know the count before the match starts. That is a `for` loop.

```python
for over in range(20):
    print("Bowl over number", over + 1)
```

Use `for` when the number of repetitions is known upfront: "print 5 rows", "check every item in this list", "run n times".

### while — keep going TILL a condition

Filling a bucket from a tap: you don't count mugs. You keep pouring **while the bucket is not full**.

```python
bucket = 0
while bucket < 10:      # keep going till full
    bucket += 2         # pour 2 litres each time
print("Bucket full!")
```

Use `while` when you don't know how many rounds it will take — you only know the stopping condition. Examples: "keep asking for a password till it's correct", "keep dividing n by 2 till it becomes 1".

### The danger with while: infinite loops

If the condition never becomes false, the loop never stops.

```python
bucket = 0
while bucket < 10:
    print("pouring...")   # forgot bucket += 2 → runs forever!
```

Rule of thumb: inside every `while` loop, something must change that pushes the condition toward false.

### Quick decision table

| Situation | Use |
|---|---|
| "Do this exactly n times" | `for` |
| "Go through every element of a list/string" | `for` |
| "Repeat until user types 'quit'" | `while` |
| "Keep halving till you reach 1" | `while` |

For pattern problems (today's topic), it is almost always `for`, because a pattern of size `n` has a known number of rows.

---

## 3. range() — the loop's fuel

`range()` generates a sequence of numbers for the loop to walk through.

Three forms:

```python
range(5)          # 0, 1, 2, 3, 4          (start=0, stop=5)
range(1, 6)       # 1, 2, 3, 4, 5          (start=1, stop=6)
range(1, 10, 2)   # 1, 3, 5, 7, 9          (start, stop, step=2)
range(5, 0, -1)   # 5, 4, 3, 2, 1          (counting DOWN, step=-1)
```

### The classic gotcha: stop is NOT included

`range(1, 5)` gives `1, 2, 3, 4` — it stops **before** 5.

Think of it like a local train announcement: "This train runs UP TO Dadar" — you get off before entering Dadar. So if you want numbers 1 to n **including** n, write `range(1, n + 1)`.

Memory trick: `range(a, b)` produces exactly `b - a` numbers. `range(0, 5)` → 5 numbers. `range(1, 6)` → 5 numbers.

### Counting backwards

`range(5, 0, -1)` → `5, 4, 3, 2, 1`. Same rule: stop (`0`) is not included. You'll use this in later patterns (like `pattern12` and `pattern18` in `main.py`).

---

## 4. Nested loops: a loop inside a loop

**Nested** just means "one inside another".

Picture chairs at a shaadi (wedding). There are 5 **rows** of chairs, and each row has 5 **chairs**. To place every chair:

- Outer loop → pick a row (row 1, row 2, ...).
- Inner loop → place each chair in that row.

```python
for row in range(5):          # outer: which row
    for chair in range(5):    # inner: chairs in that row
        print("🪑", end="")
    print()                   # row done, move to next line
```

Crucial fact: **for every single run of the outer loop, the inner loop runs completely, from start to finish.** Outer runs 5 times × inner runs 5 times each = 25 chairs placed.

Two small tools that make patterns possible:

- `print("*", end="")` — normally `print` jumps to a new line after printing. `end=""` says: "print and stay on the same line."
- A bare `print()` — prints nothing but jumps to the next line. This is our "row finished, next row please".

---

## 5. break vs continue

Both change a loop's normal flow, but very differently.

- **break** — exit the loop entirely, right now. Like a batsman getting out: his innings is over, he walks off.
- **continue** — skip the REST of this round only, jump to the next round. Like a dot ball: nothing happens this delivery, but the over continues with the next ball.

```python
for i in range(1, 10):
    if i == 5:
        break        # loop ends completely at 5
    print(i)         # prints 1 2 3 4

for i in range(1, 10):
    if i % 2 == 0:
        continue     # skip even numbers, keep looping
    print(i)         # prints 1 3 5 7 9
```

Note: in a nested loop, `break` only exits the **inner-most** loop it sits in, not all loops.

---

## 6. The universal pattern-problem recipe

Every star/number pattern in the world follows the same 3-step recipe:

1. **Outer loop = rows.** A pattern of size `n` usually has `n` rows. So: `for i in range(n)`.
2. **Figure out what each row contains, in terms of `i`.** Sit with a paper. Write row number vs count of stars/spaces/numbers. Find the formula. This is 90% of the work.
3. **`print()` at the end of the row** for the newline, and `end=""` inside so things stay on one line.

Example of step 2 in action (for a right triangle, n = 5):

| Row `i` (0-based) | Stars printed |
|---|---|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |

Stars = `i + 1`. Done — the inner loop is `for j in range(i + 1)`.

For pyramid-type patterns there is one more idea: **spaces come before stars**. Count spaces the same way (make the table, find the formula in `i`).

---

## 7. Patterns 1–8 at a glance (n = 5)

All of these are in `main.py`. Full line-by-line dry runs are in `notes.ipynb`.

**Pattern 1 — Solid rectangle/square.** Every row has `n` stars. Both loops run `n` times.

```
*****
*****
*****
*****
*****
```

**Pattern 2 — Right triangle of stars.** Row `i` (0-based) has `i + 1` stars. Grows by one star per row.

```
*
**
***
****
*****
```

**Pattern 3 — Number triangle, counting across.** Row `i` (1-based) prints `1 2 3 ... i`. The inner variable `j` itself gets printed.

```
1
12
123
1234
12345
```

**Pattern 4 — Number triangle, row number repeated.** Row `i` prints the digit `i`, `i` times. Same shape as Pattern 3, but we print `i` instead of `j`.

```
1
22
333
4444
55555
```

**Pattern 5 — Inverted right triangle.** Row `i` (1-based) has `n - i + 1` stars. Shrinks by one star per row.

```
*****
****
***
**
*
```

**Pattern 6 — Inverted number triangle.** Row `i` prints `1 2 ... (n - i + 1)`. Pattern 3 flipped upside down.

```
12345
1234
123
12
1
```

**Pattern 7 — Pyramid.** Each row = spaces first, then stars. Row `i` (0-based): `n - i - 1` spaces, then `2i + 1` stars (odd counts: 1, 3, 5, 7, 9). Like Diwali diyas stacked into a triangle.

```
    *
   ***
  *****
 *******
*********
```

**Pattern 8 — Inverted pyramid.** Row `i` (0-based): `i` spaces, then `2n - 2i - 1` stars (9, 7, 5, 3, 1). Pattern 7 upside down.

```
*********
 *******
  *****
   ***
    *
```

The big lesson from 7 and 8: **stars change by 2 per row** (that's where `2*i` comes from) and **spaces mirror the stars** so the shape stays centred.

---

## Common mistakes

1. **Off-by-one with `range`.** Wanting 1 to n but writing `range(1, n)` — you lose the last row. Remember: stop is not included.
2. **Forgetting `end=""`.** Without it every star lands on its own line and the pattern becomes a single skinny column.
3. **Forgetting the bare `print()`** after the inner loop — the whole pattern comes out as one long line.
4. **Wrong indentation of `print()`.** If it's inside the inner loop, you get a newline after every star. It must line up with the inner `for`, not inside it.
5. **Infinite `while` loops** — forgetting to update the variable the condition checks.
6. **Using `=` instead of `==`** inside an `if`.
7. **Skipping the paper step.** Trying to guess the inner-loop formula in your head instead of writing the row-vs-count table. Two minutes of paper saves twenty minutes of debugging.
8. **Expecting `break` to exit all loops.** It only exits the loop it is directly inside.

---

## Quick recap

- `if / elif / else` — decision making; only the first true branch runs.
- `for` = known number of rounds (overs in T20). `while` = repeat till a condition (fill the bucket).
- `range(start, stop, step)` — stop is **never** included. `range(1, n+1)` for 1 to n.
- Nested loops: outer = rows, inner = content of each row. Inner finishes fully for each outer round.
- `break` = walk off the pitch. `continue` = dot ball, next delivery please.
- Pattern recipe: outer loop for rows → table on paper → formula in `i` → `end=""` inside, `print()` after.
- Patterns 1–8: rectangle, growing triangle (stars/numbers ×2), shrinking triangle (stars/numbers), pyramid, inverted pyramid.
