
import glfw

class Controlador(object):
    def __init__(self):
        self.serpiente = None
        self.camara = None
    
    def setSerpiente(self, serpiente):
        self.serpiente = serpiente

    def setCamara(self, camara):
        self.camara = camara
           
    def hayChoque(self):
        return not self.serpiente.getEstado()

    def on_key(self, window, key, scancode, action, mods):

        camara = self.camara.get_vista_actual()

        if not (action == glfw.PRESS or action == glfw.RELEASE):
            return

        if key == glfw.KEY_ESCAPE:
            glfw.terminate()
            sys.exit()

        elif (key == glfw.KEY_LEFT or key == glfw.KEY_A) and action == glfw.PRESS:
            self.serpiente.setDireccion("Izquierda")
            print("izquierda")

        elif (key == glfw.KEY_RIGHT or key == glfw.KEY_D) and action == glfw.PRESS:
            self.serpiente.setDireccion("Derecha")
            print("derecha")

        elif (key == glfw.KEY_UP or key == glfw.KEY_W) and action == glfw.PRESS:
            self.serpiente.setDireccion("Arriba")
            print("arriba")

        elif (key == glfw.KEY_DOWN or key == glfw.KEY_S) and action == glfw.PRESS:
            self.serpiente.setDireccion("Abajo")
            print("abajo")

        elif (key == glfw.KEY_E) and action == glfw.PRESS:
            self.camara.set_vista_2d()
            print(self.camara.get_vista_actual())

        elif (key == glfw.KEY_R) and action == glfw.PRESS:
            self.camara.set_vista_fps()
            print(self.camara.get_vista_actual())

        elif (key == glfw.KEY_T) and action == glfw.PRESS:
            self.camara.set_vista_rts()
            print(self.camara.get_vista_actual())

        else:
            return     
