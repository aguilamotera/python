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
    q = nuevoElemento()
    q.dato = n
    q.siguiente = _.llse
    _.llse = q

def mostrarTodos(_):
    q = _.llse
    while q != None:
        print(str(q.dato))
        q = q.siguiente

def borrarTodos(_):
    p = _.llse
    q = None
    while p != None:
        q = p
        p = p.siguiente
        gc.collect
    _.llse = p

def obtener(i, q):
    n = 0
    if q == None:
        print("Lista vacía")
        return None
    #end if

    if i >= 0:
        while q != None and n < i:
            q = q.siguiente
            n+=1

        if q != None:
            return q
    #end if
    return None
#end def

def main():
    _ = Envoltorio()
    _.llse = None

    repetir = True
    n = 0
    i = 0

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
    
    #mostrarTodos(llse)
    q = obtener(i, _.llse)
    while q != None:
        print(str(q.dato))
        i += 1
        q = obtener(i, _.llse)
    #end while

    borrarTodos(_)
    mostrarTodos(_)
main()