import gc

"""
Listas lineales simplemente enlazadas (llse)
"""

class Envoltorio:
    def __init__(self, valor):
        self.v = valor

class Nodo:
    def __init__(self):
        self.dato = None
        self.sig = None

def main():
    p = Envoltorio(None)
    # La asignación de memoria se haría así.
    p.v = Nodo()
    p.v.sig = None
    del p.v; gc.collect
    p = None

main()