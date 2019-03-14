import gc

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

# Queda pendiente hacerlo por paso por ref, no mola con return.
def aniadirAlPrincipio(e, lista):
    p = lista
    q = nuevoElemento()
    q.dato = e
    q.siguiente = p
    p = q
    #lista = p
    return p

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

def borrarTodos(lista):
    p = lista
    q = None
    while p != None:
        q = p
        p = p.siguiente
        gc.collect
    #end while
    lista = None
    return lista
#end def

def main():
    repetir = True
    i = 0
    llse = None
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
                llse = aniadirAlPrincipio(n, llse)
            except:
                print("No es un entero.")
            #finally:
    
    n = obtener(i, llse)
    while n != None:
        print(str(n))
        i += 1
        n = obtener(i, llse)
    #end while

    i = 0
    n = obtener(i, llse)
    while n != None:
        del n
        gc.collect
        i += 1
        n = obtener(i, llse)
    #end while
    llse = borrarTodos(llse)
main()