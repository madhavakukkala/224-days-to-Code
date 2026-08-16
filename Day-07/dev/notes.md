[<< Day 06](../../Day-06/dev/notes.md) | [🏠 Today's tasks](../task.md) | Day 08 >> *(coming soon)*

# Day 07 Night — What Actually Happens When You Run a Python File

Your week-1 page is done: built, meta-tagged, favicon-ed, validated by W3C, and shareable with a proper preview card. That chapter is closed. So tonight we do something different — we look **under Python's hood**.

Why? Because a FAANG engineer isn't someone who just knows a language. It's someone who knows the machine beneath it. You've typed `python main.py` dozens of times this week. Tonight: what really happens in that half-second between pressing Enter and seeing output.

## Interpreter vs compiler — the translator analogy

Imagine your Python file is a speech written in Hindi, and the computer only understands a language nobody speaks directly.

- A **compiler** is a translator who takes your whole speech home, translates the entire book in one go, and hands you back a finished translated book (an `.exe` file). Slow to prepare, but the speech then runs at full native speed. C and C++ work this way.
- An **interpreter** is a live translator standing next to you, translating as you speak — sentence by sentence. You can start immediately and change lines on the fly, but every sentence pays a small translation cost while running. Python works this way.

That's the honest reason Python is slower than C — and also why it's so comfortable to learn and experiment in: it runs the moment you write it, it works the same on Windows, Mac and Linux, and its syntax reads almost like English. You trade raw speed for speed of *thinking*.

And that trade is usually fine: for most programs the computer waits on *you* (or the disk, or the network), not the other way round. When raw speed truly matters, the heavy libraries (NumPy, pandas) do their maths in C underneath anyway.

(Advanced bonus, one line only: CPython also has a rule called the **GIL** — only one thread runs Python bytecode at a time. You'll meet it properly later; today just recognise the name.)

## The actual journey of `python main.py`

Step by step:

1. **Read & check** — Python reads your file and checks the grammar (syntax). One misplaced colon and it stops right here with a `SyntaxError` — before running anything.
2. **Compile to bytecode** — surprise: Python DOES compile! But not to machine code — to **bytecode**: small, simple instructions like "load this value", "add", "return". Think of it as your recipe rewritten into telegram-style short steps that a trained cook can follow blindly.
3. **Cache it** — that bytecode is saved in the `__pycache__` folder as a `.pyc` file (for imported modules). Next run, if the source didn't change, Python skips the compile step and picks up the ready bytecode — like keeping yesterday's chopped vegetables. That folder is auto-generated; never edit it, never push it to GitHub.
4. **Execute on the PVM** — the **Python Virtual Machine** (the interpreter's engine) reads the bytecode instruction by instruction and gets your actual CPU to do the work.

So the full pipeline: **source code → syntax check → bytecode → (`__pycache__/.pyc` cache) → PVM → output.**

One distinction interviewers love: **bytecode is NOT machine code.** Machine code is raw 0s and 1s a CPU runs directly. Bytecode is a middle language that only the PVM understands — that's exactly what makes the same `.py` file portable across Windows, Mac and Linux: each OS has its own PVM, but the bytecode is the same.

See the bytecode yourself (you ran this in today's notebook):

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)   # LOAD_FAST a, LOAD_FAST b, BINARY_OP +, RETURN_VALUE
```

One more name worth knowing: the Python you installed is actually **CPython** — the default, official implementation, written in C. When people say "Python does X", they almost always mean CPython. (Advanced bonus, one line: there's a faster cousin called **PyPy** that can speed up long-running programs a lot — just recognise the name for now.)

## Memory: names and objects — the sticker system

The most useful mental model in all of Python:

- Values (numbers, strings, lists) are **objects** — dabbas sitting in memory.
- Variables are just **name stickers** stuck on those dabbas.

```python
a = [1, 2, 3]   # a dabba is created, sticker "a" goes on it
b = a           # NO new dabba — a second sticker "b" on the SAME dabba
```

This is exactly why the Day-06 aliasing surprise (and Quiz 5 this morning) happens — two stickers, one dabba. Change through either name, both "see" it.

**Reference counting:** Python keeps count of how many stickers each dabba has. When the last sticker comes off (variable reassigned, function ends), the count hits zero and Python's **garbage collector** throws the dabba away and frees the memory — like a hotel cleaning a room the moment the last guest checks out. You never free memory manually in Python; this is why. (Advanced one-liner: if two dabbas point at *each other*, their counts never hit zero — a separate **cycle collector** hunts those down periodically. Just know it exists.)

Two quick fun checks:

```python
x = [10, 20]
y = x
print(id(x) == id(y))   # True — same dabba; id() is like its address

import sys
print(sys.getsizeof(0))          # even the number 0 costs ~28 bytes!
```

That last one explains why Python objects are heavier than C's raw numbers — every dabba carries its own label, type info, and reference count. Convenience has a memory price; Day-05's space lessons just got their "why".

## Where things live while running

While your program runs, function calls sit in the **call stack** (the same stack from Day-05's recursion notes — plates in the hostel mess: last placed, first removed), and the objects themselves live in a big open area called the **heap**. A function's local stickers vanish when it returns; the dabba survives only if some other sticker still points to it.

## Your notes repo on GitHub ✅

Already done — this repo is it! Quick health checklist worth keeping for the whole 224 days:

- [x] README that tells a stranger what this is in 10 seconds
- [x] One folder per day, same structure every day
- [x] task.md → attempt → notes flow
- [ ] Commit **every day** (23:45 slot) — the green graph is the streak-keeper
- [ ] Write commit messages that say what you learned, not "update files"
- [ ] Add `__pycache__/` to a `.gitignore` (now you know exactly what it is and why it doesn't belong in git!)

```gitignore
# .gitignore
__pycache__/
*.pyc
```

## Common mistakes

- Saying "Python is interpreted, so it doesn't compile." It compiles — to bytecode, not machine code. Interviewers love this distinction.
- Confusing bytecode with machine code. Bytecode needs the PVM; machine code runs on the CPU directly.
- Editing or committing `__pycache__` / `.pyc` files. Generated files; ignore them.
- Thinking `b = a` copies a list. It copies the *sticker*, not the dabba.
- Believing the garbage collector is magic you never need to know. Reference counting comes up in interviews surprisingly often.
- Feeling bad that Python is "slow". For learning, scripting, and most real work, developer speed beats CPU speed — and the fast parts are C underneath.

## Quick recap

- `python main.py` → syntax check → **bytecode** → cached in `__pycache__` as `.pyc` → executed by the **PVM**.
- Interpreter = live translator (start fast, run slower). Compiler = whole book first (prepare slow, run fast).
- Bytecode ≠ machine code — and that gap is exactly what makes Python portable.
- Variables are stickers; values are dabbas. Reference count hits zero → garbage collector frees it. `id()` shows the dabba's address.
- Call stack holds running functions; heap holds the objects. `sys.getsizeof` shows why dabbas are heavy.
- Your Python is **CPython** (the default implementation). PyPy, the cycle collector and the GIL are names to recognise for now.
- Repo is live — from tonight, the 23:45 commit is a daily non-negotiable, and `__pycache__/` goes in `.gitignore`.

## Next week (nights)

The page's skeleton is done and its engine-room is understood. Next week's nights: **CSS** — making that validated page actually look good. Structure this week, style the next. That's how real front-ends are built.

## Learn more

- [GFG — Internal working of Python](https://www.geeksforgeeks.org/python/internal-working-of-python/) — the full source → bytecode → PVM pipeline in detail
- [W3Schools — Python introduction](https://www.w3schools.com/python/python_intro.asp) — why Python is built the way it is
- [Python docs — the `dis` module](https://docs.python.org/3/library/dis.html) — every bytecode instruction, when you're curious

---

[<< Day 06](../../Day-06/dev/notes.md) | [🏠 Today's tasks](../task.md) | Day 08 >> *(coming soon)*
