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
from controlador.controlador import Controlador
from librerias import easy_shaders as es


def SneakySnake(grilla=10,resolution=700):
    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = resolution
    height = resolution

    window = glfw.create_window(width, height, 'Sneaky Snake', None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    controlador = Controlador()

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controlador.on_key)

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()
    pipeline_texturas = es.SimpleTextureTransformShaderProgram()

    # Telling OpenGL to use our shader program

    # Setting up the clear screen color
    glClearColor(245/255, 222/255, 179/255, 1.0)

    # Our shapes here are always fully painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


    #magia para que no se vea negro el png
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    # HACEMOS LOS OBJETOS
    borde = Bordes(grilla)
    manzana = Manzana(grilla)
    serpiente = Serpiente(grilla,manzana)
    gameOver = GameOver()


    t0 = 0
    controlador.setSerpiente(serpiente)
    print(serpiente.getPosicion())
    while not glfw.window_should_close(window):  # Dibujando --> 1. obtener el input



    
        # Using GLFW to check for input events
        glfw.poll_events()  # OBTIENE EL INPUT --> CONTROLADOR --> MODELOS

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        # Reconocer la logica

        # DIBUJAR LOS MODELOS
        
        glUseProgram(pipeline.shaderProgram)
        borde.draw(pipeline)
        serpiente.comerManzana()
        manzana.draw(pipeline)

        glUseProgram(pipeline_texturas.shaderProgram)
        serpiente.draw(pipeline_texturas)

        

        # Calculamos el dt
        ti = glfw.get_time()
        margen = 0.35
        
        dt = ti - t0


        if dt > margen:
            t0 = glfw.get_time()
            print(manzana.getPosicion())
            print(serpiente.getPosicion())
            print(str(2/grilla))
            serpiente.movimientoPerpetuo()


        if controlador.hayChoque():
            gameOver.draw(pipeline_texturas)
            gameOver.rotar(ti * (pi / 8))
            print("ITS OVER SNAKE")




        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    glfw.terminate()
