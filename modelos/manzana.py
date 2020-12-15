from librerias import transformations2 as tr
from librerias import basic_shapes as bs
from librerias import scene_graph2 as sg
from librerias import easy_shaders as es
from librerias.obj_reader import readOBJ

from OpenGL.GL import *
from random import randint, random

from math import pi

class Manzana(object):

    def __init__(self,nGrilla):
        self.nGrilla = nGrilla
        self.cuadrado = round(2 / self.nGrilla, 4)
        
        path_imagen = 'recursos/carrot.obj'
        gpu_manzana = es.toGPUShape(shape=readOBJ(path_imagen, (200/255, 20 / 255, 20 / 255)))

        manzana = sg.SceneGraphNode("cuerpo")
        manzana.transform = tr.matmul([tr.uniformScale(self.cuadrado), tr.rotationX(pi / 2)])
        manzana.childs+=[gpu_manzana]
        
        manzanatr = sg.SceneGraphNode('Manzanatr')
        manzanatr.childs= [manzana]

        self.delta = 0
        if self.nGrilla % 2 == 0:
            self.delta = self.cuadrado/2

        self.model = manzanatr
        self.consumidas = 0
        self.respawn()
        self.consumidas = 0
        self.r =0
        self.g =0.5
        self.b = 0.5
        self.brillo = 100
        self.altura=10

        

    
    #aqui empezamos a dibujar la manzana
    def draw(self, pipeline_light, projection, view):
        self.iluminacion(pipeline_light,view)
        glUseProgram(pipeline_light.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_light.shaderProgram, "projection"), 1, GL_TRUE, projection)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_light.shaderProgram, "view"), 1, GL_TRUE, view)
        sg.drawSceneGraphNode(sg.findNode(self.model, 'Manzanatr'), pipeline_light)

    def actualizarPosicion(self):
        self.model.transform = tr.translate(self.pos_x, self.pos_y, 0)
        
    def getPosicion(self):
        return [self.pos_x,self.pos_y]

    def getRandomPosition(self):
        borde = int((self.nGrilla - 2) / 2)
        if self.nGrilla  % 2 == 0:
            borde = borde - 1
        random = randint(-borde,borde)
        return random*self.cuadrado

    def nuevosEjes(self):
            self.pos_x = round(self.delta  + self.getRandomPosition(),3)
            self.pos_y = round(self.delta + self.getRandomPosition(),3)
            
    def respawn(self):
        self.nuevosEjes()
        self.actualizarPosicion()
        self.consumidas += 1
        print(self.consumidas)
        if self.consumidas % 3 == 0 and self.consumidas != 0:
            self.cambiar_color()


    def cambiar_color(self):
        self.r = random()
        self.g = random()
        self.b = random()
        self.brillo= randint(0,100)

        print("r "+str(self.r)+" g "+str(self.g)+" b "+str(self.b)+", brillo: "+str(self.brillo)+" altura: "+str(self.altura))
        
        

    def iluminacion(self,pipeline_light, view):
        camera_view = view[0]
        glUseProgram(pipeline_light.shaderProgram)
        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "La"), 1.0, 1.0, 1.0)
        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "Ld"), 1.0, 1.0, 1.0)
        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "Ls"), 1.0, 1.0, 1.0)

        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "Ka"), self.r, self.r, self.r)
        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "Kd"),self.g, self.g, self.g)
        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "Ks"), self.b, self.b, self.b)

        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "lightPosition"), 0, 0, self.altura)
        glUniform3f(glGetUniformLocation(pipeline_light.shaderProgram, "viewPosition"), camera_view[0],
                    camera_view[1], camera_view[2], )
        glUniform1ui(glGetUniformLocation(pipeline_light.shaderProgram, "shininess"), self.brillo)
        glUniform1f(glGetUniformLocation(pipeline_light.shaderProgram, "constantAttenuation"), 0.001)
        glUniform1f(glGetUniformLocation(pipeline_light.shaderProgram, "linearAttenuation"), 0.1)
        glUniform1f(glGetUniformLocation(pipeline_light.shaderProgram, "quadraticAttenuation"), 0.01)
        glUniform1f(glGetUniformLocation(pipeline_light.shaderProgram, "quadraticAttenuation"), 0.01)