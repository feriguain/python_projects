#29/12/22
#Test number one:

pizza_topping = "anchovies"

print("Is pizza_topping == 'anchovies'?")

print(pizza_topping == "anchovies")

print("If you asked for pizza_topping == 'mushrooms', we're out of it.")

print(pizza_topping == "mushrooms")


#Test number two:


print("Here we have two young mans who wants to go dance.")

age_0 = 23

age_1 = 17

print("\nAll we need is to know your ages.\n")

print("First you. Are you older than 18?")

if age_0 >= 18:
	print("Ok, you can enter.")
else:
	print("No, your under age. You have to leave.")

print("\nNow you. Are you older than 18?")

if age_1 >= 18:
	print("Ok, come on in.")
else:
	print("No, you can't go inside. You're a minor.")


#Test number 3:


answer_a = "Alonso"

answer_b = 7

answer_c = 41

print("Ok. First of all, here we have a few questions:\n")

print("What's the name of the spanish 2 times world champion in F1?\n")

print("My answer is: 'Carlos Sainz'\n")

answer_a = "Carlos Sainz"

if answer_a == "Alonso":
	print("that's correct. Nicely done!\n")
else:
	print("No, I'm sorry. That's not the correct answer.\n")

print("Now the second one. How many championships does Schumacher have?\n")

print("I would say '7'.\n")

answer_b = 7

if answer_b == 7:
	print("That's correct. Excellent\n")
else:
	print("No. Sorry but that's wrong.\n")

print("Well, this is the last one. How old is Fernando Alonso?\n")

answer_c = 43

print("He is 43 years old.\n")

if answer_c == 41:
	print("Correct! Nicely done.")
if answer_c != 41:
	print("I'm sory, but that is not right.")


#Last test:

banned_users = ["cristian", "pedro", "marie", "tommy"]

print("This is a programmed message to all the users:")

print("We have a certain list of banned people in this website.\n")

if "carlos" not in banned_users:
	print("Hi my name is Carlos, I would like to say hello to the group.\n")
else:
	print("Sorry, your nusername is banned, so you can't post in here.\n")

if "pedro" not in banned_users:
	print("Hi my name is Carlos, I would like to say hello to the group.")
else:
	print("Sorry, your nusername is banned, so you can't post in here.")
