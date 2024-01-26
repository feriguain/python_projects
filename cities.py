# 2/23/23

cities = {
				'washington dc': {

				'country': 'united states',
				'population': 712816,
				'fact': 'It is the U.S capital and it is a compact city on the Potomatic river.',

				},

				'quebec': {

				'country': 'canadá',
				'population': 542298,
				'fact': 'Sits on the Saint Lawrence River. It is the mostly French-speaking province of the country.',

				},

				'new york': {

				'country': 'united states',
				'population': 8468000,
				'fact': 'Comprises 5 boroughs witting where the Hudson River meets the atlantic ocean.',

				},

				}

print("Here we have some of the most popular cities around the world:\n")

ciudades = [cities]

for ciudade in ciudades:
	for city, data in cities.items():
		country = f"{data['country'].title()}"
		city_population = f"{data['population']}"
		facts = f"{data['fact']}"

		print(f"{city.title()}:\n")
		print(f"It is located in: {country}.")
		print(f"The population of this city is: {city_population} people.")
		print(f"Here's an interesting fact about the city: {facts}\n\n")