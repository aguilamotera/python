import gc

class Elemento:
    def __init__(self):
        self.dato = 0 # int
        self.siguiente=None # Elemento.

def nuevoElemento():
    return Elemento()

def error():
    pass

def aniadirAlPrincipio(n, lista):
    p = lista
    q = nuevoElemento()
    q.dato = n
    q.siguiente = p
    p = q
    lista = p
    return lista

def mostrarTodos(p):
    q = p
    while q != None:
        print(str(q.dato))
        q = q.siguiente

def borrarTodos(p):
    q = None
    while p != None:
        q = p
        p = p.siguiente
        gc.collect
    return p


def main():
    repetir = True
    listaLinealSimpleEnlazada = None
    n = 0

    print("Introducir datos.")
    while repetir:
        n = input("dato: ")
        
        if n == "s":
            repetir = False
        else:
            try:
                n = int(n)
                listaLinealSimpleEnlazada = aniadirAlPrincipio(n, listaLinealSimpleEnlazada)
            except:
                print("No es un entero.")
            #finally:
    
    mostrarTodos(listaLinealSimpleEnlazada)
    listaLinealSimpleEnlazada = borrarTodos(listaLinealSimpleEnlazada)
    #mostrarTodos(listaLinealSimpleEnlazada)
main()