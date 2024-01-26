# 2/15/23 Still working w dictionaries:

rivers = {
				'nile' : 'egypt',
				'amazonas' : 'brazil',
				'rio de la plata' : 'argentina',
				}

"""
for rivers, countries in rivers.items():
	print(f"The {rivers.title()} runs through {countries.title()}.\n")
"""

for r, c in rivers.items():
	print(f"R: {r.title()}\n")
	print(f"C: {c.title()}\n")