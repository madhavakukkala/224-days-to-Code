# Day 2 — Control Flow: Teaching the Program to Decide and Repeat

**Yesterday → Today:** Yesterday you learned to store data in labelled dabbas (variables) and to talk to the program (`input()` / `print()`). But the program was a straight road — line 1, line 2, line 3, done. Today it learns two superpowers: to **DECIDE** (if/elif/else) and to **REPEAT** (while/for). Every program you'll ever write is just these two powers mixed with yesterday's storage.

---

## 1. `if` — the program's first decision

Think of a traffic signal. The rule in your head is: *if the light is green, go*. Python writes that thought almost word for word:

```python
light = "green"
if light == "green":
    print("Go!")
```

Three things to notice:

- The condition ends with a colon `:` — Python's way of saying "here comes the action".
- The action line is pushed 4 spaces in. This **indentation** is not decoration — it's how Python knows which lines belong to the `if`. Forget it and you get `IndentationError`.
- Everything indented under the `if` runs only when the condition is `True`. The moment you un-indent, you're back outside the `if`.

```python
marks = 82
if marks >= 35:
    print("Pass!")           # runs only if condition is True
    print("Party tonight")   # also inside the if
print("Result declared")     # NOT indented — runs always
```

## 2. `else` — the "otherwise" plan

```python
marks = 30
if marks >= 35:
    print("Pass!")
else:
    print("Supplementary exam in July")
```

Exactly one of the two blocks runs. Never both, never neither.

## 3. `elif` — many doors, first open one wins

`elif` = "else if". Use it when there are more than two possibilities — like grading:

```python
marks = 78
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

### Order matters — a lot

Python checks conditions **top to bottom** and runs the **first** one that is `True`, then skips the rest completely. Watch this trap:

```python
marks = 95
if marks >= 60:
    print("Grade C")     # 95 >= 60 is True, so THIS runs!
elif marks >= 90:
    print("Grade A")     # never even checked
```

A topper gets Grade C because the loose condition came first. Rule of thumb: **put the strictest condition first**. It's like security check at the airport — VIP gate check happens before the general gate, otherwise VIPs end up in the general queue.

## 4. Nested `if` — a decision inside a decision

You can put an `if` inside another `if`. Like entering a movie theatre: first the guard checks your ticket, and only *then* checks if you have outside food.

```python
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Watch any movie")
    else:
        print("U/A movies only")
else:
    print("Ticket counter is that way")
```

Each level goes 4 more spaces in. Two or three levels is fine; more than that and the code becomes a ladder nobody wants to climb — we'll fix that with `and` in a minute.

## 5. Comparison operators — the questions you can ask

| Operator | Question it asks | Example (`a=7, b=3`) |
|---|---|---|
| `==` | are they equal? | `a == b` → `False` |
| `!=` | are they NOT equal? | `a != b` → `True` |
| `>` | left bigger? | `a > b` → `True` |
| `<` | left smaller? | `a < b` → `False` |
| `>=` | bigger or equal? | `a >= 7` → `True` |
| `<=` | smaller or equal? | `b <= 3` → `True` |

### `=` vs `==` — the classic beginner burn

- `=` **assigns** — "put this value in the dabba": `x = 5`
- `==` **compares** — "is the dabba's value 5?": `x == 5`

```python
x = 5        # assignment: x is now 5
x == 5       # comparison: True
if x = 5:    # SyntaxError! Python refuses to let you assign inside an if
```

Good news: Python catches this mistake for you with an error instead of silently doing the wrong thing.

### Chained comparisons — Python's gift

Maths teachers write `0 <= marks <= 100`. Most languages force you to split that. Python lets you write it as-is:

```python
marks = 82
if 0 <= marks <= 100:
    print("Valid marks")
```

This means `0 <= marks` **and** `marks <= 100`. Clean.

## 6. Logical operators — combining questions

| Operator | True when... | Kitchen version |
|---|---|---|
| `and` | BOTH sides are True | chai needs milk **and** tea powder |
| `or` | AT LEAST one side is True | payment works by cash **or** UPI |
| `not` | flips True↔False | `not raining` = it's dry |

```python
age = 20
has_id = True
if age >= 18 and has_id:
    print("Voter slip issued")

day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

is_raining = False
if not is_raining:
    print("Match is on")
```

`and`/`or` also let you flatten yesterday's nested movie-theatre example:

```python
if has_ticket and age >= 18:
    print("Watch any movie")
