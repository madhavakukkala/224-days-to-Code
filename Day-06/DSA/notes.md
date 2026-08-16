# Day 6 — Lists: Our First True Data Structure

## Yesterday → Today

All week we handled values **one at a time**. One `age`, one `price`, one `marks`. Five students meant five separate variables — `m1, m2, m3, m4, m5`. Ugly. Imagine 500 students.

Today we finally hold **many values in one variable**: the **list**. This is our first true data structure — a container we can grow, shrink, search and reorder.

And here is the beautiful part. Yesterday's Big-O lessons were not random theory. They were preparation:

- Yesterday: "shifting things over costs O(n)" → today: `insert(0, x)` and `pop(0)` cost **O(n)** for exactly that reason.
- Yesterday: "checking items one by one costs O(n)" → today: `x in my_list`, `remove()`, `index()` all cost **O(n)** for exactly that reason.

Same costs, now with real code attached. Let's go.

---

## 1. What is a List?

A list is like a **train** — the Chennai Express. One train, many coaches. Coaches are attached in a fixed **order**, each coach has a **number**, and coaches can be added or removed at the yard.

```python
marks = [72, 85, 90, 66, 78]
```

One variable name (`marks`), five values inside, in a fixed order. Three properties to remember:

1. **Ordered** — the sequence stays as you wrote it. `[1, 2]` is not the same list as `[2, 1]`.
2. **Changeable (mutable)** — you can modify, add, remove items after creation.
3. **Duplicates allowed** — `[70, 70, 70]` is a perfectly fine list.

---

## 2. Creating Lists — Four Ways

```python
# 1. Literal — the everyday way
fruits = ["mango", "banana", "guava"]

# 2. Empty list, fill it later
basket = []

# 3. list() constructor — converts other things into a list
letters = list("abc")        # ['a', 'b', 'c']

# 4. list(range()) — quick number sequences
nums = list(range(5))        # [0, 1, 2, 3, 4]
evens = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]
```

A list can even mix types:

```python
mixed = ["Ravi", 21, 5.8, True]
```

Python allows this. But in DSA practice, keep one type per list — mixed lists are where bugs hide.

`type(fruits)` says `<class 'list'>`. It's a proper type of its own, like `int` and `str` were.

---

## 3. Indexing — Coach Numbers

Every item has a position number called an **index**. Counting starts at **0**, not 1.

```python
fruits = ["mango", "banana", "guava"]
#  index:     0         1        2

fruits[0]   # 'mango'  — first coach
fruits[2]   # 'guava'  — last coach
```

Why 0? Think of the index as "how many coaches to walk PAST from the engine". The first coach needs zero walking. That mental model never fails.

### Negative indexing — counting from the guard's cabin

Python lets you count from the back too. `-1` is the last item, `-2` is second last.

```python
fruits[-1]  # 'guava'
fruits[-2]  # 'banana'
```

This is a gift. To get the last item you write `fruits[-1]`, not `fruits[len(fruits) - 1]`.

### IndexError — walking off the train

Ask for a coach that doesn't exist and Python crashes:

```python
fruits[3]    # IndexError: list index out of range
fruits[-4]   # IndexError too
```

The highest valid index is always `len(list) - 1`. Burn that into memory — "off by one" is the most common bug in all of programming.

### len() — how long is the train?

```python
len(fruits)   # 3
```

`len()` is **O(1)** — Python keeps the count stored, it never walks the train to count coaches.

---

## 4. Slicing — Detaching a Set of Coaches

Slicing cuts out a **portion** of the list and gives you a **new list**.

```python
nums = [10, 20, 30, 40, 50]

nums[1:4]    # [20, 30, 40]  — index 1 up to (NOT including) 4
```

The rule: **start is included, end is excluded**. Like a railway ticket "valid from station 1 up to station 4" — you get down BEFORE station 4.

### The defaults

Leave a side empty, Python fills it in:

```python
nums[:3]    # [10, 20, 30]   — from the beginning
nums[2:]    # [30, 40, 50]   — till the end
nums[:]     # [10, 20, 30, 40, 50] — the whole list (a COPY — big deal, see section 12)
```

### The step

A third number = "take every k-th item":

```python
nums[::2]    # [10, 30, 50]  — every 2nd item
nums[1::2]   # [20, 40]      — every 2nd, starting at index 1
```

### The famous reversal

Step of `-1` walks backwards:

```python
nums[::-1]   # [50, 40, 30, 20, 10]  — reversed COPY
```

