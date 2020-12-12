from librerias import basic_shapes as bs
from librerias import easy_shaders as es
from librerias import scene_graph as sg
from librerias import transformations as tr
from OpenGL.GL import glClearColor


class Bordes(object):

    def __init__(self, nGrilla):
        self.nGrilla = nGrilla
        self.cuadrado = 2/self.nGrilla

        #aqui creamos la cosa en la gpu
        gpu_borde = es.toGPUShape(bs.createColorQuad(0.7, 0.7, 0.7))

        #creamos el rectangulo base vertical
        bordeVertical = sg.SceneGraphNode('bordeVertical')
        bordeVertical.transform = tr.scale(self.cuadrado, 2, 1)
        bordeVertical.childs += [gpu_borde]
        #base horizontal
        bordeHorizontal = sg.SceneGraphNode('bordeHorizontal')
        bordeHorizontal.transform = tr.scale(2, self.cuadrado, 1)
        bordeHorizontal.childs += [gpu_borde]

        # derecha
        bordeDerecho = sg.SceneGraphNode('bordeDerecho')
        bordeDerecho.transform = tr.translate(1,0,0)
        bordeDerecho.childs += [bordeVertical]

        # izquierda

        bordeIzquierdo = sg.SceneGraphNode('bordeIzquierdo')
        bordeIzquierdo.transform = tr.translate(-1,0,0)
        bordeIzquierdo.childs += [bordeVertical]

        # Arriba
        bordeArriba = sg.SceneGraphNode('bordeArriba')
        bordeArriba.transform = tr.translate(0, 1, 0)
        bordeArriba.childs+=[bordeHorizontal]

        # Abajo
        bordeAbajo = sg.SceneGraphNode('bordeAbajo')
        bordeAbajo.transform = tr.translate(0, -1, 0)
        bordeAbajo.childs+=[bordeHorizontal]

        # agrupamos todo en una sola figura
        bordeEntero = sg.SceneGraphNode('bordes')
        bordeEntero.childs += [bordeArriba,bordeDerecho,bordeAbajo,bordeIzquierdo]
        
        # con este trabajamos en caso que queramos cambiar las cosas
        bordeTransformada = sg.SceneGraphNode('bordesTR')
        bordeTransformada.childs += [bordeEntero] 
        
        self.model = bordeTransformada
        self.pos = 0

    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

