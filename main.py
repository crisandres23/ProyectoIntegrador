from juego_archivo import JuegoArchivo

if __name__ == "__main__":
    mapa = "mapas/"


    nombre = input("Escriba su nombre: ")
    apellido = input(f"Escriba su apellido, {nombre}: ")
    print(f"Bienvenido, {nombre} {apellido}.")

    juego = JuegoArchivo(mapa)
    juego.terminal()
    #print(juego.matriz_maze)
    juego.jugar()