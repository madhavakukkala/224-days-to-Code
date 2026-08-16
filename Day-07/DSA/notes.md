[<< Day 06](../../Day-06/DSA/notes.md) | [🏠 Today's tasks](../task.md) | Day 08 >> *(coming soon)*

# Day 07 — Consolidation: Making It Stick

## Look how far you came

Six days ago you had never written a line of Python. Look at the ladder now:

- **Day 1** — variables, `print`, `input`: you taught the computer to remember and to talk.
- **Day 2** — `if/else` and loops: you taught it to decide and to repeat.
- **Day 3** — functions and star patterns: you learned to pack logic into reusable boxes.
- **Day 4** — Big-O time: you learned to *judge* code, not just write it.
- **Day 5** — space complexity and the call stack: you learned that memory has a cost too.
- **Day 6** — lists, slicing, aliasing, deepcopy: you met the workhorse of all of DSA.

That's a real ladder — from "what is a variable" to "why is this loop O(n²)". Respect that.

But here's the honest question: how much of that ladder do you *own*, and how much did you merely *see*? Today's whole job is converting **seen → known**. No new topics. This day matters more than any of the six before it.

## Why re-solving beats re-reading

Think of how we all prepared for board exams. Reading the textbook again feels productive — the words look familiar, so the brain says "haan, I know this." That feeling is a lie. Familiarity is not memory.

The only honest test is a blank page. Close the book, take a blank sheet, and try to write the answer. Wherever your pen stops — that exact spot is what you never actually learned.

There's science behind this: memory fades on a curve (the **forgetting curve**) — steep in the first day or two, slower later. Re-reading barely bends that curve. **Recalling** — pulling the answer out of your own head with effort — bends it hard.

Code works the same way. Reading your old `main.py` and nodding along proves nothing. Opening a **blank file** and re-building the pattern from zero proves everything.

## The blank-file protocol

1. Pick the 3 patterns/problems that troubled you most this week. Be honest — the ones you had to peek for.
2. Open a completely blank file. No old code on the second monitor. No notes open.
3. Re-solve each one fully — running and correct, not "almost".
4. Stuck? Good. **Stay stuck for a few minutes.** That struggle is the brain building the memory — like a muscle tearing slightly in the gym before it grows.
5. Only if truly blocked: open your old solution, read it, understand it, **close it**, and again write from blank. Reading and then immediately typing it out is copying, not recall.

## How to honestly pick your 3 hardest

Ask yourself for each pattern from this week:

- Did I peek at a reference even once? → candidate.
- Did it take me more than two tries to get it right? → candidate.
- If someone asked me the core logic right now, would I hesitate? → candidate.

The ones you *want* to avoid re-doing are exactly the ones to pick. The mind avoids what it fears; that fear is your syllabus for today. Picking the easy ones to feel good is cheating a person who trusted you — yourself.

## The 90-second test (your daily revision from now on)

For every problem in your revision queue: read only the title, then say **out loud** —

1. the approach in one or two lines,
2. the time complexity and why,
3. the space complexity and why.

Under 90 seconds, without opening the code. Like a cricket commentator summarising a match in one breath — if you truly followed the match, it flows; if you didn't, you mumble. Mumbling = mark it failed, re-solve it fully on the next Day 7.

Why out loud? Silent nodding hides gaps. Your own voice stumbling is the most honest examiner you will ever get, and it's free.

## Writing your Big-O cheat sheet (own words only!)

One page. Handwritten or typed, but **every sentence must be yours**. Copying a table from the internet gives you a pretty page and zero memory.

A skeleton you can fill (fill it **from your head first**, then verify against Day-04 and Day-05 notes):

- **What Big-O really measures** — one line, your words.
- **The six classes** — O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) — one everyday example each. Use your OWN analogies, not the ones from the notes. Inventing your own analogy is itself the memory test.
- **The rules** — drop constants, drop smaller terms, sequential loops add, nested loops multiply.
- **The traps** — the 1+2+...+n triangle loop that is still O(n²); the digit loop that is O(log₁₀ n) not O(n); `in` on a list being O(n) but O(1) on a set.
- **Space** — when a solution costs O(1) extra vs O(n) extra; what recursion silently costs on the call stack.
- **Best / average / worst** — one line each with one example.

