# Day 07 — Consolidation: Making It Stick

No new topics today. Today is about one question: **what do you actually remember?**

## Why re-solving beats re-reading

Think of how we all prepared for board exams. Reading the textbook again feels productive — the words look familiar, so the brain says "haan, I know this." That feeling is a lie. Familiarity is not memory.

The only honest test is a blank page. Close the book, take a blank sheet, and try to write the answer. Wherever your pen stops — that exact spot is what you never actually learned.

Code works the same way. Reading your old `main.py` and nodding along proves nothing. Opening a **blank file** and re-building the pattern from zero proves everything.

## The blank-file protocol

1. Pick the 3 patterns that troubled you most this week. Be honest — the ones you had to peek for.
2. Open a completely blank file. No old code on the second monitor. No notes open.
3. Re-solve each one fully — running and correct, not "almost".
4. Stuck? Good. **Stay stuck for a few minutes.** That struggle is the brain building the memory — like a muscle tearing slightly in the gym before it grows.
5. Only if truly blocked: open your old solution, read it, understand it, **close it**, and again write from blank. Reading and then immediately typing it out is copying, not recall.

## How to pick your 3 hardest

Ask yourself for each pattern from this week:

- Did I peek at a reference even once? → candidate.
- Did it take me more than two tries to get the spaces right? → candidate.
- If someone asked me the row-logic right now, would I hesitate? → candidate.

The ones you *want* to avoid re-doing are exactly the ones to pick. The mind avoids what it fears; that fear is your syllabus for today.

## The 90-second test (your daily revision from now on)

For every problem in your revision queue: read only the title, then say **out loud** —

1. the approach in one or two lines,
2. the time complexity and why,
3. the space complexity and why.

Under 90 seconds, without opening the code. Like a cricket commentator summarising a match in one breath — if you truly followed the match, it flows; if you didn't, you mumble. Mumbling = mark it failed, re-solve it fully on the next Day 7.

## Writing your Big-O cheat sheet (own words only!)

One page. Handwritten or typed, but **every sentence must be yours**. Copying a table from the internet gives you a pretty page and zero memory.

A skeleton you can fill (fill it from your head, then verify against Day-04 notes):

- **What Big-O really measures** — one line, your words.
- **The six classes** — O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) — one everyday example each. Use your OWN analogies, not the ones from the notes. Making your own analogy is itself the memory test.
- **The rules** — drop constants, drop smaller terms, sequential loops add, nested loops multiply.
- **The traps** — the 1+2+...+n loop that is still O(n²); the digit loop that is O(log₁₀ n) not O(n); `in` on a list being O(n).
- **Best / average / worst** — one line each with one example.

If any box stays empty, that's not failure — that's today's discovery. Go fix exactly that box.

## Why revision comes back at day 2, 5 and 10

Memory fades on a schedule — steep at first, slower later (the forgetting curve). Revising just before the fall — after 2 days, then 5, then 10 — is like watering a plant exactly when the soil starts drying instead of flooding it once and forgetting it. Each revision at the right moment makes the memory last several times longer than the previous one. That's why the queue works — trust it, don't skip it.

## Common mistakes

- Re-reading old code and calling it revision. Reading is input; recall is output. Only output counts.
- Picking the 3 *easiest* patterns to feel good. You're cheating only yourself — nobody else is checking.
- Peeking "just for a second" at the first difficulty. Struggle first; that discomfort is the whole point.
- Copying a Big-O table off the internet. A borrowed cheat sheet is like a borrowed cricket bat with someone else's grip — useless in the match.
- Skipping the out-loud part of the 90-second test. Saying it aloud exposes gaps that silent nodding hides.
- Treating consolidation day as a rest day. It's the highest-return day of the week.

## Quick recap

- Blank file. No reference. 3 hardest patterns. Struggle → recall → memory.
- Big-O cheat sheet: one page, your own words, your own analogies.
- 90-second out-loud test for every revision item; failed = re-solve on next Day 7.
- Revision at day 2 / 5 / 10 beats the forgetting curve.
- Familiar ≠ known. Only what you can produce from a blank page is known.
