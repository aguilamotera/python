import gc

"""
Listas simplemente ligadas
--------------------------
Operaciones con listas simplemente ligadas.
"""

class Envoltorio:
    def __init__(self, valor):
        self.v = valor

class Nodo:
    def __init__(self):
        self.INFO = None
        self.LIGA = None

def crearInicio(p):
    p.v = Nodo()
    p.v.INFO = input("Dato: ")
    p.v.LIGA = None
    res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")

    while res == "1":
        q = Nodo()
        q.INFO = input("Dato: ")
        q.LIGA = p.v
        p.v = q
        res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")

def crearFinal(p):
    p.v = Nodo()
    p.v.INFO = input("Dato: ")
    p.v.LIGA = None
    t = p.v
    res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")

    while res == "1":
        q = Nodo()
        q.INFO = input("Dato: ")
        q.LIGA = None
        t.LIGA = q
        t = q
        res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")

def recorreIterativo(p):
    q = p.v
    while q != None:
        print(str(q.INFO))
        q = q.LIGA

def recorreRecursivo(p):
    if p != None:
        print(str(p.INFO))
        recorreRecursivo(p.LIGA)

def insertarInicio(p, dato):
    q = Nodo()
    q.INFO = dato
    q.LIGA = p.v
    p.v = q

def insertarFinal(p, dato):
    t = p.v
    while t.LIGA != None:
        t = t.LIGA

    q = Nodo()
    q.INFO = dato
    q.LIGA = None

    t.LIGA = q

def insertarAntesX(p, dato, x):
    t = None
    q = p.v
    band = 1

    while q.INFO != x and band == 1:
        if q.LIGA != None:
            t = q
            q = q.LIGA
        else:
            band = 0
    #end while

    if band == 1:
        x = Nodo()
        x.INFO = dato

        if p.v == q:
            x.LIGA = p.v
            p.v = x
        else:
            t.LIGA = x
            x.LIGA = q
    else:
        print("El nodo dado como referencia no se encuentra en la lista.")
    #end if

def insertarDespuesX(p, dato, x):
    q = p.v
    band = 1
    while q.INFO != x and band == 1:
        if q.LIGA != None:
            q = q.LIGA
        else:
            band = 0
    #end while

    if band == 1:
        t = Nodo()
        t.INFO = dato
        t.LIGA = q.LIGA
        q.LIGA = t
    else:
        print("El nodo dado como referencia no se encuntra en la lista.")
    #end if

# Eliminar el primer nodo. 
def eliminaInicio(p):
    q = p.v
    p.v = q.LIGA
    del q
    gc.collect

# Eliminar el último nodo.
def eliminarUltimo(p):
    q = p.v
    if p.v.LIGA == None:
        p.v = None
    else:
        while q.LIGA != None:
            t = q
            q = q.LIGA
        #end while
        t.LIGA = None
    #end if
    del q
    gc.collect

# Eliminar un nodo con información X.
def eliminaX(p, x):
    q = p.v
    band = True
    while q.INFO != x and band:
        if q.LIGA != None:
            t =  q
            q = q.LIGA
        else:
            band = False
    #end while

    if not band :
        print("El elemento con información X no se encuentra en la lista.")
    else:
        if p.v == q:
            p.v = q.LIGA
        else:
            t.LIGA = q.LIGA
        #end if
        del q
        gc.collect
    #end if

# Eliminar el nodo anterior al nodo con información X.
def eliminaAntesX(p, x):
    if p.v.INFO == x:
        print("No existe un nodo que precede al que contiene a X")
    else:
        q = p.v
        t = p.v
        band = True
        while q.INFO != x and band:
            if q.LIGA != None:
                r = t
                t = q
                q = q.LIGA
            else:
                band = False
            #end if
        #end while

        if not band:
            print("El elemento no se enecuentra en la lista.")
        else:
            if p.v.LIGA == q:
                p.v = q
            else:
                r.LIGA = q
            #end if
            del t
            gc.collect
        #end if
    #end if

# Eliminar el nodo posterior al nodo con información x.
#No implementado

def busquedaDesordenada(p, x):
    q = p.v
    while q != None and q.INFO != x:
        q = q.LIGA
    
    if q == None:
        print("El elemento no se encuentra en la lista.")
    else:
        print("El elemento si se encuentra en la lista.")

def busquedaOrdenada(p, x):
    q = p.v
    while q != None and q.INFO < x:
        q = q.LIGA

    if q == None or q.INFO > x:
        print("El elemento no se encuentra en la lista.")
    else:
        print("El elemento sí se encuentra en la lista.")

def busquedaRecursivo(p, x):
    if p != None:
        if p.INFO == x:
            print("El elemento se encuentra en la lista.")
        else:
            busquedaRecursivo(p.LIGA, x)
    else:
        print("El elemento no se encuentra en la lista.")

def main():
    print("\033c", end="")

    p = Envoltorio(None)
    #crearInicio(p)
    #crearFinal(p)

    insertarInicio(p, "b")
    insertarInicio(p, "a")
    #insertarFinal(p, "c")

    #insertarAntesX(p, "n", "b")
    #insertarDespuesX(p, "m", "n")

    #insertarFinal(p, "a")
    #insertarFinal(p, "b")

    #eliminaInicio(p)
    #eliminarUltimo(p)

    #eliminaX(p, "a")
    #eliminaAntesX(p, "a")

    #busquedaDesordenada(p, "n")
    #busquedaOrdenada(p, "c")
    busquedaRecursivo(p.v, "c")

    recorreIterativo(p)
    #recorreRecursivo(p.v)
main()

