# 2/15/23 ejercicio aleatorio probando key-value pairs:

# we take info. from a poll we made:

user_data = {
				'name' : 'coraline',
				'last name' : 'iguain',
				'age' : '19',
				'place you were born' : 'china',
				}


for q, a in user_data.items():
	print(f"\t\nQuestion: {q.title()}?\nAnswer: {a.title()}\n")
