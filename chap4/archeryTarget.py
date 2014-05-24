#This will draw a archery target with yellow, red, blue, black, and white

from graphics import *

def main():
	win = GraphWin("target", 320, 320) #draw the graphic box
	win.setCoords(0,0,100,100) #set coordinates so its easier to draw the circles
	yellowTarget = Circle(Point(50,50), 10) #yellow target
	yellowTarget.setFill("yellow") 
	yellowTarget.setOutline("yellow")
	redTarget = Circle(Point(50,50), 20) #red target
	redTarget.setFill("red")
	redTarget.setOutline("red")
	blueTarget = Circle(Point(50,50), 30) #blue target
	blueTarget.setFill("blue")
	blueTarget.setOutline("blue")
	blackTarget = Circle(Point(50,50), 40) #black target
	blackTarget.setFill("black")
	blackTarget.setOutline("black")
	whiteTarget = Circle(Point(50,50), 50) #white target
	whiteTarget.setFill("white")
	whiteTarget.setOutline("white")
	
	
	whiteTarget.draw(win) #draw the outmost target first
	blackTarget.draw(win) 
	blueTarget.draw(win)
	redTarget.draw(win)
	yellowTarget.draw(win)

main()