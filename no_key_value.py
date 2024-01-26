# Testing no_key_value error.

alien_0 =				{
				'color' : 'green' ,
				'speed' : 'slow',
				}

#This will return a KeyError:

point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)

"""

print(alien_0['points'])

"""