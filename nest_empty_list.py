# 2/17/23 Nesting with empty list.

# Make an empty list for storing data.

aliens = []

# Make 30 green aliens.

for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

# We change first 3 aliens info.

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'

for alien in aliens[9:]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 20

# Show the first 5 aliens.

for alien in aliens[:5]:
	print(alien)
print("...")

for alien in aliens[7:]:
	print(alien)

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")