from partido import Partido

class Escrutinio():
    def __init__(self, numEscanios):
        self.numEscanios = numEscanios
        self.partidos = []

    def agregar(self, nombre, votos):
        self.partidos.append( Partido(nombre, votos) )
    
    def limpiarEscanios(self):
        for partido in self.partidos:
            partido.escanios = 0

    def asignarEscanios(self):
        self.limpiarEscanios()
        for i in range(0,self.numEscanios):
            max = 0
            indiceMax = 0
            j = 0
            for partido in self.partidos:
                cociente = partido.votos / (1 + partido.escanios)
                if(cociente > max):
                    max = cociente
                    indiceMax = j
                j=j+1
            
            self.partidos[indiceMax].escanios += 1