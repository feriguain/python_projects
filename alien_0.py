# 1/23/2023

alien_0 = {'color' : 'green',
			 'points' : '5'}


print(alien_0 ['color'])

print(alien_0 ['points'])

# Probando diferentes 'dictionary'

alien_b = {'height': '175 cm',
			'color': 'blue',
			'points': 20}


print(alien_b ['height'])
print(alien_b ['color'])

# Situacion: Player kills an alien, so we shown their points.

new_points = alien_b ['points']
print(f"You just earned {new_points} points!")

###

alien_c = {'color' : 'red',
			'points' : 35}

print(alien_c)

alien_c ['x_position'] = 0
alien_c ['y_position'] = 25

print(alien_c)