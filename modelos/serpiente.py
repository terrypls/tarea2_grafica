from librerias import transformations2 as tr
from librerias import basic_shapes as bs
from librerias import scene_graph2 as sg
from librerias import easy_shaders as es

from OpenGL.GL import *
from math import pi

class Serpiente(object):
    

    def __init__(self, nGrilla, manzana):
        self.nGrilla = nGrilla
        self.cuadrado = 2 / self.nGrilla
        self.estado = True
        self.direccion = "Izquierda"
        self.manzana = manzana
        

        gpu_cuerpo = es.toGPUShape(bs.createTextureCube("recursos/question_box.png"), GL_REPEAT, GL_NEAREST)
        gpu_cara = es.toGPUShape(bs.createTextureCube("recursos/Metal_Gear_MSX_Snake_sprite.png"), GL_REPEAT, GL_NEAREST)

        cuerpo = sg.SceneGraphNode("cuerpo")
        cuerpo.transform = tr.matmul([tr.scale(1, 1, 1), tr.translate(0, 0, 0)])
        cuerpo.childs += [gpu_cuerpo]

        cabeza = sg.SceneGraphNode("cabeza")
        cabeza.transform = tr.matmul([tr.scale(0.95, 0.95, 0.95), tr.translate(0.1, 0, 0)])
        cabeza.childs += [gpu_cara]



        snake = sg.SceneGraphNode('Snake')
        snake.transform = tr.scale(self.cuadrado, self.cuadrado, self.cuadrado)
        snake.childs = [cabeza]
        
        snaketr = sg.SceneGraphNode('SnakeTR')
        snaketr.childs = [snake]

        self.model = snaketr

        self.delta = 0
        if self.nGrilla % 2 == 0:
            self.delta = self.cuadrado/2


        self.pos_x = self.delta
        self.pos_y = self.delta
        
        self.model.transform = tr.matmul([tr.translate(self.delta, self.delta, 0), tr.rotationZ(pi / 2)])


    def draw(self, pipeline_texture, projection, view):
        glUseProgram(pipeline_texture.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "projection"), 1, GL_TRUE, projection)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "view"), 1, GL_TRUE, view)
        sg.drawSceneGraphNode(sg.findNode(self.model, 'SnakeTR'), pipeline_texture)

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
        muralla = 1 - self.cuadrado
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
            