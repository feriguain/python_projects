# 2/15/23 working on dict:

favorite_languages = {
				'jen' : 'python' ,
				'sarah' : 'c' ,
				'edward' : 'rust' ,
				'phil' : 'python' ,
				}

users = ['pedro', 'jen', 'sarah', 'edward', 'phil', 'mark']


for name, language in favorite_languages.items():
	if users in favorite_languages.items():
		print(f"Thank you {name.title()} for taking the poll.")
	if users not in favorite_languages.items():
		print(f"Please {name.title()} take the poll.")