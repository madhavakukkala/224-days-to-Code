# Day 1 — Python Basics + First 5 Number Problems

Today was setup day plus the first real problems. These notes go from absolute zero to the level an interviewer expects. No skipping steps.

---

## 1. Setup (VS Code + Python)

- Installed Python and VS Code.
- Installed the **Python extension** in VS Code (it gives colours, error squiggles, and the Run button).
- To run a file: open the terminal in VS Code and type `python main.py`.
- One folder per day. Inside it, `main.py` is where I actually write code.

That's it. Setup is boring but it only happens once.

---

## 2. What is a variable?

A **variable** is a labelled box that stores a value.

Think of the dabbawala system in Mumbai. Every tiffin box has a code painted on it. The code tells you whose lunch is inside. A variable is the same: a name stuck on a value so you can find it later.

```python
runs = 87          # a box named "runs" holding the number 87
player = "Kohli"   # a box named "player" holding some text
```

Two technical words:

- **Integer (int)** — a whole number. `87`, `0`, `-5`.
- **String (str)** — text, always inside quotes. `"Kohli"`, `"hello"`.

You can change what's in the box anytime:

```python
runs = 87
runs = 90   # the old 87 is gone, the box now holds 90
```

---

## 3. print() — showing output

`print()` displays something on the screen. Whatever you put inside the brackets gets shown.

```python
print("Chai is ready")   # shows: Chai is ready
print(87)                # shows: 87
```

---

## 4. input() — taking input (THE trap)

`input()` asks the user to type something and hands it to your program.

**The trap: input() ALWAYS gives you a string.** Even if the user types `25`, you get the text `"25"`, not the number 25.

```python
age = input("Enter your age: ")
print(age + 5)   # CRASH! You can't add text and a number
```

Why does this matter? `"25" + "25"` gives `"2525"` (text glued together), not `50`. Like writing two scores next to each other on a scoreboard instead of adding them.

The fix is type casting (next section):

```python
age = int(input("Enter your age: "))
print(age + 5)   # works, shows 30
```

---

## 5. Type casting — converting between types

**Type casting** means converting a value from one type to another.

| Function | What it does | Example |
|---|---|---|
| `int(x)` | makes a whole number | `int("25")` → `25` |
| `float(x)` | makes a decimal number | `float("2.5")` → `2.5` |
| `str(x)` | makes text | `str(100)` → `"100"` |

A **float** is just a number with a decimal point, like `99.50` — think price of petrol per litre.

Notes:

- `int("abc")` crashes. Python can't magically turn "abc" into a number.
- `int(7.9)` gives `7` — it chops off the decimal part, it does NOT round.

---

## 6. f-strings — clean printing

An **f-string** is a string with an `f` before the quotes. Inside it, anything in `{curly braces}` gets replaced by its value.

```python
name = "Rohit"
runs = 264
print(f"{name} scored {runs} runs")   # Rohit scored 264 runs
```

Without f-strings you'd be juggling commas and `str()` calls. With f-strings it reads like a normal sentence. Use them everywhere.

---

## 7. The two heroes of digit problems: `%` and `//`

Every single problem today uses these two operators, so understand them cold.

### Modulo `%` — the remainder

`a % b` gives the **remainder** after dividing a by b.

```python
17 % 5   # 2  (5 goes into 17 three times, 2 left over)
453 % 10 # 3
```

**The magic: `num % 10` gives you the LAST digit of num.**
It's like taking the last coin off a stack of coins — you peel off just the bottom-most digit.

### Floor division `//` — divide and drop the decimals

`a // b` divides and **throws away everything after the decimal point**.

```python
17 // 5    # 3   (not 3.4)
453 // 10  # 45
```

**The magic: `num // 10` REMOVES the last digit of num.**

### Together they dismantle a number

Auto-rickshaw meter running backwards: `453` → peel `3`, left with `45` → peel `5`, left with `4` → peel `4`, left with `0`. Stop when 0.

```python
digit = num % 10   # look at the last digit
num = num // 10    # throw the last digit away
```

This peel-and-shrink loop is the skeleton of problems 2, 3, 4 and 5 below.

---

## 8. Quick word on complexity (plain English)

- **Time complexity** — how does the work grow when the input grows? Counting how many chai cups to make for n guests: more guests, more work.
- **Space complexity** — how much extra memory do we use, beyond the input itself?
- **O(n)** means work grows in step with n. **O(1)** space means we only use a fixed handful of variables no matter the input.
- For digit problems, note: a number `n` has about `log₁₀(n)` digits (1 crore = 10,000,000 has only 8 digits). So a loop that runs once per digit is **O(number of digits)**, written **O(log n)** — very fast.

---

## 9. Problem 1 — Sum of first N numbers

**Ask:** given n, return 1 + 2 + 3 + ... + n. For n = 10, answer is 55.

**Idea:** keep a running total, like adding each ball's runs to the scoreboard.

```python
def Sum_of_first_N(self, n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
```

- `range(1, n+1)` gives 1, 2, ..., n. The `+1` matters — `range` stops one BEFORE the second number.
- `sum += i` means `sum = sum + i`.

