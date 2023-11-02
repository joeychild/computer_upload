import turtle as t
import time
t.speed(0)
t.colormode(255)
s = t.Screen()

def clear():
    time.sleep(1)
    t.clearscreen()

s.tracer(0)
for i in range(255):
    t.fd(1)
    t.pencolor((i,i,i))
s.update()
clear()

t.bgcolor("black")
s.tracer(0)
for i in range(500):
  if i % 3 == 0:
    t.pencolor("red")
  elif i % 3 == 1:
    t.pencolor("yellow")
  else:
    t.pencolor("blue")
  t.fd(i)
  t.rt(121)
s.update()
clear()

print("Old project. Copy and paste into VSCode if you really want to try.")
print("https://replit.com/@JoeyZ/X-Camp-Gomoku-Project#main.py")
time.sleep(1)

n = int(input(("hew men sed ")))
for i in range(n):  
    t.fd(25)
    t.rt(360/n)
clear()