from datos import Datos
import re

class Juego():
    def __init__(self):
        self.temas = []
        self.enunciados = []
        self.alternativas = []
        self.ranking = []
        self.datos = Datos()
        #self.estadisticas = Estadisticas(self)
        #self.alfabeto = [range(A,Z)]
        self.tInicio = 0
        self.tFin = 0
        self.puntuacion = 0
        self.bloquesCompletados = 0
        self.bloquesCorrectos = 0
        self.bloquesFallidos = 0
        self.FALLOPORBLOQUE = 3
        self.FALLOPORTEMA = 2
        self.NUMENUNCIADOS = 5
        self.NUMTEMAS = 5
    
    def reiniciarEstadisticas(self):
        self.puntuacion = 0
        self.bloquesCompletados = 0
        self.bloquesCorrectos = 0
        self.bloquesFallidos = 0
        self.temaIdx = 0
        self.tInicio = 0
        self.tFin = 9

    def mostrarResultados(self):
        print("\nTrivial\n", end="")
        print("Estadísticas\n", end="")

        #if self.temas

    def nuevoJuego(self):
        repetir = True
        self.datos.obtTemas(self.temas, self.NUMTEMAS)
        self.reiniciarEstadisticas()
        #self.tInicio = nanotiempo
        while repetir:
            if self.bloquesFallidos >= self.FALLOPORBLOQUE:
                #self.tFin = 
                #self.mostrarResultados()
                repetir = False
            else:
                i = 0
                if len(self.temas) > 0:
                    print("\nTrivial\n------\n", end="")
                    print("Bloques fallidos: "+str(self.bloquesFallidos)+"/"+str(self.FALLOPORBLOQUE))

                    for tema in self.temas:
                        if not tema.completado:
                            print(str(i)+") "+tema.nombre)
                        i += 1
                    
                    ch = input("\nElija un tema: ")
                    patron=re.compile('[0-'+ str(i - 1) +']+')
                    if patron.match(ch):
                        if self.temas[i].completado:
                            print("El tema " + ch + ", ya está completado, por favor elija otro.\n")
                        else:
                            idx = self.temas[ch].id
                            pass