# 2/13/23 KeyValue excercise:

"""
person = {
				'first name' : 'Benjamin',
				'last name' : 'Dinallo',
				'age' : 21 ,
				'city' : 'mar del plata',
				}

print(person['first name'])
print(person['last name'])
print(person['age'])
print(person['city'])
"""

# 2/17/23 Working with an old exc. (new learning)

persons = {
				'benji': {
				'first' : 'benjamin',
				'last' : 'dinallo',
				'age' : 21 ,
				'location' : 'mar del plata',
				},

				'mykie': {
				'first': 'myke',
				'last': 'myers',
				'age': 35,
				'location': 'ee.uu',
				},

				'tonnyh': {
				'first': 'tony',
				'last': 'hawk',		
				'age': 51,
				'location': 'california',
				},

				}

people = [persons]


for people in people:
	for user, user_data in persons.items():
		username = f"{user}"
		full_name = f"{user_data['first']} {user_data['last']}"
		age = f"{user_data['age']}"
		location = f"{user_data['location']}"
		print(f"\nUsername: {username}")
		print(f"\tFull name: {full_name.title()}")
		print(f"\tAge: {age}")
		print(f"\tLocation: {location.title()}")

