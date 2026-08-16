# Day 2 — Conditionals, Loops, and Star Patterns (Striver 1–8)

Plan for today: learn how Python makes decisions (`if`), how it repeats work (`for`, `while`), and then use loops to draw star/number patterns. Patterns look childish but they quietly build the exact muscle interviews test: turning a picture into a formula.

---

## 1. Conditionals: if / elif / else

A **conditional** is a decision point in code. "If this is true, do this. Otherwise, do that."

Think of an auto-rickshaw meter with fare slabs:

- First 1.5 km → flat ₹25
- Up to 5 km → ₹25 + ₹15 per extra km
- Beyond 5 km → higher rate per km

```python
km = 4.0

if km <= 1.5:
    fare = 25
elif km <= 5:
    fare = 25 + (km - 1.5) * 15
else:
    fare = 25 + 3.5 * 15 + (km - 5) * 18

print(fare)
```

How to read this:

- `if` — the first check. If true, its block runs and everything below is skipped.
- `elif` — short for "else if". Checked **only** when the checks above it failed.
- `else` — the catch-all. Runs when nothing above matched. No condition allowed on it.

Two rules that save you from bugs:

1. **Order matters.** Python checks top to bottom and stops at the first true condition. If you put `km <= 5` before `km <= 1.5`, a 1 km ride would wrongly enter the `km <= 5` slab — because 1 is also ≤ 5. Always put the narrowest slab first.
2. **Exactly one block runs** in an `if/elif/else` chain. Never two, never zero (as long as `else` exists).

Also note the **colon** `:` at the end of each condition line, and the **indentation** (the 4 spaces). In Python, indentation is not decoration — it is how Python knows which lines belong inside the `if`.

### `==` vs `=` — and the rest of the comparison family

`=` **stores**, `==` **asks**. `x = 5` puts 5 into the box named `x`. `x == 5` asks "is the box holding 5?" and answers `True` or `False`. Writing `if x = 5:` is a syntax error — Python refuses to even run it.

| Operator | Asks |
|---|---|
| `==` | equal? |
| `!=` | not equal? |
| `<` , `>` | strictly smaller / bigger? |
| `<=` , `>=` | smaller-or-equal / bigger-or-equal? |

Every comparison produces a `True` or `False` — and that is exactly what `if` eats.

**Chained comparison** — a Python speciality. Instead of writing `1 < x and x < 10`, write it like maths:

```python
if 1 < x < 10:
    print("x sits between 1 and 10")
```

Both ends get checked in one go. Reads exactly like the maths teacher wrote it on the board.

### Combining checks: `and`, `or`, `not`

Real decisions often need two conditions at once. Metro smart-card gate: it opens only if the card is valid **and** the balance covers the minimum fare.

```python
card_valid = True
balance = 12

if card_valid and balance >= 10:
    print("Gate opens")
```

- `and` — True only when **both** sides are True. Strict parent: homework done AND room clean, only then TV.
- `or` — True when **at least one** side is True. Priority queue at the bank: senior citizen OR differently-abled → separate line.
- `not` — flips the answer. `not True` is `False`.

The classic trap: `if x == 5 or 6:` does NOT mean "x is 5 or 6". Python reads it as `(x == 5) or (6)`, and a bare `6` counts as True on its own — so the condition is *always* true. Repeat the variable: `if x == 5 or x == 6:`.

### Nested ifs — a check inside a check

An `if` can sit inside another `if`. Airport security: the first gate checks your ticket; only after you pass that does the baggage scan even happen.

```python
has_ticket = True
bag_ok = True

if has_ticket:
    if bag_ok:
        print("Board the flight")
    else:
        print("Bag needs a re-check")
else:
    print("No entry without a ticket")
```

Each level goes 4 more spaces in. Two levels are fine; three or more usually means the logic can be flattened. Notice: if both failures gave the *same* message, `if has_ticket and bag_ok:` would do the whole job in one line — nest only when the different failures need different handling.

### One-line if — the ternary

When each branch just picks a value, Python has a one-liner:

```python
result = "Pass" if marks >= 35 else "Fail"
```

Read it left to right: "result is Pass — if marks ≥ 35 — otherwise Fail." Same as a four-line `if/else`, but for simple pick-one-of-two cases. If it stops reading like a sentence, go back to the full `if`.

