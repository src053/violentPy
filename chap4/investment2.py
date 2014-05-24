# This program will graph a future value when given initial investment and apr

from graphics import *

def main():
	#Introduction
	print("This program plots the growth of a 10-year investment")

	#Get the principal and interest rate
	principal = eval(input("Enter the intial principal: "))
	apr = eval(input("Enter the annualized interest rate: "))

	#Create a graphics window with labels on left edge
	win = GraphWin("INvestment Growth Chart", 320, 240)
	win.setBackground("white")
	win.setCoords(-1.75, -200, 11.5, 10400)
	Text(Point(-1, 0), '0.0K').draw(win)
	Text(Point(-1, 2500), '2.5K').draw(win)
	Text(Point(-1, 5000), '5.0K').draw(win)
	Text(Point(-1, 7500), '7.5K').draw(win)
	Text(Point(-1, 10000), '10.0K').draw(win)

	#Draw bar for initial principal
	height = principal * 0.02
	bar = Rectangle(Point(0, 0), Point(1, principal))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)

	#Draw bars for successive years
	for year in range(1,11):
		#calculate value for the next year
		principal = principal * (1 + apr)
		#draw bar for this value
		#x11 = year * 25 + 40
		#height = principal * 0.02
		bar = Rectangle(Point(year, 0), Point(year + 1, principal))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)

	input("Press <Enter> to quit")
	win.close()

main()