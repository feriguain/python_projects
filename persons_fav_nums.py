# 2/13/23 persons fav. numbers:

# 2/23/23 Retaking this excercise to apply last learnings.
# 2/23/23 More numbers added to each person:

favorite_numbers = {
				'pedro' : [6, 23, 5, 75],
				'martin' : [21, 23, 71, 9],
				'matias' : [8, 27, 33, 99],
				'lucas' : [7, 1, 12, 34],
				'exequiel' : [99, 24, 121, 11],
				}

# 2/15/23 looping into the dict. to avoid multiple print() calls:

"""
print(f"Pedro's favorite number is {favorite_numbers['pedro']}.")
print(f"Martin's favorite number is {favorite_numbers['martin']}.")
print(f"Matias's favorite number is {favorite_numbers['matias']}.")
print(f"Lucas's favorite number is {favorite_numbers['lucas']}.")
print(f"Lara's favorite number is {favorite_numbers['lara']}.")
"""

print("So after taking the poll, these were the answers:\n")

for persons, fav_numbers in favorite_numbers.items():
	print(f"{persons.title()} choose the following numbers:\n{fav_numbers}\n")

