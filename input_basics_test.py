# 2/24/23 Testing input() program. Check!

name_gvn = input("Hi, what's your name? ")

message = (f"Hello, {name_gvn}")

print(message)

age = input("How old are you? ")

prompt = input(f"So you are {age} old? ")

age = int(age)

if age >= 18:
	print("You are old enough to vote.")
	final_msg = input("Who are you planning to vote? ")
	print(f"So, you're voting {final_msg}. Good for you!")

else:
	print(f"Sorry {name_gvn}, you're not old enough to vote.")
