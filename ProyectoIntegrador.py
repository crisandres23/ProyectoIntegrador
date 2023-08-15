#Agregar nombre de jugador

nombre = input("Escriba su nombre: ")
apellido = input(f"Escriba su apellido, {nombre}: ")
print(f"Bienvenido, {nombre} {apellido}.")

#Proyecto integrador parte 2
print ("EMPEZEMOS!!!")

import readchar
keypress = readchar.readkey()
tecla = (input("presione una tecla:"))

while True:
    # Leer la tecla que se presiona
    tecla = readchar.readkey()
    # Imprimir la tecla en la pantalla
    print(tecla)
    # Comprobar si la tecla es la flecha hacia arriba
    if tecla == readchar.key.UP:
        # Asignar el valor de la tecla flecha arriba a la variable keypress
        keypress = readchar.key.UP
        # Salir del bucle
        break
    # Comprobar si la tecla es UP
    if tecla == readchar.key.UP:
        # Salir del bucle
        break
#parte 3 del proyecto
import os
import readchar

def borrar_e_imprimir(numero):
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"Numero actual: {numero}")

numero = 0
borrar_e_imprimir(numero)

while numero < 50:
    char = readchar.readkey()
    if char == "n":
        numero += 1
        borrar_e_imprimir(numero)
    elif char == readchar.key.UP:
        print("Presionaste la tecla UP. Saliendo del programa")
        break

print("Fin del programa")


