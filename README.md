# Pyrenza

> A Python variable that remembers its entire life.

```python
from pyrenza import T

score = T(0)
score.set(10)
score.set(100)

print(score)       # 100
print(score.prev)  # 10
print(score.first) # 0
score.why()        # explains the last change
score.log()        # full timeline
score.diff()       # every change with delta
score.ago(3)       # what it was 3 seconds ago
```

No debugger. No logging. No setup. The history lives inside the variable itself.

---

## Install

```bash
pip install pyrenza
```

---

## API

| Method | What it does |
|---|---|
| `T(value)` | Create a temporal variable |
| `.set(value)` | Update the value |
| `.prev` | Previous value |
| `.first` | Very first value |
| `.ago(seconds)` | Value N seconds ago |
| `.why()` | Explains the last change |
| `.log()` | Full timeline |
| `.diff()` | Every change + delta |
| `.states()` | How many times it changed |

---

## License
MIT
