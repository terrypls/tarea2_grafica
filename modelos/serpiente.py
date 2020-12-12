from librerias import transformations as tr
from librerias import basic_shapes as bs
from librerias import scene_graph as sg
from librerias import easy_shaders as es

from OpenGL.GL import *

class Serpiente(object):
    

    def __init__(self, nGrilla, manzana):
        self.nGrilla = nGrilla
        self.cuadrado = 2 / self.nGrilla
        self.estado = True
        self.direccion = "Derecha"
        self.manzana = manzana
        

        gpu_serpiente = es.toGPUShape(bs.createTextureQuad("recursos/snake.png"), GL_REPEAT, GL_NEAREST)

        snake = sg.SceneGraphNode('Snake')
        snake.transform = tr.matmul([tr.scale(self.cuadrado, self.cuadrado, 0),tr.translate(0,0,0)])
        snake.childs = [gpu_serpiente]
        
        snaketr = sg.SceneGraphNode('SnakeTR')
        snaketr.childs = [snake]


        self.model = snaketr

        if self.nGrilla %2 ==0:
            self.pos_x = 0
            self.pos_y = 0
        else:
            self.pos_x = self.cuadrado / 2
            self.pos_y = self.cuadrado / 2
            self.model.transform = tr.translate(self.cuadrado/2,self.cuadrado/2,0)


    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getPosicion(self):
        return [self.pos_x,self.pos_y]

    def actualizarPosicion(self):
        self.model.transform = tr.translate(self.pos_x, self.pos_y, 0)

    def getEstado(self):
        return self.estado

    def izquierda(self):
            if self.estado:
                self.direccion = "Izquierda"
                
                self.pos_x -= self.cuadrado
                self.actualizarPosicion()
    
    def derecha(self):
            if self.estado:
                self.direccion = "Derecha"
                self.pos_x += self.cuadrado
                self.actualizarPosicion()

    def arriba(self):
            if self.estado:
                
                self.direccion = "Arriba"
                self.pos_y += self.cuadrado
                self.actualizarPosicion()

    def abajo(self):
            if self.estado:
                self.direccion = "Abajo"
                
                self.pos_y -= self.cuadrado
                self.actualizarPosicion()

    def movimientoPerpetuo(self):
        if not self.choque():
            if self.direccion == "Izquierda":
                self.izquierda()
            if self.direccion == "Derecha":
                self.derecha()
            if self.direccion == "Arriba":
                self.arriba()
            if self.direccion == "Abajo":
                self.abajo()


    def choque(self):
        muralla = 1 - self.cuadrado/2
        if self.pos_x >= muralla or self.pos_x <= -muralla or self.pos_y >= muralla or self.pos_y <= -muralla :
            self.estado = False
            print("chocamos D:")
            return True
        else:

            return False
        
    
    def comerManzana(self):
        posicionLocal = self.getPosicion()
        posicionManzana = self.manzana.getPosicion()
        x = abs(posicionManzana[0] - posicionLocal[0])
        y = abs(posicionManzana[1]- posicionLocal[1])
        
        if x <= (self.cuadrado / 2) and y <= (self.cuadrado / 2):
            print("rica manzanita")
            self.manzana.respawn()
            