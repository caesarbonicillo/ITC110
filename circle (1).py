#create a function that makes a circle.
#import graphics library
# make 3 circles

from graphics import *

win = GraphWin ("Faces", 400, 400)

def circ():
    Circle(Point(100,300), 80)
    circ.setFill("black")
    circ.setOutline("black")
    circ.draw(win)

pos = 100

rad = 80

def circles():
    for x in range(3):
       circ = Circle(Point(pos +100),rad - 80)
