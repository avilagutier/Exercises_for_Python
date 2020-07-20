# Los condicionales le daran estructura a mi codigo, esto se emplea cada día en cuanto a la toma de decisiones

# Synthax if / else

'''
if <expr>:
    <statement>
else:
    <statement>
'''

name = input ("Cual es tu nombre ? ") # Cual es el nombre de la persona
age = int (input ("Que edad tienes ? ")) # cual es su edad (importante)

if age > 18: # Primera condición : Si es mayor a 18, puede entrar 
    print("Bienvenido, puedes pasar") # fin del primer bloque
else:  # else es mi condicion negativa, si no puede pasar tendra que irse 
    print("Lo siento, no puedes entrar...tendras que irte ") # fin del segundo bloque

    


