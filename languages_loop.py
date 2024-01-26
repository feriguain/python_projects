# 2/13/23 favorite_language extra excercise:

favorite_languages = {
				'jen' : 'python' ,
				'sarah' : 'c' ,
				'edward' : 'rust' ,
				'phil' : 'python' ,
				}


friends = ['jen', 'phil']

if 'erin' not in favorite_languages:
	print("Erin, please take our poll!")

for name in favorite_languages:
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")


for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking our poll!")

print("These languages have been mentioned:")

for language in set(favorite_languages.values()):
	print(language.title())