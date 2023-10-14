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
#Parte 4
import os
import keyboard

def terminal():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" * 100)

def limpiar_pantalla(matriz):
    os.system("cls")
    for fila in matriz:
        print("".join(fila))

def convertir_mapa(mapa):
    
    mapa = mapa.strip()
    filas = mapa.split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz

def posicion_inicial(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == "P":
                posicion_inicial = (i, j)
            elif laberinto[i][j] == "E":
                posicion_final = (i, j)
    return posicion_inicial, posicion_final

def limpiar_y_mostrar(matriz, px, py):
    terminal()
    for fila in matriz:
        print("".join(fila))
    matriz[py][px] = "P"

mapa = """
####################
#P...............###
#.#.##############.#
#.#..............#.#
#.#.#..#########.#.#
#.#.#..........#.#.#
#.#.#.########.#.#.#
#.#.#.#......#.#.#.#
#.#.#.#.####.#.#.#.#
#...#...#..#...#...#
#.#####.##.##.#####.
#.....#....#.....#.#
#####.######.#####.#
#.....#....#.....#.#
#.#####.##.##.#####.
#...#...#..#...#.###
#.###.#.####.#.#...#
#...#.#......#.#.###
#.###.#.####......E#
"""

matriz = convertir_mapa(mapa)
posicion_inicial, posicion_final = posicion_inicial(matriz)
px, py = posicion_inicial

salir = False

while (px, py) != posicion_final and matriz[py][px] != "#":
    if keyboard.is_pressed("up"):
        if py > 0 and matriz[py-1][px] != "#":
            matriz[py][px] = "."
            py -= 1
            matriz[py][px] = "P"
            posicion_inicial = (px, py)  # Actualizar la posición inicial
        limpiar_y_mostrar(matriz, px, py)
    elif keyboard.is_pressed("down"):
        if py < len(matriz) - 1 and matriz[py+1][px] != "#":
            matriz[py][px] = "."
            py += 1
            matriz[py][px] = "P"
            posicion_inicial = (px, py)  # Actualizar la posición inicial
        limpiar_y_mostrar(matriz, px, py)    
    elif keyboard.is_pressed("left"):
        if px > 0 and matriz[py][px-1] != "#":
            matriz[py][px] = "."
            px -= 1
            matriz[py][px] = "P"
            posicion_inicial = (px, py)  # Actualizar la posición inicial
        limpiar_y_mostrar(matriz, px, py)    
    elif keyboard.is_pressed("right"):
        if px < len(matriz[0]) - 1 and matriz[py][px+1] != "#":
            matriz[py][px] = "."
            px += 1
            matriz[py][px] = "P"
            posicion_inicial = (px, py)  # Actualizar la posición inicial
        limpiar_y_mostrar(matriz, px, py)
    
    if salir:
            break

print("¡Felicidades! ¡Lograste salir del laberinto!")

