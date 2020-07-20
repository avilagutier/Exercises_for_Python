'''
    Este pequeño programa es un indentificador de invitados en una lista de nombre

'''

invitados_mario= ["luis", "Antoine", "Estelle", "Olivier", "Alex", "Romain", "Katia", "Papa", "Mama", "Python"]

contacto = input("Cual es tu nombre, por favor ? ")

if contacto == "Katia" :
    print("Hola chata !, pasa por favor ")
    input("Cual es tu nombre, por favor ? ")
elif contacto == "Antoine" :
    print("Hola Pollito !, pasa por favor ")
    input("Cual es tu nombre, por favor ? ")
elif contacto == "Estelle" :
    print("Coucou Estelle !, pasa por favor ")
    input("Cual es tu nombre, por favor ? ")
elif contacto == "Olivier" :
    print("Hola Oliv !, pasa por favor ")
    input("Cual es tu nombre, por favor ? ")
else:
    print("No estas en la lista ! " )
    input("Cual es tu nombre, por favor ? ")