`[::-1]` is a Python party trick worth memorising. (But note — it builds a new list: O(n) extra space. Remember yesterday's auxiliary-space lesson.)

### Slicing is forgiving

Indexing out of range crashes. Slicing out of range does NOT:

```python
nums[2:100]   # [30, 40, 50] — no error, just gives what exists
nums[50:60]   # []           — empty list, still no error
```

Index = strict ticket checker. Slice = friendly conductor who says "take whatever seats exist".

---

## 5. Mutation — Lists Change In Place

Day 2 flashback: strings are **immutable**. You cannot do `s[0] = "X"`. Lists are the opposite:

```python
marks = [72, 85, 90]
marks[1] = 99          # works! list is now [72, 99, 90]

name = "ravi"
name[0] = "R"          # TypeError — strings never change in place
```

This is THE dividing line. String "changes" always create a new string. List changes edit the same list in memory. This difference is exactly why aliasing (section 12) bites people with lists but not with strings.

---

## 6. The Method Toolbox — With Price Tags

Every operation has a cost. Recall the train analogy: attaching a coach at the **back** is easy; inserting one in the **middle** means detaching and re-attaching everything after it.

### Adding

```python
a = [1, 2, 3]
a.append(4)        # [1, 2, 3, 4]     — add at the END       → O(1)
a.insert(0, 99)    # [99, 1, 2, 3, 4] — add at a position    → O(n)
```

`insert(0, x)` shifts EVERY existing item one step right. That's yesterday's shifting lesson, live.

### extend() vs append(list) — a classic trap

```python
a = [1, 2]
a.extend([3, 4])   # [1, 2, 3, 4]       — items joined the train
b = [1, 2]
b.append([3, 4])   # [1, 2, [3, 4]]     — the WHOLE LIST became one item!
```

`extend` = attach each new coach to the train. `append([...])` = load a whole small train onto one flatbed coach. Length of `a` becomes 4; length of `b` becomes 3.

### Removing

```python
a = [10, 20, 30, 40]
a.pop()        # removes and RETURNS 40  → O(1)  (last item, nothing shifts)
a.pop(0)       # removes and returns 10  → O(n)  (everything shifts left)
a.remove(20)   # removes first matching VALUE 20 → O(n) (search + shift)
a.clear()      # []  — empties the list
```

- `pop` works by **index** and gives the item back to you.
- `remove` works by **value** and returns nothing. If the value is absent → `ValueError`.
- `del a[1]` also deletes by index (statement, not method).

### Sorting — and the trap that gets everyone

```python
a = [3, 1, 2]
a.sort()           # a is now [1, 2, 3]  — sorted IN PLACE, returns None
b = sorted(a)      # NEW sorted list, original untouched
```

The trap:

```python
a = [3, 1, 2]
a = a.sort()       # a is now None!!  😱
```

`sort()` returns `None` because it modifies in place — it has nothing to give back. Assigning that `None` to `a` destroys your list. Rule: **`a.sort()` alone, or `b = sorted(a)`. Never `a = a.sort()`.**

Extras: `a.sort(reverse=True)` for descending. Sorting costs **O(n log n)** — remember that tier from Day 4's Big-O ladder.

### Reversing

```python
a.reverse()    # in place, returns None (same trap as sort!)
b = a[::-1]    # new reversed copy, original safe
```

Choose by intent: modify the original → `reverse()`. Keep the original → `[::-1]`.

### Searching and counting

```python
a = [10, 20, 30, 20]
a.index(20)    # 1  — index of FIRST match     → O(n); ValueError if absent
a.count(20)    # 2  — how many times it occurs → O(n)
```

---

## 7. in / not in — Membership Check

```python
if 30 in a:
    print("found")
if 99 not in a:
    print("missing")
```

Clean to read, but never forget the price: Python walks the list item by item — **O(n)**. Using `x in big_list` inside a loop over that same list quietly builds an O(n²) program. (Later in the course, sets will do this check in O(1). Teaser!)

---

## 8. + and * on Lists

```python
[1, 2] + [3, 4]    # [1, 2, 3, 4]  — new joined list
[0] * 5            # [0, 0, 0, 0, 0]  — great for initialising
```

### The `[[0]] * 3` trap

```python
grid = [[0]] * 3       # [[0], [0], [0]]  ... looks fine
grid[0][0] = 9
print(grid)            # [[9], [9], [9]]  😱 ALL rows changed!
```

`*` did not photocopy the inner list — it wrote the **same inner list's address** three times. Three name-plates on one house. The safe way to build a grid:

```python
grid = [[0] for _ in range(3)]   # three SEPARATE inner lists
```

This trap makes full sense after section 12 (aliasing). Park it here, we'll return.

---

## 9. Looping Over Lists

### Way 1 — for item (when you only need values)

```python
for fruit in fruits:
    print(fruit)
```

### Way 2 — range(len()) (when you need to MODIFY by index)

```python
for i in range(len(marks)):
    marks[i] += 5      # 5 grace marks for everyone
```

### Way 3 — enumerate (when you need index AND value)

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

Why is `enumerate` better than `range(len())` for reading? Compare:

```python
for i in range(len(fruits)):
    print(i, fruits[i])          # clunky, easy to typo fruits[j]
for i, fruit in enumerate(fruits):
    print(i, fruit)              # both handed to you, no lookup
```

Pythonic rule of thumb: values only → plain `for`. Index needed to write → `range(len())`. Index needed to read → `enumerate`.

### Bonus — zip (walking two lists together)

```python
names = ["Ravi", "Priya", "Amit"]
marks = [72, 85, 90]
for name, mark in zip(names, marks):
    print(name, mark)
```

Like two parallel train tracks — `zip` pairs coach 0 with coach 0, coach 1 with coach 1... It stops at the shorter list.

---

## 10. min, max, sum — Free Built-ins

```python
marks = [72, 85, 90, 66]
min(marks)   # 66
max(marks)   # 90
sum(marks)   # 313
sum(marks) / len(marks)   # average: 78.25
```

Each is **O(n)** — they walk the whole list once. Convenient, but in today's practice problems you will build min/max **yourself**, because interviewers want to see the loop, not the shortcut.

---

## 11. Copy Levels — Aliasing vs Copy vs Deepcopy

The most important section today. This bug will bite you at least once in your career; let it bite you today, cheaply.

### Aliasing — two name-plates, one tiffin

```python
a = [1, 2, 3]
b = a          # NOT a copy! b is a second NAME for the SAME list
b.append(4)
print(a)       # [1, 2, 3, 4]  — a changed too!
```

Think of a **tiffin box** with two name stickers on it — "Ravi" and "Ravi's mom's dabba". Two names, ONE box. Whoever opens it eats the same food. `b = a` copies the **address**, not the contents.

Check with `a is b` → `True` means same box.

### Shallow copy — a new tiffin (top layer only)

Three equivalent ways:

```python
b = a.copy()
b = a[:]
b = list(a)
```

Now `b` is a genuinely new list — appending to `b` leaves `a` alone. For flat lists of numbers/strings, this is all you ever need.

### The nested catch — and deepcopy

A shallow copy photocopies the **outer** tiffin but the **inner** containers are still shared:

```python
students = [["Ravi", 72], ["Priya", 85]]
copy1 = students.copy()
copy1[0][1] = 99
print(students)      # [['Ravi', 99], ['Priya', 85]]  — original changed! 😱
```

New outer tiffin, but the inner dabbas inside it are the SAME ones. To photocopy every level:

```python
import copy
copy2 = copy.deepcopy(students)
copy2[0][1] = 40
print(students)      # untouched now
```

### One-table summary

| Level | Code | Outer list | Inner lists |
|---|---|---|---|
| Alias | `b = a` | shared | shared |
| Shallow | `b = a.copy()` / `a[:]` | new | shared |
| Deep | `copy.deepcopy(a)` | new | new |

And now the `[[0]] * 3` trap from section 8 makes sense: `*` created three aliases of one inner list.

---

## 12. List Comprehensions — Lists in One Line

The pattern "make an empty list, loop, append" is so common Python gave it a shortcut.

### Basic form

```python
# Long way
squares = []
for x in range(5):
    squares.append(x * x)

# Comprehension
squares = [x * x for x in range(5)]    # [0, 1, 4, 9, 16]
```

Read it aloud: "x squared, **for** each x **in** range 5". It reads like English.

### Filter — if at the END

```python
evens = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]
```

End-`if` = a **gatekeeper**. Items failing the test are dropped entirely.

### Choose — if-else at the FRONT

```python
labels = ["pass" if m >= 40 else "fail" for m in marks]
```

Front `if-else` = every item **stays**, but you choose what it becomes. Two different jobs, two different positions:

- **End if** → filters items OUT (no `else` allowed there).
- **Front if-else** → transforms every item (must have `else`).

### One nested example

```python
pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

Left-to-right = outer loop then inner loop, same as writing two nested `for`s.

### When NOT to use them

- Logic needs more than one line (multiple steps, try/except) → normal loop.
- Nested three levels deep → unreadable, use a loop.
- You are only doing a side effect (printing) and don't need the list → normal loop.

A comprehension should be readable in one breath. If you need two breaths, write the loop.

---

## 13. Bonus — Unpacking

```python
a, b = [10, 20]          # a=10, b=20
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]
*init, last = [1, 2, 3, 4]    # init=[1, 2, 3], last=4
a, b = b, a              # the famous Python swap — no temp variable!
```

That last one — `a, b = b, a` — is a strong hint for today's first practice problem. 😉

---

## 14. Today's Practice Problems — Hints Only

Attempt in `main.py` FIRST. Hints below, solutions never.

### Problem 1 — Reverse an array IN PLACE

"In place" means: no new list. O(1) auxiliary space (yesterday's lesson!). `arr[::-1]` creates a new list — that's cheating here.

- **Hint 1:** Two pointers — one finger on the first item, one on the last.
- **Hint 2:** Swap what's under the fingers, then move both fingers toward the middle.
- **Hint 3:** When do the fingers stop? Think about when they meet or cross.
- **Hint 4:** Python's swap `arr[i], arr[j] = arr[j], arr[i]` needs no temp variable.

### Problem 2 — Find min and max (no built-ins)

- **Hint 1:** Single pass, "best so far". Assume the first item is BOTH the smallest and largest seen so far.
- **Hint 2:** Walk the rest of the list once; every item challenges the current champions.
- **Hint 3:** One loop can update both min and max together. O(n) time, O(1) space.

### Problem 3 — Second largest WITHOUT sorting

Sorting costs O(n log n). One clever pass costs O(n). That's why "without sorting".

- **Hint 1:** Keep TWO champions: `largest` and `second`.
- **Hint 2:** When a new item beats `largest` — careful, ORDER matters. Where should the old `largest` go before you crown the new one?
- **Hint 3:** What if the item beats `second` but not `largest`? Handle that branch too.
- **Hint 4 (gotcha):** `[10, 10, 5]` — is the second largest 10 or 5? Decide your rule for duplicates, then test with this exact input. Strict "second distinct largest" needs an extra condition.

### Problem 4 — Left rotate by one

`[1, 2, 3, 4]` → `[2, 3, 4, 1]`. In place again.

- **Hint 1:** Three moves: **save** something, **shift** things, **place** the saved thing.
- **Hint 2:** What must be saved before shifting destroys it?
- **Hint 3:** Shift each item one step LEFT — which direction should the loop travel so nothing gets overwritten too early?
- **Hint 4:** After the loop, the saved value has exactly one empty home. This whole exercise is O(n) shifting — the very cost we've been discussing for two days.

---

## 15. Common Mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `a = a.sort()` | `a` becomes `None` | `a.sort()` alone, or `b = sorted(a)` |
| `b = a` thinking it copies | Both names, one list | `b = a.copy()` |
| `a.copy()` on nested lists | Inner lists still shared | `copy.deepcopy(a)` |
| `append([1, 2])` to merge | Whole list nested as one item | `extend([1, 2])` |
| `arr[len(arr)]` | IndexError | Last index is `len(arr) - 1`, or use `arr[-1]` |
| `[[0]] * 3` for a grid | All rows are one shared list | `[[0] for _ in range(3)]` |
| `remove(x)` when x absent | ValueError crash | Check `if x in a:` first |
| Removing items while looping the same list | Skipped items, weird bugs | Loop over a copy, or build a new list |

---

## 16. Quick Recap

- List = ordered, changeable, duplicates allowed. Train of coaches.
- Index from 0; negative counts from the back; last index = `len - 1`.
- Slice `[start:end:step]` — end excluded, forgiving, `[::-1]` reverses a copy.
- Lists mutate in place; strings never do.
- Costs: `append`/`pop()` O(1); `insert(0)`/`pop(0)`/`remove`/`in`/`index`/`count` O(n); `sort` O(n log n).
- `sort()`/`reverse()` return `None` — never assign them back.
- `extend` merges items; `append` adds one item (even if that item is a list).
- `b = a` aliases; `a.copy()` copies one level; `deepcopy` copies all levels.
- Comprehension: end-`if` filters, front `if-else` transforms.

---

## 17. Learn More

- [W3Schools — Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [W3Schools — List Methods](https://www.w3schools.com/python/python_lists_methods.asp)
- [W3Schools — List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
- [GeeksforGeeks — Python Lists](https://www.geeksforgeeks.org/python/python-lists/)
- [Python Docs — More on Lists](https://docs.python.org/3/tutorial/datastructures.html)

---

## Tomorrow

Day 7 is **consolidation** — honestly, the most important day of the week. No new topics. Just proving what stuck: re-solving this week's problems from a blank file, no peeking. Anything you can't rebuild from memory, you haven't learned yet — and tomorrow is exactly when we find out, while it's still cheap to fix.
