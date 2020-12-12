
import glfw

class Controlador(object):
    def __init__(self):
        self.serpiente = None
    
    def setSerpiente(self, serpiente):
        self.serpiente = serpiente

    def hayChoque(self):
        return not self.serpiente.getEstado()

    def on_key(self, window, key, scancode, action, mods):
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

        else:
            return     
