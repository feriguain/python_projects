# 2/17/23 Creating a list in a dictionary:

#Store info. about the pizza ordered.

pizza = {
				'crust': 'thick',
				'toppings': ['mushrooms', 'extra cheese'],
				}

# Summarize the order.

print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")