### Advanced note: truthiness — what counts as False

`if` does not strictly need a `True`/`False`. Give it any value and it asks: "is this *something* or *nothing*?" The "nothing" values — called **falsy** — are:

- `0` and `0.0`
- `""` (empty string)
- `[]` (empty list — you will meet lists in a few days)
- `None`

Everything else is truthy — including `-1` and even the string `"False"`. So `if name:` is Pythonic shorthand for "if name is not empty". Handy — and it is also exactly why the `x == 5 or 6` trap above always fires: the bare `6` is truthy.

---

## 2. `for` vs `while` — when to use which

Both are **loops** — a way to repeat lines of code without copy-pasting them.

**`for` loop = T20 match.** You know before the innings starts: exactly 20 overs, not 21, not 19. When the repeat-count is known in advance, use `for`.

```python
for over in range(1, 21):   # overs 1 to 20
    print("Bowling over", over)
```

**`while` loop = filling a bucket from a tap.** You do not know how many mugs it will take. You keep pouring **while** the bucket is not full. When you only know the *stopping condition*, not the count, use `while`.

```python
bucket = 0          # litres currently in bucket
capacity = 10

while bucket < capacity:
    bucket = bucket + 3   # one mug = 3 litres
print("Full! Bucket has", bucket)
```

The `while` loop checks the condition **before** every round. The moment `bucket < capacity` becomes false, the loop ends and the line after it runs.

### Two ways to `for`-loop: by counter, or over the items

`for` can walk a counter (`range`) — or walk **directly over the items** of anything that holds items, like the letters of a string:

```python
name = "CHAI"

for i in range(len(name)):   # by counter: i = 0, 1, 2, 3
    print(i, name[i])

for letter in name:          # over items: letter = 'C', 'H', 'A', 'I'
    print(letter)
```

The second style is cleaner when you only need each item. Use the counter style when you also need the **position** (the index). Same choice comes back with lists in a few days — remember it.

**Danger with `while`:** if you forget the line that changes `bucket`, the condition never becomes false and the loop runs forever. That is called an **infinite loop**. Rule of thumb: every `while` loop must have a line inside it that pushes it towards the exit.

For today's patterns we always know the number of rows in advance, so patterns are `for`-loop territory.

---

## 3. `range()` — the counting machine

`range()` generates a sequence of numbers for a `for` loop to walk through. Three forms:

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(1, 10, 2)   # 1, 3, 5, 7, 9   (step of 2)
```

Full form: `range(start, stop, step)`.

- `start` — where counting begins (default 0).
- `stop` — where counting **ends, but is never included**.
- `step` — jump size (default 1).

### The number-one gotcha: stop is EXCLUDED

`range(5)` gives five numbers, but the number 5 itself is **not** one of them. It is like a local train announcement "this train goes up to Dadar" — meaning it stops *before* entering the next station. If you want to actually print 1 to n, you must write `range(1, n + 1)`.

### Negative step — counting down

```python
range(5, 0, -1)   # 5, 4, 3, 2, 1
```

For a countdown, `start` must be bigger than `stop`, and `step` must be negative. Common mistake: `range(5, 0)` with no step gives **nothing** — the default step is +1, and you cannot climb from 5 up to 0.

Quick self-test: how many numbers does `range(3, 10, 2)` give? Answer: 3, 5, 7, 9 → four numbers. If you got that, `range` is yours.

---

## 4. Nested loops — a loop inside a loop

**Nested** simply means one thing placed inside another. A nested loop is a loop whose body contains another loop.

Picture the seating at a shaadi: 5 rows of chairs, 4 chairs in each row. To greet every guest, you walk along row 1 chair by chair, then move to row 2 and repeat.

```python
for row in range(1, 6):          # 5 rows
    for chair in range(1, 5):    # 4 chairs per row
        print("Row", row, "Chair", chair)
```

The rule to burn into memory:

> **For every ONE step of the outer loop, the inner loop runs COMPLETELY.**

So the outer loop runs 5 times, the inner loop runs 4 times *per outer step*, giving 5 × 4 = 20 greetings. Outer loop = which row. Inner loop = movement within that row. Every pattern problem today is exactly this shape.

---

## 5. `break` vs `continue`

Two keywords that change a loop's flow from inside.

**`break` = batsman is out.** The innings (loop) ends immediately. Nothing more happens inside the loop; control jumps to the first line after the loop.

```python
for ball in range(1, 7):
    if ball == 4:
        print("OUT on ball", ball)
        break
    print("Ball", ball, "- runs scored")
