import os
import random

class Juego:
    def __init__(self ,mapa, posicion_inicial, posicion_final):
        self.mapa= mapa
        self.posicion_inicial= posicion_inicial
        self.posicion_final= posicion_final

class JuegoArchivo(Juego):
    def __init__(self):
        lista= os.listdir("mapas/")
        nombre_archivo= random.choice(lista)
        with open("mapas/" + nombre_archivo, "r")as f:
            mapa = f.readlines()
        posicion_inicial = self.obtener_posicion_inicial(mapa)  
        posicion_final = self.obtener_posicion_final(mapa)  
        super().__init__(mapa, posicion_inicial, posicion_final)

    def obtener_posicion_inicial(self, mapa):
        pass   
        

    def obtener_posicion_final(self, mapa):
        pass


juego = JuegoArchivo()
print(juego.mapa)
print(juego.posicion_inicial)
print(juego.posicion_final)
 