from graphics import *

win = GraphWin()
pt = Point(100,50)
c = Circle(pt, 25)
c.draw(win)
win.getMouse()
r = Rectangle(pt, Point(0, 0))
r.draw(win)
win.getMouse()
l = Line(pt, Point(0, 0))
l.draw(win)
win.getMouse()
win.close()

win = GraphWin("Animation?", 1000, 1000, autoflush = False)
for i in range(300):
    l = Line(Point(i, i), Point(i+10, i+10))
    c = Circle(Point(i, i), 10)
    l.draw(win)
    if i % 10 == 0:
      c.draw(win)
    update(30)
win.getMouse()
win.close()

win = GraphWin()
o = Oval(Point(0, 0), Point(150, 100))
o.draw(win)
win.getMouse()
win.close()
