# 2/17/23 Nesting:

alien_0 = {'color' : 'red', 'points' : 5}
alien_1 = {'color' : 'blue', 'points' : 10}
alien_2 = {'color' : 'yellow', 'points' : 15}

# After creating the dictionaries, we nest them.

aliens = [alien_0, alien_1, alien_2]

# With the list, we loop through it. To get the info.

for alien in aliens:
	print(alien)