from librerias import basic_shapes as bs
from librerias import easy_shaders as es
from librerias import scene_graph2 as sg
from librerias import transformations2 as tr
from OpenGL.GL import *

class GameOver(object):
    def __init__(self):
               
        gpu_ending = es.toGPUShape(bs.createTextureCube("recursos/gameover.png"), GL_REPEAT, GL_NEAREST)
        

        ending = sg.SceneGraphNode('Ending')
        ending.transform = tr.uniformScale(1.5)
        ending.childs = [gpu_ending]


        endingtr = sg.SceneGraphNode('EndingTR')
        endingtr.transform = tr.matmul([tr.translate(0, 0, 1), tr.scale(0.8,0.8, 0.8)])
        endingtr.childs = [ending]

        self.model = endingtr


    def draw(self, pipeline_texture, projection, view):
        glUseProgram(pipeline_texture.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "projection"), 1, GL_TRUE, projection)
        glUniformMatrix4fv(glGetUniformLocation(pipeline_texture.shaderProgram, "view"), 1, GL_TRUE, view)
        sg.drawSceneGraphNode(sg.findNode(self.model, 'EndingTR'), pipeline_texture)

    def rotar(self, angulo):
        self.model.transform = tr.matmul([self.model.transform, tr.rotationZ(angulo)])