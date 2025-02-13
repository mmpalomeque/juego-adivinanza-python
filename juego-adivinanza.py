
import random


numero_secreto = random.randint(1,101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("GAME OVER")
        break

    entrada = input("Introduce un número del 1 al 100: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones, has adivinado el número secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    cant_intentos += 1 #para que vaya aumentando la cantidad de intentos hasta llegar a 5
