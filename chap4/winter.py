# this will draw a winter festive scene

from graphics import *

def main():
	win = GraphWin("Happy Holidays", 320, 320)
	win.setCoords(0, 0, 50, 50)

	trunk = Rectangle(Point(10,0), Point(18,4))
	trunk.setFill("brown")
	trunk.setOutline("brown")

	trunk.draw(win)

	t1 = Polygon(Point(2,4), Point(26,4), Point(14,18))
	t1.setFill("darkgreen")
	t1.setOutline("darkgreen")

	t1.draw(win)

	t2 = Polygon(Point(4,10), Point(24,10), Point(14,26))
	t2.setFill("darkgreen")
	t2.setOutline("darkgreen")

	t2.draw(win)

	t3 = Polygon(Point(6,20), Point(22,20), Point(14,32))
	t3.setFill("darkgreen")
	t3.setOutline("darkgreen")

	t3.draw(win)

	t4 = Polygon(Point(10,30), Point(18,30), Point(14,36))
	t4.setFill("darkgreen")
	t4.setOutline("darkgreen")

	t4.draw(win)

	starTop = Polygon(Point(14,38), Point(12,34), Point(16,34))
	starTop.setFill("yellow")
	starTop.setOutline("yellow")

	starTop.draw(win)

	startBottom = Polygon(Point(14,32), Point(12, 36), Point(16, 36))
	startBottom.setFill("yellow")
	startBottom.setOutline("yellow")

	startBottom.draw(win)


	s1 = Circle(Point(38,6), 6)
	s1.setFill("white")
	s1.setOutline("white")

	s1.draw(win)

	s2 = Circle(Point(38,12), 5)
	s2.setFill("white")
	s2.setOutline("white")

	s2.draw(win)

	s3 = Circle(Point(38,18), 3)
	s3.setFill("white")
	s3.setOutline("white")

	s3.draw(win)

	b1 = Circle(Point(6,6), 1)
	b1.setFill("blue")
	b1.setOutline("blue")

	b2 = b1.clone()
	b2.move(6, 0)
	b2.setFill("red")
	b2.setOutline("red")

	b3 = b1.clone()
	b3.move(14, 0)
	b3.setFill("yellow")
	b3.setOutline("yellow")

	b4 = b1.clone()
	b4.move(4, 4)
	b4.setFill("yellow")
	b4.setOutline("yellow")

	b5 = b1.clone()
	b5.move(10, 4)
	b5.setFill("green")
	b5.setOutline("green")

	b6 = b1.clone()
	b6.move(6, 10)
	b6.setFill("red")
	b6.setOutline("red")

	b7 = b1.clone()
	b7.move(12, 10)
	b7.setFill("yellow")
	b7.setOutline("yellow")

	b8 = b1.clone()
	b8.move(8, 14)
	b8.setFill("darkblue")
	b8.setOutline("darkblue")

	b9 = b1.clone()
	b9.move(8, 18)
	b9.setFill("green")
	b9.setOutline("green")

	b10 = b1.clone()
	b10.move(6, 20)
	b10.setFill("yellow")
	b10.setOutline("yellow")

	b1.draw(win)
	b2.draw(win)
	b3.draw(win)
	b4.draw(win)
	b5.draw(win)
	b6.draw(win)
	b7.draw(win)
	b8.draw(win)
	b9.draw(win)
	b10.draw(win)


	c1 = Circle(Point(38, 8), .5)
	c1.setFill("black")
	c1.setOutline("black")

	c1.draw(win)


main()