**Complexity:** Time O(n) — the loop runs n times. Space O(1) — just two variables.

**Interview bonus:** there's a formula, `n * (n + 1) // 2`, which is O(1) time. Gauss figured it out as a schoolkid. Good to mention.

---

## 10. Problem 2 — Reverse a number

**Ask:** 453 → 354.

**Idea:** peel the last digit off the old number, and push it onto the back of a new number.

```python
def reverse_a_number(self, number):
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    return reverse
```

The key line is `reverse = reverse * 10 + digit`. Multiplying by 10 shifts existing digits left (making room), then the new digit sits in the ones place. Like a queue at a ration shop where each new person joins at the end — but here "joining at the end" builds the number backwards.

Trace for 453:

| number | digit | reverse |
|---|---|---|
| 453 | 3 | 3 |
| 45 | 5 | 35 |
| 4 | 4 | 354 |
| 0 | — | done → 354 |

**Complexity:** Time O(log n) — one loop run per digit. Space O(1).

---

## 11. Problem 3 — Count digits

**Ask:** 1082945 → 7.

**Idea:** keep chopping off the last digit and count how many chops until nothing is left.

```python
def count_digits(self, num):
    count = 0
    while num > 0:
        num % 10
        count += 1
        num //= 10
    return count
```

**Did you notice?** The line `num % 10` sitting alone computes the last digit and then... throws it away. Nothing stores it. The function still works because we only need the COUNT of chops, not the digits themselves. That line can simply be deleted. Lesson: every line should earn its place.

**Complexity:** Time O(log n) (once per digit). Space O(1).

**Edge case to remember:** `num = 0` gives count 0 with this code, but zero has 1 digit. Interviewers love this one.

---

## 12. Problem 4 — Palindrome number

**Ask:** does the number read the same forwards and backwards? 32523 → yes. 453 → no.

**Idea:** reverse the number (exactly like Problem 2), then check if the reverse equals the original. Like "MADAM" — same from both sides.

```python
def palindrome_number(self, num):
    number = num
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    return num == reverse
```

- We copy `num` into `number` first, because the loop destroys its copy digit by digit. We need the untouched original for the final comparison.
- `num == reverse` is itself the answer: it's `True` or `False` (a **boolean** — a yes/no value).

**Complexity:** Time O(log n). Space O(1).

---

## 13. Problem 5 — Armstrong number

**Ask:** a number is an Armstrong number if the sum of each digit raised to the power of (number of digits) equals the number itself.

153 has 3 digits: `1³ + 5³ + 3³ = 1 + 125 + 27 = 153`. Yes, Armstrong.

**Idea:** two passes.
1. First pass: count the digits (that's Problem 3 again).
2. Second pass: peel each digit, raise it to that count (`digit ** count` — `**` means "to the power of"), add it up.
3. Compare the sum with the original.

```python
def armstrong_number(self, num):
    temp = num
    count = 0
    while temp > 0:
        temp % 10
        count += 1
        temp //= 10

    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10

    return sum == num
```

- Same "did you notice?" as Problem 3: the lone `temp % 10` in the first loop does nothing and can go.
- `temp = num` appears twice because each loop grinds `temp` down to 0, so we refill it before the second loop.

**Complexity:** Time O(log n) — two passes over the digits is still proportional to the digit count. Space O(1).

---

## Common mistakes

1. **Forgetting `int()` around `input()`.** `input()` always returns a string. `"5" + 1` crashes; `"5" * 2` gives `"55"`.
2. **`range(1, n)` instead of `range(1, n+1)`.** `range` excludes the end value, so you silently miss n. Off-by-one errors are the #1 beginner bug.
3. **Confusing `/` and `//`.** `453 / 10` is `45.3` (a float). Digit problems need `453 // 10` = `45`. A float in the loop breaks everything.
4. **Not saving the original before destroying it.** In palindrome/Armstrong, the loop eats the number. Copy it first (`number = num`), or the final comparison compares against 0.
5. **Writing an expression on its own line and thinking it did something.** `num % 10` alone computes a value and discards it. It must be assigned: `digit = num % 10`.
6. **Using `sum` as a variable name.** It works, but `sum` is also a built-in Python function; naming a variable `sum` shadows (hides) it. `total` is safer. Same story for `count` vs the string method — fine here, but worth knowing.
7. **Ignoring edge cases:** n = 0, single-digit numbers (every single-digit number is a palindrome AND an Armstrong number).

---

## Quick recap

- Variable = named box. `input()` gives a string — cast it with `int()`.
- f-strings: `f"{name} scored {runs}"`.
- `% 10` peels the last digit; `// 10` throws it away. Loop until 0.
- Reverse = peel from one number, push into another via `reverse*10 + digit`.
- Palindrome = reverse, then compare with the saved original.
- Armstrong = count digits, then sum of `digit ** count`, then compare.
- All digit loops: O(log n) time (once per digit), O(1) space.
- Pending for Day 3: prime check, GCD by Euclid, LCM.
