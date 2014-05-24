#This program will draw a rectangle after three clicks by the user, then calculat the area and perimeter

from graphics import *
import math

def main():
	win = GraphWin("Draw a Rectangle", 320, 320)
	win.setCoords(0, 0, 10, 10)
	message = Text(Point(5, 0.5), "Click on two points")
	message.draw(win)

	#Get the four points from mouse click
	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)


	#create and draw the rectangle
	rectangle = Rectangle(p1, p2)
	rectangle.setFill("red")
	rectangle.setOutline("cyan")

	rectangle.draw(win)

	#calculate and print the length and slope of the line
	p1X = round(p1.getX())
	p1Y = round(p1.getY())
	p2X = round(p2.getX())
	p2Y = round(p2.getY())
	dx = p2X - p1X
	dy = p2Y - p1Y
	area = round(dx * dy)
	perimeter = round(2 * (dx + dy))


	#display the slope and the length
	Text(Point(1,9), area).draw(win)
	Text(Point(1,8), perimeter).draw(win)

main()
