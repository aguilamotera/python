import gc

class Envoltorio:
    pass

class Elemento:
    def __init__(self):
        self.dato = None
        self.siguiente = None # Elemento.

def nuevoElemento():
    q = Elemento()
    #if q == None:
    #    error()
    return q

# Queda pendiente hacer el equivalente.
def error():
    print("Insuficiente memoria")
    #exit(1)

def aniadirAlPrincipio(e, _):
    q = nuevoElemento()
    q.dato = e
    q.siguiente = _.llse
    _.llse = q

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
        #end while

        if q != None:
            return q.dato
    #end if
    return None
#end def

def borrarTodos(_):
    p = _.llse
    q = None
    while p != None:
        q = p
        p = p.siguiente
        gc.collect
    #end while
    _.llse = None
#end def

def main():
    _ = Envoltorio()
    _.llse = None

    repetir = True
    i = 0
    n = None #int
    d = ""
    
    print("Introducir datos.")
    while repetir:
        d = input("dato: ")
        
        if d == "s":
            repetir = False
        else:
            try:
                n = int(d)
                aniadirAlPrincipio(n, _)
            except:
                print("No es un entero.")
            #finally:
    
    n = obtener(i, _.llse)
    while n != None:
        print(str(n))
        i += 1
        n = obtener(i, _.llse)
    #end while

    i = 0
    n = obtener(i, _.llse)
    while n != None:
        del n
        gc.collect
        i += 1
        n = obtener(i, _.llse)
    #end while
    borrarTodos(_)
main()