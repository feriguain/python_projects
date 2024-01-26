# 1/19/2023 Probando mas de una lista:

available_toppings = ["mushrooms", "olives", "green pepper", 
					"pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

#With this lists, we write a code to complete the pizza.

for requested_topping in requested_toppings:

	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")

	else:
		print(f"Sorry we don't have {requested_topping}.")

print("\nFinished making your pizza!")