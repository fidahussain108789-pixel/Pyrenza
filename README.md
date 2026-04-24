# Chronos
A Python variable that remembers its entire life. x.prev x.why() x.ago(3) x.diff() — the history lives inside the variable itself. No debugger. No logging. No setup. Just time, built in.
# CHRONOS — Copy-Paste Descriptions for Every Platform

---

## GITHUB

### Repo Description (one line, shown under repo name)
A Python variable that remembers its entire life. `.why()` `.prev` `.ago()` `.diff()`

### README tagline
> Variables have no memory. I think that's wrong.

### GitHub Topics/Tags (add all of these)
python, debugging, developer-tools, time-travel, variable-history,
python-library, devtools, causal-debugging, temporal, pip

---

## PYPI (python package page)

### Short description
A Python type where every variable remembers its entire history — queryable by index, time, or causality.

### Long description (paste in the PyPI readme field)
Every programming language ever made gives a variable one value: its current one.
The past is gone. Chronos fixes that.

    from chronos import T

    score = T(0)
    score.set(10)
    score.set(100)

    score.prev    # 10
    score.first   # 0
    score.why()   # explains the last change, file + line + time
    score.log()   # full timeline
    score.diff()  # every change with delta
    score.ago(3)  # what it was 3 seconds ago

No debugger. No logging setup. No external tools.
Time is part of the variable itself.

---

## REDDIT (r/Python, r/programming)

### Title
I made a Python variable that remembers its entire life — x.prev, x.why(), x.ago(3)

### Body
Every variable in every language has one value: the current one.
The past is just gone.

I built Chronos — a Python type where history is native to the variable itself.

    from chronos import T

    score = T(0)
    score.set(10)
    score.set(25)
    score.set(100)

    print(score.prev)    # 25
    print(score.first)   # 0
    score.why()          # "set at 14:22:01, line 7, was 25"
    score.diff()         # 0→10 (+10), 10→25 (+15), 25→100 (+75)
    score.ago(3)         # what it was 3 seconds ago

Still acts like a normal variable — math, comparisons, print all work.

Existing tools (watchpoints, time-travel debuggers) are external monitors
you attach to your program. This is the history living inside the variable itself.

GitHub: github.com/yourname/chronos
pip install chronos-t

Would love feedback from the community — especially whether this
is actually useful in real projects or feels like over-engineering.

---

## HACKER NEWS

### Title
Show HN: Chronos – Python variables that remember their entire history natively

### Body
I built a small Python library where every variable carries its own
queryable history — not as an external debugger or profiler, but as
a native property of the object itself.

    x = T(100)
    x.set(80)
    x.set(55)

    x.prev       # 80
    x.why()      # line number, timestamp, previous value
    x.ago(2)     # what x was 2 seconds ago
    x.diff()     # every change with numeric delta

The closest existing tools are watchpoints (alerts on change, no history)
and time-travel debuggers like PyTrace (external process, not in-code).
Neither lets you call .why() directly in your source.

The long-term goal is a CPython patch where T() becomes unnecessary —
every variable is temporal by default.

GitHub: github.com/yourname/chronos

---

## TWITTER / X

### Launch tweet
just shipped Chronos —

a Python variable that remembers everything

    x = T(0)
    x.set(42)
    x.set(99)

    x.prev    → 42
    x.why()   → "set at line 7, was 42"
    x.ago(3)  → what x was 3 seconds ago

no debugger. no logs. time is just part of the variable.

pip install chronos-t
github: [link]

---

### Follow-up tweet (post 2 days later)
the idea behind Chronos:

every other debugging tool is something you ATTACH to your code

watchpoints — notifies you of changes
time-travel debuggers — separate process
logging — manual, you have to set it up

Chronos puts the history INSIDE the variable

x.why() just works. anywhere. always.

---

## DEV.TO / HASHNODE (blog post title options, pick one)

1. "Variables have no memory. I built one that does."
2. "I added time travel to Python variables"
3. "What if x.why() just worked — anywhere, always?"
4. "The debugging tool that lives inside the variable itself"
5. "Every variable loses its past. I think that's a design flaw."

---

## LINKEDIN

I just open-sourced something I've been building called Chronos.

The idea is simple: in every programming language ever made,
a variable has one value — its current one. The past is gone.

Chronos makes time a native property of the variable itself.

    score = T(0)
    score.set(100)
    score.prev     # previous value
    score.why()    # explains the last change
    score.diff()   # full change history with deltas

No debugger setup. No logging. No external tools.

Built in Python. One file. Zero dependencies.

Would love thoughts from developers — does this solve a real pain
you've felt, or is it a cool idea that wouldn't change how you work?

GitHub: [link]
pip install chronos-t

#Python #OpenSource #DevTools #Debugging #Programming

---

## PRODUCT HUNT (when you're ready to launch there)

### Tagline
Python variables that remember everything — .why(), .prev, .ago(), .diff()

### Description
Chronos is a Python library that gives every variable a built-in memory.
Not a debugger. Not a profiler. The history lives inside the variable itself.

You write x.why() in your actual source code and it tells you exactly
how that value got there — timestamp, file, line, previous value.

Perfect for: debugging complex state, teaching students causality in code,
tracing bugs that only appear after many state changes.

One file. Zero dependencies. pip install chronos-t.
