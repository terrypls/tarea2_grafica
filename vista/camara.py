import numpy as np
from librerias import transformations2 as tr

class Camara(object):

    def __init__(self, nGrilla):
        self.nGrilla = nGrilla
        self.cuadrado = 2 / self.nGrilla
        self.posicion = "rts"


    def get_vista(self):
        if self.posicion == "2d":
            vista = self.get_vista_2d()
        elif self.posicion == "rts":
            vista = self.get_vista_rts()
        elif self.posicion == "fps":
            vista = self.get_vista_fps()
        return vista

    def get_proyeccion(self):
        if self.posicion == "2d":
            proyeccion = self.get_proyeccion_2d()
        elif self.posicion == "rts":
            proyeccion = self.get_proyeccion_rts()
        elif self.posicion == "fps":
            proyeccion = self.get_proyeccion_fps()
        return proyeccion


    # Cosas del 2D
    def get_vista_2d(self):
        vista = tr.lookAt(
            np.array([self.cuadrado, self.cuadrado, 1 + self.cuadrado]),
            np.array([self.cuadrado, self.cuadrado, 0]),
            np.array([0, 1, 1]))
        return vista
    def get_proyeccion_2d(self):
        proyeccion = tr.ortho(-1 - self.cuadrado, 1 + self.cuadrado, -1 - self.cuadrado, 1 + self.cuadrado,
                              0.1, 50)
        return proyeccion

    #Cosas FPS


    def get_vista_fps(self):
        pass

    def get_proyeccion_fps(self):
        pass

    #Cosas RTS
    def get_vista_rts(self):
        vista = tr.lookAt(
            np.array([-1, -1, 1 + self.cuadrado]),
            np.array([0, 0, 0]),
            np.array([1, 1, 1]))
        return vista

    def get_proyeccion_rts(self):
        proyeccion = tr.perspective(95,1, 0.1, 10)
        return proyeccion

    #Setters
    def set_vista_2d(self):
        self.posicion = "2d"
        
    def set_vista_fps(self):
        self.posicion = "fps"
        
    def set_vista_rts(self):
        self.posicion = "rts"
        

    def get_vista_actual(self):
        return self.posicion