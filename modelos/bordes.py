from librerias import basic_shapes as bs
from librerias import easy_shaders as es
from librerias import scene_graph2 as sg
from librerias import transformations2 as tr
from OpenGL.GL import *

from math import pi

class Bordes(object):

    def __init__(self, nGrilla):
        self.nGrilla = nGrilla
        self.cuadrado = 2/self.nGrilla

        path_imagen = "recursos/bricks.jpg"

        #aqui creamos la cosa en la gpu
        gpu_bloque = es.toGPUShape(bs.createTextureCube(path_imagen), GL_REPEAT, GL_NEAREST)

        bloque = sg.SceneGraphNode("Bloque")
        bloque.transform = tr.matmul([tr.scale(self.cuadrado,self.cuadrado,self.cuadrado),tr.translate(0,0,0)])
        bloque.childs += [gpu_bloque]
        
        largo = self.cuadrado / 2
        i = largo - 1
        
        muralla_list=[]
        while i <1:
            murallas = sg.SceneGraphNode("bloque_" + str(i))
            murallas.transform = tr.translate(1 - largo, i, 0)
            murallas.childs += [bloque]
            muralla_list.append(murallas)
            i += self.cuadrado

        larguero = sg.SceneGraphNode("Muralla")
        larguero.transform = tr.identity()
        larguero.childs += muralla_list

        bordes = sg.SceneGraphNode("bordes")
        bordes.transforms = tr.identity()
        bordes_list = []
        for i in range(0, 4):
            muro = sg.SceneGraphNode("muro" + str(i))
            muro.transform = tr.rotationZ(i * pi / 2)
            muro.childs += [larguero]
            bordes_list.append(muro)


        bordes.childs += bordes_list
        
        self.model = bordes
        print("se creo una muralla :D")

        

    def draw(self, pipeline_texture, projection, view):
        glUseProgram(pipeline_texture.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "projection"), 1, GL_TRUE, projection)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "view"), 1, GL_TRUE, view)
        sg.drawSceneGraphNode(sg.findNode(self.model, 'bordes'), pipeline_texture)

