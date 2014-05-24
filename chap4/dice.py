#program draws five dice on the screen

from graphics import *
def main():
	win = GraphWin("5 die", 320, 320)
	win.setCoords(0,0, 20, 20)

	#create side one of the die
	d1 = Rectangle(Point(1,1), Point(5,5))
	d1.setFill("white")
	d1.setOutline("white")

	#create side two of the die
	d2 = d1.clone()
	d2.move(0,5)

	#create side three of the die
	d3 = d1.clone()
	d3.move(6,0)

	#create side four of the die
	d4 = d1.clone()
	d4.move(6,5)

	#create side five of the die
	d5 = d1.clone()
	d5.move(12,2)


	#dot for side one of dice
	dot1 = Circle(Point(3,3), .3)
	dot1.setFill("black")
	dot1.setOutline("black")

	#dots for side two of dice
	dot2 = dot1.clone()
	dot2.move(-1,4)

	dot3 = dot1.clone()
	dot3.move(1,6)

	#dots for side three of dice
	dot4 = dot1.clone()
	dot4.move(6,0)

	dot5 = dot1.clone()
	dot5.move(5,-1)

	dot6 = dot1.clone()
	dot6.move(7,1)

	#dots for side four of die
	dot7 = dot1.clone()
	dot7.move(5,4)

	dot8 = dot1.clone()
	dot8.move(5,6)

	dot9 = dot1.clone()
	dot9.move(7,4)

	dot10 = dot1.clone()
	dot10.move(7,6)

	#dots for side five of die
	dot11 = dot1.clone()
	dot11.move(11,1)

	dot12 = dot1.clone()
	dot12.move(13,1)

	dot13 = dot1.clone()
	dot13.move(12,2)

	dot14 = dot1.clone()
	dot14.move(11,3)	

	dot15 = dot1.clone()
	dot15.move(13,3)

	#draw the dice
	d1.draw(win)
	d2.draw(win)
	d3.draw(win)
	d4.draw(win)
	d5.draw(win)

	#draw the dots on the dice
	dot1.draw(win)
	dot2.draw(win)
	dot3.draw(win)
	dot4.draw(win)
	dot5.draw(win)
	dot6.draw(win)
	dot7.draw(win)
	dot8.draw(win)
	dot9.draw(win)
	dot10.draw(win)
	dot11.draw(win)
	dot12.draw(win)
	dot13.draw(win)
	dot14.draw(win)
	dot15.draw(win)

main()