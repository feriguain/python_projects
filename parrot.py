# 2/24/23 Testing input() function.

"""
message = input("Tell me something and I will repeat it after you: ")

print(message)

name = input("Please enter your name: ")

print(f"Hello, {name}!")


prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
"""

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
 message = input(prompt)
 print(message)