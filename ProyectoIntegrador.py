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



