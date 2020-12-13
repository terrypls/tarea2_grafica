from librerias import basic_shapes as bs
from librerias import easy_shaders as es
from librerias import scene_graph2 as sg
from librerias import transformations2 as tr
from OpenGL.GL import *

class Fondo(object):

    def __init__(self, nGrilla):
        self.nGrilla = nGrilla
        self.cuadrado = 2 / self.nGrilla
        
        path_imagen = 'recursos/pasto.png'

        gpu_fondo = es.toGPUShape(bs.createTextureCube(path_imagen), GL_REPEAT, GL_NEAREST)

        fondo = sg.SceneGraphNode('fondo')
        fondo.transform = tr.matmul([tr.scale(2, 2, self.cuadrado), tr.translate(0, 0, -1)])
        fondo.childs += [gpu_fondo]
        
        fondoTr = sg.SceneGraphNode("fondoTr")
        fondoTr.childs += [fondo]
        
        self.model = fondoTr

    def draw(self, pipeline_texture, projection, view):
        glUseProgram(pipeline_texture.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "projection"), 1, GL_TRUE, projection)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "view"), 1, GL_TRUE, view)
        sg.drawSceneGraphNode(sg.findNode(self.model, 'fondoTr'), pipeline_texture)
        
            
