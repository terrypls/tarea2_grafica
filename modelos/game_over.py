from librerias import basic_shapes as bs
from librerias import easy_shaders as es
from librerias import scene_graph as sg
from librerias import transformations as tr
from OpenGL.GL import GL_REPEAT,GL_NEAREST

class GameOver(object):
    def __init__(self):
        gpu_ending = es.toGPUShape(bs.createTextureQuad("recursos/gameover.png"), GL_REPEAT, GL_NEAREST)


        ending = sg.SceneGraphNode('Ending')
        ending.transform = tr.uniformScale(2)
        ending.childs = [gpu_ending]


        endingtr = sg.SceneGraphNode('EndingTR')
        endingtr.childs = [ending]

        self.model = endingtr


    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

    def rotar(self, angulo):
        self.model.transform = tr.rotationZ(angulo)