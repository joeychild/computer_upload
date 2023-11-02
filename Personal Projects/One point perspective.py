import turtle as t
import tkinter as tk

t.speed(0)
t.colormode(255)
t.ht()

x = int(t.numinput("Inputs", "Enter x"))
y = int(t.numinput("Inputs", "Enter y"))
n = int(t.numinput("Inputs", "Enter number of sides"))

def test1():
    root.destroy()
    t.pu()
    t.goto(x, y)
    t.pd()
    for i in range(n):
        t.seth(t.towards(0,0))
        t.fd(t.distance(0,0)/2)
        t.seth(i * (360/n))
        t.fd(abs(y/4))
        t.seth(t.towards(0,0))
        t.bk(t.distance(0,0))
        t.seth(i * (360/n))
        t.bk(abs(y/2))
        t.fd(abs(y/2))

def test2():
    root.destroy()
    t.goto(x, y)
    for i in range(n):
        t.seth(i * (360/n))
        t.fd(abs(y/2))
        t.seth(t.towards(0,0))
        temp = t.distance(0,0)
        t.fd(temp)
        t.bk(temp/2)
        t.seth(i * (360/n))
        t.bk(abs(y/4))
        t.fd(abs(y/4))
        t.seth(t.towards(0, 0))
        t.bk(temp/2)

t.fd(960)
t.bk(1920)
t.fd(960)
t.dot(5)

root = tk.Tk()
parent = tk.Frame(root)
parent.pack()

button = tk.Button(parent, text = "Option 1", command = test1)
button2 = tk.Button(parent, text = "Option 2", command = test2)

button.pack()
button2.pack()

t.mainloop()
