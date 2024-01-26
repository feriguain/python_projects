# 1/2/2023 bloque if_elif_else:

#Definimos variable de edad.

age = 12

#Creamos block.

if age < 4:
	price = 0

elif age < 18:
	price = 25

#Se pueden agregar aun mas elif si es necesario:

#En este caso, agregamos la edad de jubilados:

elif age >= 65:
	price = 20

#Podemos quitar el bloque else: simplemente ajustando el elif que querramos.

"""
else:
	price = 20
"""

#Creamos un solo mensaje para el block:

print(f"Your admission ticket cost is ${price}.")