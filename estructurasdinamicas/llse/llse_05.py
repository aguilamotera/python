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

def tamanio(q):
    n = 0
    while q != None:
        n += 1
        q = q.sig
    return n

def aniadir(i, x, listaRef):
    n = 0
    anterior = pRef.v
    actual = pRef.v
    numDeElementos = tamanio(pRef.v)
    if i > numDeElementos or i < 0:
        return 0

    q = Nodo()
    q.dato = x
    q.sig = None

    if numDeElementos == 0:

    p.v = q

def MostrarTodos(p):
    q = p.v
    while q != None:
        print(q.dato)
        q = q.sig

def obtener(i, q):
    n = 0
    if q == None:
        print("lista vacía")
        return None
    #

    if i >= 0:
        while q != None and n < i:
            q = q.sig
            n += 1

        if q != None:
            return q
    #

    return None

def borrarTodos(p):
    while p.v != None:
        q = p.v
        p.v = p.v.sig
        del q; gc.collect

def main():
    i = 0
    p = Envoltorio(None)
    print("Introducir datos. Finalizar con Enter")
    n = input("dato: ")
    while n != "":
        aniadirAlPrincipio(n, p)
        n = input("dato: ")

    print()
    #MostrarTodos(p)
    q = obtener(i, p.v)
    while q != None:
        print(q.dato)
        i += 1
        q = obtener(i, p.v)
    
    borrarTodos(p)

main()