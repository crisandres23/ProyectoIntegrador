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
os.system 
import readchar
keypress = readchar.readkey()
def terminal():
      os.system ("cls" if os.name =="nt" else "clear")

def main():
    print("presione la tecla UP. Para salir del bucle while")
    while True:
        char =readchar.readkey()
        print(f"Tecla presionada: {char}")
        #print(f"Tecla presionada: {char}")
        if char == readchar.key.UP:
            print("Presionaste la tecla UP. Saliendo del bucle")
        break
numero = 0

while numero <=50:
            terminal()
            print(f"Numero actual: {numero}")

            char = readchar.readkey()
            if char == "n":
                numero += 1
                if numero ==50:
                    terminal()
                    print("Llegaste al numero 50:")
                    break


