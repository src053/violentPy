#This program will draw a face

from graphics import *

def main():
	win = GraphWin("Smiley Guy", 320, 320)
	win.setCoords(0,0,100,100)
	
	head = Circle(Point(50,50), 40)
	head.setFill("yellow")
	head.setOutline("black")

	head.draw(win)

	smile = Circle(Point(50, 47), 25)
	smile.setFill("yellow")
	smile.setWidth(3)
	smile.setOutline("black")

	smile.draw(win)

	coverSmile = Rectangle(Point(18, 32), Point(75,72))
	coverSmile.setFill("yellow")
	coverSmile.setWidth(3)
	coverSmile.setOutline("yellow")

	coverSmile.draw(win)



	leftEye = Circle(Point(35, 60), 5)
	leftEye.setFill("black")
	leftEye.setOutline("black")

	rightEye = leftEye.clone()
	rightEye.move(30, 0)

	rightEye.draw(win)
	leftEye.draw(win)


main()