```

### ⚠️ The `x == 5 or 6` trap

This looks right and is completely wrong:

```python
x = 100
if x == 5 or 6:          # WRONG — always True!
    print("runs every single time")
```

Python reads it as `(x == 5) or (6)`. And a bare `6` is truthy (next section), so the whole thing is always `True`. You must repeat the comparison:

```python
if x == 5 or x == 6:     # correct
```

In English "if x is 5 or 6" makes sense. Python is not English. Each side of `or` must be a complete question.

## 7. Truthiness — everything has a True/False shadow

Put any value inside an `if` and Python converts it to `True` or `False`:

- **Falsy** (act like `False`): `0`, `0.0`, `""` (empty string), `None`, and empty containers like `[]`
- **Truthy** (act like `True`): everything else — `1`, `-5`, `"hello"`, even `"False"` (it's a non-empty string!)

```python
name = input("Your name: ")
if name:                      # same as: if name != ""
    print("Hello,", name)
else:
    print("You typed nothing!")
```

Like a dabba check — an empty dabba is "nothing there" (falsy), a dabba with even one grain is "something there" (truthy).

## 8. Ternary — one-line if/else

For tiny decisions, Python has a shorthand:

```python
marks = 40
result = "Pass" if marks >= 35 else "Fail"
print(result)    # Pass
```

Read it as English: *result is "Pass" if marks are enough, else "Fail"*. Use it only when it fits on one readable line. If it needs scrolling, go back to the full `if/else`.

---

## 9. `while` — repeat as long as a condition holds

`while` is a chowkidar (watchman) at a gate. Before every round, he checks the condition. Condition `True`? One more round. `False`? Duty over.

```python
count = 1
while count <= 5:
    print("Round", count)
    count = count + 1     # remember from yesterday: same as count += 1
print("Done")
```

```
Round 1
Round 2
Round 3
Round 4
Round 5
Done
```

Every `while` loop has 3 mandatory pieces:

1. **Setup** before the loop: `count = 1`
2. **Condition** checked each round: `count <= 5`
3. **Update** inside the loop: `count += 1`

### Infinite loops — forget the update, run forever

```python
count = 1
while count <= 5:
    print("Round", count)
    # forgot count += 1  →  count is 1 forever  →  loop never ends!
```

Your terminal will keep printing until you press **Ctrl+C** (the emergency brake — remember this shortcut). Every programmer writes an accidental infinite loop in week one. Now you know the cure: check that something inside the loop pushes the condition towards `False`.

Sometimes an infinite loop is *intentional* — `while True:` with a `break` inside is how ATMs and menus run forever until you choose "Exit". More on `break` below.

## 10. `for` + `range()` — repeat a known number of times

When you know *how many* times to repeat, `for` is your friend:

```python
for i in range(5):
    print("Namaste", i)
```

```
Namaste 0
Namaste 1
Namaste 2
Namaste 3
Namaste 4
```

### `range()` — the number machine

`range(start, stop, step)` generates numbers **from `start`, up to but NOT including `stop`, jumping by `step`.**

| Call | Produces | Note |
|---|---|---|
| `range(5)` | 0 1 2 3 4 | start defaults to 0; **5 excluded** |
| `range(1, 6)` | 1 2 3 4 5 | start at 1, stop before 6 |
| `range(2, 11, 2)` | 2 4 6 8 10 | step 2 — even numbers |
| `range(5, 0, -1)` | 5 4 3 2 1 | negative step counts DOWN |
| `range(5, 0)` | *(nothing!)* | empty — can't go 5→0 with step +1 |

The stop-is-excluded rule trips everyone. Think of it like floors in a lift display "0 to 4" — five floors, but you never reach floor 5. Want 1 to n? Write `range(1, n + 1)`.

The empty range is a silent bug: `range(5, 0)` doesn't crash — the loop body just never runs, and you sit wondering why nothing printed. Counting down? You **must** give step `-1`.

### Counter vs items — two ways to loop

`for` can walk through any sequence directly — even a string:

```python
for ch in "chai":
    print(ch)          # c, h, a, i — one letter per round
```

So you have two styles:

```python
menu = "dosa"
for ch in menu:              # style 1: give me the ITEMS
    print(ch)

for i in range(len(menu)):   # style 2: give me the POSITIONS (counter)
    print(i, menu[i])        # 0 d, 1 o, 2 s, 3 a
