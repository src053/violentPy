# To find the multiples of 3 and 5 under 1000 and sum them together


def main():
	i = 1000
	total = 0
	count = 1

	while(count < i):
		if count % 3 == 0:
			total = total + count
			print(count, total)
		elif count % 5 == 0:
			total = total + count
			print(count, total)
		else:
			print(count , " is not a multiple of 3 or 5")

		count += 1
	print("The total is: ", total)

main()

