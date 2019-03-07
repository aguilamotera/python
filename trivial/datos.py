from tema import Tema
from enunciado import Enunciado
from alternativa import Alternativa

class Datos():
    def __init__(self):
        self.generarDatos()

    def generarDatos(self):
        self.crearTemas()
        self.crearEnunciados()
    
    def crearTemas(self):
        self.temas = []
        self.temas.append( Tema(1, "A") )
        self.temas.append( Tema(2, "B") )
        self.temas.append( Tema(3, "C") )
        self.temas.append( Tema(4, "D") )
        self.temas.append( Tema(5, "E") )
    
    def crearEnunciados(self):
        cont1 = 100
        cont2 = 100
        idx = 1
        self.enunciados = []
        self.alternativas = []

        for i in range(0,10):
            self.enunciados.append( Enunciado(cont1, idx, "Yo soy tema:" + str(idx) + " id:" + str(cont1) ))
            self.alternativas.append( Alternativa(cont2, cont1, "x", 1) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            cont1 += 1

        idx = 2
        for i in range(0,10):
            self.enunciados.append( Enunciado(cont1, idx, "Yo soy tema:" + str(idx) + " id:" + str(cont1) ))
            self.alternativas.append( Alternativa(cont2, cont1, "x", 1) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            cont1 += 1

        idx = 3
        for i in range(0,10):
            self.enunciados.append( Enunciado(cont1, idx, "Yo soy tema:" + str(idx) + " id:" + str(cont1) ))
            self.alternativas.append( Alternativa(cont2, cont1, "x", 1) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            cont1 += 1

        idx = 4
        for i in range(0,10):
            self.enunciados.append( Enunciado(cont1, idx, "Yo soy tema:" + str(idx) + " id:" + str(cont1) ))
            self.alternativas.append( Alternativa(cont2, cont1, "x", 1) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            cont1 += 1

        idx = 5
        for i in range(0,10):
            self.enunciados.append( Enunciado(cont1, idx, "Yo soy tema:" + str(idx) + " id:" + str(cont1) ))
            self.alternativas.append( Alternativa(cont2, cont1, "x", 1) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            self.alternativas.append( Alternativa(cont2, cont1, "m", 0) )
            cont2 += 1
            cont1 += 1

    def obtTemas(self, temas, num):
        temas = []
        for i in range(0,num):
            tema = Tema( self.temas[i].id, self.temas[i].nombre )
            self.temas.append( tema )

    def obtEnunciados(self, enunciados, id):
        enunciados = []
        for enunciado in self.enunciados:
            if enunciado.temaId == id:
                self.enunciados.append(enunciado)
    
    def obtAlternativas(self, alternativas, id):
        alternativas = []
        for alt in self.alternativas:
            if alt.enunciadoId == id:
                self.alternativas.append( alt )