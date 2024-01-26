# 2/23/23 

favorite_places = {

				'exe': {
				'most_vstd': 'brazil',
				'rct_vstd': 'uruguay',
				'wouldlovetovst': 'tokyo',
				'favorite': 'germany',

				},

				'majito': {
				'most_vstd': 'jujuy',
				'rct_vstd': 'mendoza',
				'wouldlovetovst': 'luxemburgo',
				'favorite': 'belgica',

				},

				'benji': {
				'most_vstd': 'palma de mallorca',
				'rct_vstd': 'alcudia',
				'wouldlovetovst': 'paris',
				'favorite': 'mar del plata',

				},

				'gonza': {
				'most_vstd': 'dolores',
				'rct_vstd': 'chile',
				'wouldlovetovst': 'switzerland',
				'favorite': 'leitschester',

				},

				}

friends_fav_places = [favorite_places]


for friends_fav_place in friends_fav_places:
	for name, city in favorite_places.items():
		print(f"\n{name.title()}:\n")
		print(f"Most visited place's: {city['most_vstd'].title()}\n")
		print(f"Recently visted {city['rct_vstd'].title()}.\n")
		print(f"Says that he/she would love to visit {city['wouldlovetovst'].title()}.\n")
		print(f"Once said that he/she favorite place's {city['favorite'].title()}.\n")