If any box stays empty, that's not failure — that's today's discovery. Go fix exactly that box.

## Why revision returns at day 2, 5 and 10

Memory fades fastest right after learning, then slower. So revising **just before the fall** — after 2 days, then 5, then 10 — catches the memory at the exact moment it starts slipping. This is called **spaced repetition**, and it's the most proven study technique there is.

Think of watering a plant. Flooding it once on Sunday and forgetting it all week kills it. Watering it exactly when the soil starts drying keeps it alive with the least water. Your revision queue is that watering schedule — each well-timed revision makes the memory last several times longer than the previous one. Trust the queue; don't skip it, don't do extra.

## Week-1 self-checklist

For each item ask one question: **"Can I explain this to a friend right now, without opening any notes?"** Tick only if the honest answer is yes. Every unticked box is a 15-minute task for today.

- [ ] Variables — what `x = 5` actually does, and why `x = x + 1` makes sense
- [ ] `input()` always gives a string, and why `int()` is needed
- [ ] `if / elif / else` — how Python picks exactly one branch
- [ ] `for` vs `while` — when I'd choose each
- [ ] `range(start, stop, step)` — and why `stop` is never included
- [ ] Functions — parameters vs arguments, and what `return` really does
- [ ] Why a function with no `return` gives `None`
- [ ] Nested loops — how the inner loop fully finishes for each outer step
- [ ] Big-O — what it measures and why constants get dropped
- [ ] The triangle-sum trap: why 1+2+...+n work is O(n²)
- [ ] The digit-loop trap: why `n //= 10` loops are O(log n)
- [ ] Space complexity — counting *extra* memory, not the input
- [ ] The call stack — what recursion costs in memory and why it can overflow
- [ ] List indexing — why the last index is `len - 1`, and what `[-1]` means
- [ ] Slicing — `a[start:stop:step]` gives a *new* list
- [ ] `sort()` vs `sorted()` — in place vs photocopy
- [ ] `in` on a list is O(n); on a set it's O(1) average
- [ ] Aliasing — why `b = a` is a second sticker on the same dabba, not a copy
- [ ] Shallow copy vs `deepcopy` — and when shallow copy still bites you

## Common mistakes

- Re-reading old code and calling it revision. Reading is input; recall is output. Only output counts.
- Picking the 3 *easiest* patterns to feel good. Nobody else is checking — which is exactly why honesty here pays the most.
- Peeking "just for a second" at the first difficulty. Struggle first; that discomfort is the whole point.
- Copying a Big-O table off the internet. A borrowed cheat sheet is like a borrowed cricket bat with someone else's grip — useless in the match.
- Skipping the out-loud part of the 90-second test. Saying it aloud exposes gaps that silent nodding hides.
- Treating consolidation day as a rest day. It's the highest-return day of the week.
- Doing the checklist by mood ("haan, I think I know this"). The test is *explaining to a friend*, not feeling familiar.

## Quick recap

- Week 1 ladder: variables → control flow → functions → Big-O time → space → lists. Today converts seen → known.
- Blank file. No reference. 3 hardest patterns. Struggle → recall → memory.
- Big-O cheat sheet: one page, your own words, your own analogies. Empty boxes = today's syllabus.
- 90-second out-loud test for every revision item; failed = re-solve on next Day 7.
- Spaced repetition at day 2 / 5 / 10 beats the forgetting curve — water the plant when the soil dries.
- Familiar ≠ known. Only what you can produce from a blank page is known.

## Next week

Week 2 begins tomorrow: **strings** — the second workhorse of DSA — and problems that go a level deeper than this week's. And from tomorrow morning, the 06:30 revision slot is a permanent daily habit, not an event. The queue is now part of your life. That's not a burden — that's the machine that makes the next 217 days compound.

## Learn more

- [Forgetting curve and spaced repetition (Wikipedia)](https://en.wikipedia.org/wiki/Spacing_effect) — the science behind the 2/5/10 schedule
- [GFG — Python practice problems](https://www.geeksforgeeks.org/python-programming-language/python-exercises-practice-questions-and-solutions/) — extra blank-file material when the week's own problems run out

---

[<< Day 06](../../Day-06/DSA/notes.md) | [🏠 Today's tasks](../task.md) | Day 08 >> *(coming soon)*