```

Use style 1 when you only need the items. Use style 2 when you need the position number too (like "3rd letter"). Star patterns today are pure counter work — style 2 territory.

## 11. Nested loops — a loop inside a loop

Cricket: a match has overs, each over has 6 balls. Outer loop = overs, inner loop = balls. **The inner loop finishes ALL its rounds for every single round of the outer loop.**

```python
for over in range(1, 3):          # 2 overs
    for ball in range(1, 7):      # 6 balls each
        print("Over", over, "Ball", ball)
```

That prints 2 × 6 = 12 lines. The over changes slowly; the ball spins fast. This slow-outer / fast-inner rhythm is the engine behind every star pattern you'll draw today.

## 12. `break`, `continue`, `pass` — the loop's remote control

**`break` — stop the whole loop immediately.** You're searching a queue of dabbas for the one with sugar; the moment you find it, you stop opening the rest.

```python
for i in range(1, 11):
    if i == 4:
        break
    print(i)          # 1 2 3 — the loop DIES at 4
```

**`continue` — skip this round, jump to the next.** Like a conductor skipping seat 4 because it's empty, but continuing to check seats 5, 6, 7...

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)          # 1 2 4 5 — only 3 is skipped
```

**`pass` — do nothing, but legally.** Python refuses an empty block. `pass` is a placeholder — "I'll write this later":

```python
for i in range(5):
    pass              # loop runs 5 times doing nothing; no error
```

Quick memory hook: `break` = leave the queue, `continue` = skip your turn but stay in the queue, `pass` = stand quietly doing nothing.

## 13. Loop `else` — the loop's report card (advanced)

Surprise: loops can have an `else` too. The `else` block runs **only if the loop finished all rounds without hitting `break`.**

```python
for i in range(2, 7):
    if 49 % i == 0:               # remember % from yesterday — remainder
        print("Divisible by", i)
        break
else:
    print("No divisor found")     # runs only if no break happened
```

For 49, the loop finds 7 and breaks — `else` stays silent. For 47, no divisor is found, the loop completes, and `else` fires. Think of it as: `break` = search succeeded, `else` = search came up empty. Rarely needed, but interviewers love asking about it.

## 14. `for` vs `while` — which one when?

| Use `for` when... | Use `while` when... |
|---|---|
| You KNOW how many rounds: "print 5 rows", "check each letter" | You DON'T know: "keep asking until PIN is correct" |
| Walking through a sequence | Waiting for a condition to change |
| Star patterns, tables, fixed counts | Menus, retries, games, `while True` + `break` |

Simple test: can you finish the sentence "repeat ___ times" with a number? Use `for`. If the sentence is "repeat until ___", use `while`.

---

## 15. The universal 3-step pattern recipe

Every star/number pattern in existence surrenders to the same recipe:

1. **Outer loop = rows.** Count the rows in the target picture. That's your `for row in range(...)`.
2. **Inner loop(s) = one row's contents.** Stare at ONE row and ask: how many spaces? how many stars/numbers? *as a formula of the row number*. Make a small table on paper: row 1 → ?, row 2 → ?, row 3 → ? until the formula jumps out.
3. **Newline after each row.** Print the row's pieces with `end=""` (remember `end` from yesterday — it stops `print` from jumping to a new line), then one empty `print()` to close the row.

### One fully-worked demo: the Hollow Square (NOT one of your 8 — those you solve yourself)

Target for n = 5:

```
* * * * *
*       *
*       *
*       *
* * * * *
```

**Step 1 — rows:** 5 rows → outer loop `for row in range(1, 6)`.

**Step 2 — one row's contents:** make the paper table.

| row | what's in it |
|---|---|
| 1 | 5 stars (top border) |
| 2, 3, 4 | star, 3 gaps, star |
| 5 | 5 stars (bottom border) |

The rule per cell: print `*` if we're on the **first/last row** OR the **first/last column** — otherwise print a gap. That's an `if` with `or` — today's two topics shaking hands!

**Step 3 — code it:**

```python
n = 5
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row == 1 or row == n or col == 1 or col == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()    # close the row
```

