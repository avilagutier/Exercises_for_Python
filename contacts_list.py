'''
    Este pequeño programa es un indentificador de invitados en una lista de nombre

'''

invitados_mario= ["luis", "Antoine", "Estelle", "Olivier", "Alex", "Romain", "Katia", "Papa", "Mama", "Python"]

contacto = input("Cual es tu nombre, por favor ? ")

if contacto in invitados_mario:
    print("Hola!, pasa por favor ")
else:
    print("No estas en la lista ! " )

