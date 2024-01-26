#12/28/22 Chapter 5 If examples:

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

#Este codigo permitira resaltar el valor 'bmw' en caso de que este en la lista.