Note how we wrote `row == 1 or row == n` — NOT `row == 1 or n` (Section 6's trap, dodged!).

Every pattern below is this same recipe with a different Step-2 table. Do the paper table first, every time. Code without the table is guessing.

---

## 16. Striver Patterns 1–8 — shapes + hints only

Attempt each in `main.py` before peeking at hints. All shapes shown for **n = 5**. No solutions here — the struggle is the workout.

### Pattern 1 — Solid Rectangle

```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

*Hint:* every row is identical. Outer loop rows, inner loop columns, star every time. The "hello world" of nested loops.

### Pattern 2 — Right Triangle

```
*
* *
* * *
* * * *
* * * * *
```

*Hint:* paper table — row 1 has 1 star, row 2 has 2... row `i` has `?` stars. The inner loop's `range` depends on the outer variable.

### Pattern 3 — Number Triangle (counting across)

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

*Hint:* same skeleton as Pattern 2, but instead of `*`, print the inner loop's own counter. Where should the inner counter start for that to work?

### Pattern 4 — Number Triangle (row number repeated)

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

*Hint:* again Pattern 2's skeleton — but now print the OUTER variable, `i` times. One-character change from Pattern 3. Feel the difference.

### Pattern 5 — Inverted Right Triangle

```
* * * * *
* * * *
* * *
* *
*
```

*Hint:* row 1 → 5 stars, row 2 → 4 stars... row `i` → `?` stars. Either make the inner range shrink (`n - i + 1` style) or run the outer loop backwards with a negative step (Section 10!).

### Pattern 6 — Inverted Number Triangle

```
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

*Hint:* Pattern 5's shrinking skeleton + Pattern 3's counting trick. Two solved ideas glued together — that's how all DSA works.

### Pattern 7 — Pyramid

```
    *
   * *
  * * *
 * * * *
* * * * *
```

*Hint:* the first row with spaces! Each row = (some spaces) + (some stars). Paper table with TWO columns now: row 1 → 4 spaces + 1 star; row 2 → 3 spaces + 2 stars... Find both formulas in terms of `i`. Two inner loops back-to-back, then the newline.

### Pattern 8 — Inverted Pyramid

```
* * * * *
 * * * *
  * * *
   * *
    *
```

*Hint:* Pattern 7 upside down — spaces grow while stars shrink. If your Pattern 7 table was right, flip the two formulas.

---

## 17. Common mistakes today

1. **`=` instead of `==`** in a condition — Python throws `SyntaxError`, read the arrow it points at.
2. **`if x == 5 or 6:`** — always True. Repeat the full comparison: `x == 5 or x == 6`.
3. **Missing colon `:`** after `if` / `elif` / `else` / `while` / `for` — instant `SyntaxError`.
4. **Wrong indentation** — the line you *thought* was inside the loop is actually outside. Python only knows what your spaces tell it.
5. **`elif` order wrong** — loose condition first eats all cases; strictest condition goes first.
6. **Off-by-one with `range`** — `range(5)` is 0–4, not 1–5. Want 1 to n? `range(1, n + 1)`.
7. **Empty range when counting down** — `range(5, 0)` runs zero times; you need `range(5, 0, -1)`.
8. **Forgetting the update in `while`** — infinite loop. Ctrl+C, add the `+= 1`, breathe.
9. **Forgetting `print()` after the inner loop** in patterns — everything smashes onto one line.
10. **Coding patterns without the paper table** — five minutes on paper saves thirty on screen.

## 18. Quick recap

- `if` / `elif` / `else` — decide; first True wins, so order strictest-first.
- `==` compares, `=` assigns. Chain freely: `0 <= x <= 100`.
- `and` / `or` / `not` combine questions; each side of `or` must be complete.
- Falsy: `0`, `""`, `None`, empty things. Everything else truthy.
- Ternary: `"Pass" if marks >= 35 else "Fail"`.
- `while` = repeat until condition fails (setup, condition, update — or infinite loop).
- `for` + `range(start, stop, step)` = repeat a known count; stop is excluded.
- Nested loops: outer slow, inner fast — the pattern engine.
- `break` leaves, `continue` skips, `pass` does nothing; loop-`else` runs only without `break`.
- Patterns: rows → table → formulas → code. Always in that order.

## 19. Learn more

- [W3Schools — Python Conditions](https://www.w3schools.com/python/python_conditions.asp)
- [W3Schools — While Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [W3Schools — For Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [GeeksforGeeks — Loops in Python](https://www.geeksforgeeks.org/python/loops-in-python/)

---

**Tomorrow:** your code is getting longer — and you're already copy-pasting bits of it. Day 3 fixes that: **functions** — packing reusable logic into a named box you can call again and again. Write once, use forever.
