# 2/23/23 Nesting some info:

animals = {

				'pez': {
				'owner' : 'michael',
				'animal' : 'fish',
				'name' : 'goldie',
				'weight': '47 gr',
				'length' : '7 cm',
				'age': 3,
				},

				'perro' : {
				'owner' : 'martin',
				'animal' : 'dog',
				'name' : 'rubio',
				'weight' : '14 kg',
				'length' : '46 cm',
				'age' : 9,
				},

				'gato': {
				'owner' : 'benji',
				'animal' : 'cat',
				'name' : 'sushi',
				'weight' : '4 kg',
				'length' : '29 cm',
				'age' : 3,
				},

				'roedor': {
				'owner' : 'pedro',
				'animal' : 'hamster',
				'name' : 'mac',
				'weight' : '156 gr',
				'length' : '11 cm',
				'age' : 3,
				},

				}

pets = [animals]


for pet in pets:
	for pet, info in animals.items():
		print(f"\n{pet.title()}:")
		print(f"\tIt's owner's name is: {info['owner'].title()}.\n")
		print(f"\tIt's a: {info['animal'].title()}.\n")
		print(f"\tIt's name is: {info['name'].title()}.\n")
		print(f"\tIt's weight is: {info['weight']}.\n")
		print(f"\tIt's length is: {info['length']}.\n")
		print(f"\tIt's {info['age']} years old.\n")