# prints balls 1,2,3 then "OUT on ball 4" and stops
```

**`continue` = dot ball.** That one delivery gives nothing, but the over is not finished — skip the rest of *this* round and go straight to the next one.

```python
for ball in range(1, 7):
    if ball == 3:
        continue          # skip ball 3 entirely
    print("Ball", ball, "- counted")
# prints balls 1,2,4,5,6 — ball 3 is silently skipped
```

Memory hook: **break = out of the loop. continue = on to the next round.**

One more subtlety for interviews: in a *nested* loop, `break` only exits the **innermost** loop it sits in — the outer loop keeps going.

### `pass` — the do-nothing placeholder

`pass` means "nothing here, carry on". Python refuses an empty block — every `if`, `for`, `while` must contain at least one line. `pass` is the legal filler while the real code is still pending, like a "Work in Progress" board on a dug-up road.

```python
for ball in range(1, 7):
    if ball == 3:
        pass        # TODO: decide later what happens on ball 3
    print("Ball", ball)
# prints ALL six balls — pass changed nothing
```

Do not confuse it with `continue`: `continue` skips the rest of that round; `pass` skips nothing at all — it is pure filler.

### Advanced note: the loop's `else` clause

A `for` or `while` loop can carry an `else` block. Strange but true: it runs when the loop finished **without hitting `break`**.

```python
for seat in range(1, 6):        # searching this row for seat 10
    if seat == 10:
        print("Found it!")
        break
else:
    print("Not in this row")    # loop ended naturally → no break happened
```

Memory hook: loop-`else` = "**no break happened**". Its classic use is exactly this search-and-report-failure shape. Rarely written in real code, but interviewers love asking what it does.

---

## 6. The universal 3-step pattern recipe

Every pattern problem — all 8 today, and the harder ones later — falls to the same recipe:

1. **Outer loop = rows.** Count the rows in the picture. If there are `n` rows, write `for i in range(n)` (or `range(1, n+1)` if 1-based maths feels cleaner).
2. **Inner loop(s) = what one row contains, as a formula in `i`.** Stare at row `i` and ask: how many spaces? how many stars/numbers? Write each count as an expression using `i` and `n`. If a row has spaces *then* stars, use two inner loops one after the other.
3. **A bare `print()` at the end of each row.** Inside a row we print with `print("*", end="")` — `end=""` means "do not jump to a new line". The empty `print()` after the inner loop(s) is what moves us to the next row.

The whole game is step 2: **make a small table of row number vs count, then find the formula.**

### Worked example (my demo, not one of the 8): right-ALIGNED triangle of `#`

Target for `n = 5` (dots shown where spaces go, just for clarity):

```
....#
...##
..###
.####
#####
```

**Step 1 — rows:** 5 rows → outer loop `for i in range(1, n + 1)` with `i` = 1 to 5.

**Step 2 — the table.** For each row, count spaces and hashes straight off the picture:

| row `i` | spaces | hashes |
|---|---|---|
| 1 | 4 | 1 |
| 2 | 3 | 2 |
| 3 | 2 | 3 |
| 4 | 1 | 4 |
| 5 | 0 | 5 |

Now find formulas. Hashes column is just `i`. Spaces column: 4,3,2,1,0 against `i` = 1..5 → each is `5 - i`, i.e. **`n - i`**. Check the edges: `i=1` → 4 spaces ✓, `i=5` → 0 spaces ✓. Edges correct → formula correct.

**Step 3 — write it:**

```python
n = 5
for i in range(1, n + 1):
    for s in range(n - i):        # spaces first
        print(" ", end="")
    for h in range(i):            # then hashes
        print("#", end="")
    print()                       # row done, new line
```

That is the entire method. Picture → table → formula → code. Never try to "imagine" the formula directly; the table makes it mechanical.

---

## 7. Practice patterns 1–8 (shapes + hints only — work them out yourself)

For each: the expected output for `n = 5`, plus a nudge. Build the row table like above before touching the keyboard.

### Pattern 1 — Solid rectangle

```
*****
*****
*****
*****
*****
```

