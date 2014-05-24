#This program will display points you click in a circle

from graphics import *

def main():
	win = GraphWin() #Creates a new graphic window
	shape = Rectangle(Point(50,50),Point(65,65)) #Creates the first square
	shape.setOutline("red") #Sets the outline color to red
	shape.setFill("red") #Sets the fill to red
	shape.draw(win) #Draws the square to the graphic window
	for i in range(10): #Creates 10 loops
		newShape = shape.clone() #Clones the first square for use in the loop
		p = win.getMouse() #Sets the P variable to the mouse click in the graphic window
		c = shape.getCenter() #Sets the c var to the location of the center of the rectangle
		dx = p.getX() - c.getX() #Finds the new X point by subtracting the X location of the mouse click from the X location of the original square 
		dy = p.getY() - c.getY() #Finds the new X point by subtracting the Y location of the mouse click from the Y location of the original square
		newShape.move(dx, dy) #Moves the location of the clone
		newShape.draw(win) #Draws the newShape var

	exitScreen = Text(Point(80,50), "Press again to quit")
	exitScreen.draw(win)
	win.getMouse()
	win.close() #Closes the graphic window
main()
