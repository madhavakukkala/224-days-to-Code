# Day 07 Night — What Actually Happens When You Run a Python File

You've typed `python main.py` dozens of times this week. Tonight: what really happens in that half-second between pressing Enter and seeing output.

## Interpreter vs compiler — the translator analogy

Imagine your Python file is a speech written in Hindi, and the computer only understands a tribal language nobody speaks directly.

- A **compiler** is a translator who takes your whole speech home, translates the entire thing into the computer's language, and hands you back a finished translated book (an `.exe` file). Slow to prepare, but the speech itself then runs at full native speed. C and C++ work this way.
- An **interpreter** is a live translator standing next to you, translating as you speak — sentence by sentence. You can start immediately and change lines on the fly, but every sentence pays a small translation cost while running. Python works this way.

That's the honest reason Python is slower than C — and also why it's so comfortable to learn and experiment in. You trade raw speed for speed of *thinking*.

## The actual journey of `python main.py`

Step by step:

1. **Read & check** — Python reads your file and checks the grammar (syntax). One misplaced colon and it stops right here with a `SyntaxError` — before running anything.
2. **Compile to bytecode** — surprise: Python DOES compile! But not to machine code — to **bytecode**: small, simple instructions like "load this value", "add", "return". Think of it as your recipe rewritten into telegram-style short steps that a trained cook can follow blindly.
3. **Cache it** — that bytecode is saved in the `__pycache__` folder as a `.pyc` file (for imported modules). Next run, if the source didn't change, Python skips step 2 and picks up the ready bytecode — like keeping the chopped vegetables from yesterday. That folder is auto-generated; never edit it, and don't push it to GitHub (`.gitignore` it).
4. **Execute on the PVM** — the **Python Virtual Machine** (the interpreter's engine) runs the bytecode one instruction at a time and talks to your actual CPU.

So: **source code → bytecode → PVM → output.** You can see the bytecode yourself:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

## Memory: names and objects — the sticker system

The most useful mental model in all of Python:

- Values (numbers, strings, lists) are **objects** — dabbas sitting in memory.
- Variables are just **name stickers** stuck on those dabbas.

```python
a = [1, 2, 3]   # a dabba is created, sticker "a" goes on it
b = a           # NO new dabba — a second sticker "b" on the SAME dabba
```

This is exactly why the Day-06 aliasing surprise happens — two stickers, one dabba. Change through either name, both "see" it.

**Reference counting:** Python keeps count of how many stickers each dabba has. When the last sticker comes off (variable reassigned, function ends), the count hits zero and Python's **garbage collector** throws the dabba away and frees the memory — like a hotel cleaning a room the moment the last guest checks out. You never free memory manually in Python; this is why.

Two quick fun checks:

```python
x = [10, 20]
y = x
print(id(x) == id(y))   # True — same dabba, id() is like its address

import sys
print(sys.getsizeof(0))          # even a small int costs ~28 bytes!
```

That last one explains why Python objects are heavier than C's raw numbers — every dabba carries its own label, type info, and reference count.

## Where things live while running

While your program runs, function calls sit in the **call stack** (the same stack from Day-05's recursion notes — plates in the hostel mess), and the objects themselves live in a big open area called the **heap**. A function's local stickers vanish when it returns; the dabba survives only if some other sticker still points to it.

## Set up your notes repo on GitHub ✅

Already done — this repo is it! Quick health checklist worth keeping for the whole 224 days:

- [x] README that tells a stranger what this is in 10 seconds
- [x] One folder per day, same structure every day
- [x] task.md → attempt → notes flow
- [ ] Commit **every day** (23:45 slot) — the green graph is the streak-keeper
- [ ] Write commit messages that say what you learned, not "update files"
- [ ] Add `__pycache__/` to a `.gitignore` (now you know what it is!)

## Common mistakes

- Saying "Python is interpreted, so it doesn't compile." It compiles — to bytecode, not machine code. Interviewers love this distinction.
- Editing or committing `__pycache__` / `.pyc` files. Generated files; ignore them.
- Thinking `b = a` copies a list. It copies the *sticker*, not the dabba.
- Confusing bytecode with machine code. Bytecode needs the PVM; machine code runs on the CPU directly.
- Believing the garbage collector is magic you never need to know. Reference counting is asked in interviews surprisingly often.

## Quick recap

- `python main.py` → syntax check → **bytecode** → cached in `__pycache__` → executed by the **PVM**.
- Interpreter = live translator (start fast, run slower). Compiler = whole book first (prepare slow, run fast).
- Variables are stickers; values are dabbas. Reference count hits zero → garbage collector frees it.
- Call stack holds running functions; heap holds the objects.
- Repo is live — from tonight, the 23:45 commit is a daily non-negotiable.
