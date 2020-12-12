import sys

from vista.snake import SneakySnake

grilla = 10

if len(sys.argv) > 2:
    grilla = int(sys.argv[1])
    resolucion = int(sys.argv[2])

elif len(sys.argv) > 1:
    grilla = int(sys.argv[1])
    resolucion = 700

else:
    grilla = 10
    resolucion = 700

print("Tamaño del juego es de " + str(grilla) + "x" + str(grilla))
print("Resolución: " + str(resolucion)+"x"+str(resolucion))

SneakySnake(grilla)   