Hint: every row is identical — `n` stars each, `n` rows. Neither loop needs to depend on `i`.

### Pattern 2 — Right triangle

```
*
**
***
****
*****
```

Hint: row `i` has `i` stars (1-based). Only the inner loop's stop changes with the row. Watch out for the off-by-one if you count from 0.

### Pattern 3 — Number triangle (counting across)

```
1
12
123
1234
12345
```

Hint: same skeleton as Pattern 2, but print the **inner** loop variable instead of a star. Start the inner count from 1, not 0.

### Pattern 4 — Number triangle (row number repeated)

```
1
22
333
4444
55555
```

Hint: one-character change from Pattern 3 — print the **outer** variable. The inner loop still decides *how many*, it just no longer decides *what*.

### Pattern 5 — Inverted right triangle

```
*****
****
***
**
*
```

Hint: stars shrink as `i` grows — like overs remaining in a chase. Make the table 5,4,3,2,1 vs `i` = 1..5 and find the expression in `n` and `i`.

### Pattern 6 — Inverted number triangle

```
12345
1234
123
12
1
```

Hint: Pattern 5's shrinking length, Pattern 3's "print the counter" trick. Decide the last number of row `i` first, then remember `range` excludes its stop.

### Pattern 7 — Pyramid

```
    *
   ***
  *****
 *******
*********
```

Hint: first pattern needing **two** inner loops — spaces first, then stars. Star counts are the odd numbers 1,3,5,7,9 (what formula in `i` gives odd numbers?). Spaces shrink by one each row. No spaces needed after the stars.

### Pattern 8 — Inverted pyramid

```
*********
 *******
  *****
   ***
    *
```

Hint: Pattern 7 flipped — now spaces grow and stars shrink by 2 per row. The two formulas from Pattern 7 essentially swap directions.

---

## Common mistakes

1. **Forgetting `end=""`** — every star lands on its own line and the pattern becomes a tall stick.
2. **Forgetting the bare `print()`** after the inner loop — the whole pattern comes out as one long line.
3. **Off-by-one with `range`** — wanting 1..n but writing `range(1, n)`. Stop is excluded. Always.
4. **`range(0)` runs zero times** — a 0-based first row with inner `range(i)` prints an empty row. Check row one on paper.
5. **Wrong indentation of the final `print()`** — indent it under the inner loop and you get a newline after *every star* instead of every row. It must line up with the inner `for`.
6. **Infinite `while` loops** — no line inside moves the condition towards false.
7. **Wrong `elif` order** — a wide condition placed above a narrow one swallows all the cases.
8. **Guessing formulas instead of tabling them** — write row vs count, check both edge rows (`i = 1` and `i = n`), then code.
9. **`=` instead of `==` in a condition** — `=` stores, `==` asks. Python at least throws a syntax error for this one.
10. **`x == 5 or 6`** — always True, because the bare `6` is truthy. Repeat the variable: `x == 5 or x == 6`.
11. **`pass` when you meant `continue`** — `pass` does nothing; the rest of the round still runs.

## Quick recap

- `if / elif / else`: top-to-bottom checks, first true wins, exactly one block runs.
- `=` stores, `==` asks. Comparisons (`==`, `!=`, `<`, `<=`...) return True/False; chain them like maths: `1 < x < 10`.
- `and` = both sides true, `or` = at least one, `not` flips. Falsy values: `0`, `""`, `[]`, `None` — everything else is truthy.
- Ternary for simple picks: `x if cond else y`. Nested ifs = check inside a check; flatten with `and` when messages don't differ.
- `for` = known count (20 overs). `while` = unknown count, known stopping condition (bucket full).
- `range(start, stop, step)`: stop is **excluded**; negative step counts down (and then start > stop).
- Nested loops: one full inner-loop run per single outer-loop step. Outer = rows, inner = inside a row.
- `for` walks a counter (`range`) when you need positions, or walks items directly when you don't.
- `break` exits the loop (batsman out); `continue` skips to the next round (dot ball). `break` only exits the innermost loop. `pass` = do-nothing filler.
- Loop `else` runs only when the loop finished with **no `break`** — the search-failed reporter.
- Pattern recipe: rows → table → formula in `i` → `print(..., end="")` inside, bare `print()` per row.
- Verify every formula at the edges: first row and last row. If both match, you are done.
