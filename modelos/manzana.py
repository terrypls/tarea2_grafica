from librerias import transformations as tr
from librerias import basic_shapes as bs
from librerias import scene_graph as sg
from librerias import easy_shaders as es

from OpenGL.GL import glClearColor
from random import randint


class Manzana(object):

    def __init__(self,nGrilla):
        self.nGrilla = nGrilla
        self.cuadrado = round(2/self.nGrilla,4)


        gpu_manzana = es.toGPUShape(bs.createColorQuad(220/255, 30/255, 40/255))
        gpu_palito = es.toGPUShape(bs.createColorQuad(139/255,69/255,19/255))
        gpu_hoja = es.toGPUShape(bs.createColorQuad(0,100/255,0))

        # cuerpo de la manzana
        cuerpo = sg.SceneGraphNode('Cuerpo')
        #cuerpo.transform = tr.matmul([tr.scale(self.cuadrado, self.cuadrado, 0),tr.translate(0,0,0)])
        cuerpo.childs = [gpu_manzana]

        palito = sg.SceneGraphNode('Palito')
        palito.transform = tr.translate(0,1,0)
        palito.childs = [gpu_palito]

        palitotr = sg.SceneGraphNode('Palitotr')
        palitotr.transform = tr.scale(0.2, 0.65, 0)
        palitotr.childs = [palito]

        hojita = sg.SceneGraphNode('Hojita')
        hojita.transform = tr.matmul([tr.scale(0.4,0.15,0),tr.translate(0.5,5,0)])
        hojita.childs = [gpu_hoja]

        hojita1 = sg.SceneGraphNode('Hojita1')
        hojita1.transform = tr.matmul([tr.scale(0.4, 0.15, 0), tr.translate(0.3, 5.2, 0)])
        hojita1.childs = [gpu_hoja]
        
        hojita2 = sg.SceneGraphNode('Hojita2')
        hojita2.transform = tr.matmul([tr.scale(0.4, 0.15, 0), tr.translate(0.3, 4.8, 0)])
        hojita2.childs = [gpu_hoja]

        manzana = sg.SceneGraphNode('Manzana')
        manzana.transform = tr.scale(self.cuadrado/2,self.cuadrado/2,0)
        manzana.childs = [ hojita,hojita1,hojita2,palitotr,cuerpo]
        
        manzanatr = sg.SceneGraphNode('Manzanatr')
        
        manzanatr.childs= [manzana]

        self.model = manzanatr
        self.delta = 0
        self.pos_x = 0
        self.pos_y = 0
        
        if self.nGrilla %2 ==0:
            
            self.model.transform = tr.translate(self.cuadrado + self.getRandomPosition(),self.cuadrado + self.getRandomPosition(),0)
        else:
            self.delta = self.cuadrado
            
            self.model.transform = tr.translate(self.cuadrado / 2 + self.getRandomPosition(),self.cuadrado / 2 + self.getRandomPosition(),0)
        



    #aqui empezamos a dibujar la manzana
    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

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