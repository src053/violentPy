#This program will draw a traingle after three clicks by the user

from graphics import *
import math

def main():
	win = GraphWin("Draw a line", 320, 320)
	win.setCoords(0, 0, 10, 10)
	message = Text(Point(5, 0.5), "Click on two points")
	message.draw(win)

	#Get the two points from mouse click
	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)

	#create and draw the lines
	line = Line(p1, p2)
	midPoint = line.getCenter()
	midPoint.setOutline("cyan")

	line.draw(win)
	midPoint.draw(win)

	#calculate and print the length and slope of the line
	p1X = round(p1.getX())
	p1Y = round(p1.getY())
	p2X = round(p2.getX())
	p2Y = round(p2.getY())
	dx = p2X - p1X
	dy = p2Y - p1Y
	slope = round(dy / dx, 2)
	length = round(math.sqrt((dx ** 2) + (dy ** 2)))


	#display the slope and the length
	Text(Point(1,9), slope).draw(win)
	Text(Point(1,8), length).draw(win)
	#Text(Point(1,7), p2X).draw(win)
	#Text(Point(1,6), p2Y).draw(win)

main()
