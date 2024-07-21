edad = 15
if edad >=0 and edad<5:
    print("esta es la primera estancia")
elif edad>=5 and edad<12:
    print("esta es la infancia")
elif edad>=12 and edad<=19:
    print("esta en la adolecencia")
elif edad>=19 and edad<=30:
    print("esta en la juventud")
elif edad>=30 and edad<=65:
    print("esta en la adultez")
elif edad>65:
    print("es abuelo")
    # inputs
edad2 = int(input("insertar edad:"))
edad2 = edad2 +3
print(edad2)