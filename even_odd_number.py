# 2/24/23
# We are going to test a program that tells if a number it's even or odd.

number = input("Tell me a number, and I'll tell you if it's even or odd: ")

# we define the answer as an 'int' so we can work with it.

number = int(number)

# we test if it's even or odd.

if number % 2 == 0:
	print(f"\n{number} is even.")
else:
	print(f"\n{number} is odd.")