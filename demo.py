from pyrenza import T
import time

print("─" * 45)
print("  pyrenza demo")
print("─" * 45)

# basic
score = T(0)
score.set(10)
score.set(25)
score.set(100)

print("\ncurrent :", score)
print("previous:", score.prev)
print("first   :", score.first)
print("changes :", score.states())

score.log()
score.why()
score.diff()

# strings work too
status = T("idle")
status.set("loading")
status.set("done")
status.log()

# math works normally
health = T(100)
health.set(55)
print("health      :", health)
print("health - 10 :", health - 10)
print("health > 50 :", health > 50)

# time travel
budget = T(1000)
time.sleep(0.5)
budget.set(800)
time.sleep(0.5)
budget.set(600)
print("\n1s ago:", budget.ago(1))
print("now   :", budget)

print("\n" + "─" * 45)
