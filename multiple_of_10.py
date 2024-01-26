# 2/24/23 Testing if the number give is or not a multiple of 10.

number = input("Please give us a number, so we can check if it's multiple of 10: ")
number = int(number)

if number % 10 == 0:
	print(f"\nThe number you choose is a multiple of 10.")

else:
	print(f"\nSorry that number is not a multiple of 10.")