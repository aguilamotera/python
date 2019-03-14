import gc

class Envoltorio:
    pass

class Elemento:
    def __init__(self):
        self.dato = 0 # int
        self.siguiente=None # Elemento.

def nuevoElemento():
    return Elemento()

def error():
    pass

def aniadirAlPrincipio(n, _):
    p = _.listaLinealSimpleEnlazada
    q = nuevoElemento()
    q.dato = n
    q.siguiente = p
    p = q
    _.listaLinealSimpleEnlazada = p

def mostrarTodos(_):
    q = _.listaLinealSimpleEnlazada
    while q != None:
        print(str(q.dato))
        q = q.siguiente

def borrarTodos(_):
    p = _.listaLinealSimpleEnlazada
    q = None
    while p != None:
        q = p
        p = p.siguiente
        gc.collect
    _.listaLinealSimpleEnlazada = p


def main():
    _ = Envoltorio()
    _.listaLinealSimpleEnlazada = None
    repetir = True
    n = 0

    print("Introducir datos.")
    while repetir:
        n = input("dato: ")
        
        if n == "s":
            repetir = False
        else:
            try:
                n = int(n)
                aniadirAlPrincipio(n, _)
            except:
                print("No es un entero.")
            #finally:
    
    mostrarTodos(_)
    borrarTodos(_)
    mostrarTodos(_)
main()