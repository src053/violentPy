#This program will display points you click in a circle

from graphics import *

def main():
	win = GraphWin()
	shape = Rectangle(Point(50,50),Point(65,65))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for i in range(10):
		p = win.getMouse()
		c = shape.getCenter()
		dx = p.getX() - c.getX()
		dy = p.getY() - c.getY()
		shape.move(dx,dy)
	win.close()
main()