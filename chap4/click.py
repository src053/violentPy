# start using mouse clicks

from graphics import *

def main():
	win = GraphWin("Click Me!")
	win.setCoords(0,0,25,25)
	for i in range(10):
		p = win.getMouse()
		print("You clicked at:", round(p.getX()), round(p.getY()))

main()