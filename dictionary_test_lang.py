# Working with dictionaries.

favorite_languages = {
				'jen' : 'python' ,
				'sarah' : 'c' ,
				'edward' : 'rust' ,
				'phil' : 'python' ,
				}

"""
language = favorite_languages['sarah'].title()
"""

#looping through the dictionary:


for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")


"""
print(f"Sarah's favorite language is {language}.")
"""

#Looping through the names of a poll:

for name in favorite_languages.keys():
	print(name.title())


users = ['pedro', 'jen', 'sarah', 'edward', 'phil', 'mark']

for name, language in favorite_languages.items():
	for user in users:
		if users in favorite_languages.items():
			print(f"Thank you {name.title()} for taking the poll.")
