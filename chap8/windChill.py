#Program will determine the wind chill

def windChill(wind, temp):
	#calculate wind chill
	return 35.74 + (0.6215 * temp) - (35.75 * (wind ** 0.16)) + 0.4275 * (wind ** 0.16)

def main():

	#var for wind speed
	wind = 0


	#print the top row
	print("-(-20)-(-10)-(0)-(10)-(20)-(30)-(40)-(50)-(60)")
	print("_______________________________________________")

	while wind < 50:
		#var for temp
		temp = -20
		#check that wind speed is above 3mph
		if wind > 3:
			