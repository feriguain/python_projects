# 2/24/23 Testing a code to ask how many people are eating in a restaurant.

people = input("Hello, how many are you gonna be? ")
number = int(people)

if number >= 8:
	print("\nSorry, you'll have to wait until a table gets free.")

else:
	print("\nOk, follow me this way please. Here's your table.")