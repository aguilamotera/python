```
import gc

class S:
    def __init__(self):
        self.siguiente=None # Siguiente elemento.

def nuevoElemento():
    return S()

def main():
    p = None
    p = nuevoElemento()
    p.siguiente = None
    p = None
    gc.collect

main()
```

```
import gc

class S:
    def __init__(self):
        self.siguiente=None # Siguiente elemento.

def nuevoElemento():
    return S()

def main():
    p = None
    q = None

    p = nuevoElemento()
    q = nuevoElemento()
    q.siguiente = p
    p = q
    gc.collect

    q=q.siguiente
    print(q)

    q=q.siguiente
    print(q)

main()
```

```
import gc

class S:
    def __init__(self):
        self.dato = 0 # int
        self.siguiente=None # Siguiente elemento.

def nuevoElemento():
    return S()

def main():
    p = None
    q = None
    n = 0
    repetir = True

    print("Introducir datos.")

    while repetir:
        n = input("dato: ")
        
        if n == "s":
            repetir = False
        else:
            try:
                n = int(n)

                q = nuevoElemento()
                q.dato = n
                q.siguiente = p
                p = q
            except:
                print("No es un entero.")
            #finally:
           
    
    print("terminado")

main()
```

Por cuestiones de tiempo he dejado pendiente el tema de paso por refe y queda optimizar algo por ahí.
```
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
```

```
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
    repetir = True
    llse = None
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
                llse = aniadirAlPrincipio(n, llse)
            except:
                print("No es un entero.")
            #finally:
    
    #mostrarTodos(llse)
    q = obtener(i, llse)
    while q != None:
        print(str(q.dato))
        i += 1
        q = obtener(i, llse)
    #end while

    llse = borrarTodos(llse)
    #mostrarTodos(llse)
main()
```