'''
    Se pueden agregar condiciones intermedias entre if y else
    tambien conocidas como elif.

    Su sinthax es la siguiente:
    if age = 19:
        print("hola")
    elif age < 15:
        print("non")
    else:
        print("nopo")
'''

name = input ("Cual es tu nombre ? ") # Cual es el nombre de la persona
age = int (input ("Que edad tienes ? ")) # cual es su edad (importante)

if age > 18: # Primera condición : Si es mayor a 18, puede entrar 
    print("Bienvenido al concierto de Jaguares, puedes pasar !") # fin del primer bloque
elif age == 18:
    print("Tienes que ir al concierto de Zoe !")
else:  # else es mi condicion negativa, si no puede pasar tendra que irse 
    print("Lo siento, no puedes entrar...tendras que irte ") # fin del segundo bloque

