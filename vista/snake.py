"""
Aqui se ejecuta el snake snake
"""
import glfw
from OpenGL.GL import *
import sys
from math import pi


from modelos.bordes import Bordes
from modelos.manzana import Manzana
from modelos.serpiente import Serpiente
from modelos.game_over import GameOver
from modelos.fondo import Fondo

from vista.camara import Camara

from controlador.controlador import Controlador
from librerias import easy_shaders as es
from librerias import lighting_shaders as ls


def SneakySnake(grilla=10,resolution=700):
    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = resolution
    height = resolution

    window = glfw.create_window(width, height, 'Sneaky Snake, ahora gordita', None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    controlador = Controlador()

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controlador.on_key)

    # Assembling the shader program (pipeline) with both shaders
    texturas = es.SimpleTextureModelViewProjectionShaderProgram()
    color = es.SimpleModelViewProjectionShaderProgram()
    luces = ls.SimpleGouraudShaderProgram()


    # Setting up the clear screen color
    glClearColor(245/255, 222/255, 179/255, 1.0)

    # Activates the depth as we are working in 3D
    glEnable(GL_DEPTH_TEST)
    
    # HACEMOS LOS OBJETOS
    camara = Camara(grilla)
    fondo = Fondo(grilla)
    borde = Bordes(grilla)
    manzana = Manzana(grilla)
    serpiente = Serpiente(grilla,manzana)
    gameOver = GameOver()
    controlador.setSerpiente(serpiente)
    controlador.setCamara(camara)

    t0 = 0
    
    

    while not glfw.window_should_close(window):  # Dibujando --> 1. obtener el input
 
        # Using GLFW to check for input events
        glfw.poll_events()  # OBTIENE EL INPUT --> CONTROLADOR --> MODELOS

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Camara
        vista = camara.get_vista()
        proyeccion = camara.get_proyeccion()

        manzana.draw(luces,proyeccion,vista)
        fondo.draw(texturas, proyeccion, vista)
        borde.draw(texturas, proyeccion, vista)
        serpiente.draw(texturas, proyeccion, vista)
        serpiente.comerManzana()
    
        # Calculamos el dt
        ti = glfw.get_time()
        margen = 0.35        
        dt = ti - t0

        if dt > margen:
            t0 = glfw.get_time()
            serpiente.movimientoPerpetuo()

        if controlador.hayChoque():
            gameOver.draw(texturas, proyeccion, vista)
            if dt > margen:
                gameOver.rotar(pi / 8)
                print("ITS OVER SNAKE")                
           

        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    glfw.terminate()
