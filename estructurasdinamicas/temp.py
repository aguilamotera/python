class Nodo:
    def __init__(self):
        self.INFO = None
        self.LIGA = None

def crearInicio():
    p = Nodo()
    p.INFO = input("Dato: ")
    p.LIGA = None
    res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")

    while res == "1":
        q = Nodo()
        q.INFO = input("Dato: ")
        q.LIGA = p
        p = q
        res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")

    return p

def insertarInicio(p, dato):
    q = Nodo()
    q.INFO = dato
    q.LIGA = p
    p = q

def crearFinal():
    p = Nodo()
    p.INFO = input("Dato: ")
    p.LIGA = None
    t = p
    res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")

    while res == "1":
        q = Nodo()
        q.INFO = input("Dato: ")
        q.LIGA = None
        t.LIGA = q
        t = q
        res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 ")
    
    return p

def recorreIterativo(p):
    q = p
    while q != None:
        print(str(q.INFO))
        q = q.LIGA

def recorreRecursivo(p):
    if p != None:
        print(str(p.INFO))
        recorreRecursivo(p.LIGA)

def main():
    p = crearInicio()
    #p = crearFinal()
    #recorreIterativo(p)
    recorreRecursivo(p)
main()

