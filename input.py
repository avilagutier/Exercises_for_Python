# Comentarios en Python o
'''
    comentario prolongado en Python
'''

# Primera parte del programa de Python en cuanto a la programación de una frase

m = "Bienvenido a tu curso de Python"
print(m)


'''
    Input : permite al usuario escribir en una linea de input en el tablero
    ex : s = input ()
'''

name = input("Cual es tu nombre ? ") #Permite al usuario poner el nombre que se desea
print("Hola " + name) #Imprime la linea que puso el usuario 


n = (input("Cuantos años tienes ? ")) #El usuario puede indicar su edad 
print(n + " años" + " Ya estas viejo!!!") #El tablero puede interactuar con el

'''
    input siempre regresa una string, pero si se requiere un regreso numerico, se necesita convertir
    apropiadamente el tipo en int(), float() o complex()
'''

a = int(input("A que adivino en que numero piensas : "))
print(a + 7)
print("Es el numero que pensaste ?")



