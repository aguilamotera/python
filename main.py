

class MiClase():
    def __init__(self):
        self.unAtributo = 5
        print("hola clase padre")
    
    def unMetodo(self):
        print("hola")

#miClase = MiClase()
#miClase.unMetodo()

class OtraClase(MiClase):
    def __init__(self):
        self.otroAtributo = 3
        super().__init__()
    
    def unMetodo(self):
        print("ja")

otraClase = OtraClase()
otraClase.unMetodo()
