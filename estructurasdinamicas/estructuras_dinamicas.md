## Paso por referencia

### Caso 1
La salida que obtenemos es: hola
```
def funcA(var):
    var = "adios"
    
def main():
    x = "hola"
    funcA(x)
    print(x)

main()
```

Una posible solución. En la salida obtendremos: adios
```
class Pruebas:
    def __init__(self):
        self.x = None

def funcA(obj):
    obj.x = "adios"

def main():
    p = Pruebas()
    p.x = "hola"
    funcA(p)
    print(p.x)

main()
```

### Caso 2
Similar al caso 1, la salida obtenida es hola
```
class Pruebas:
    def __init__(self):
        self.x = None

def funcA(obj):
    obj = None
    obj = Pruebas()
    obj.x = "adios"

def main():
    p = Pruebas()
    p.x = "hola"
    funcA(p)
    print(p.x)

main()
```

```
import gc

class Elemento:
    def __init__(self):
        self.siguiente=None # Siguiente elemento.

def nuevoElemento():
    return Elemento()

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

class Elemento:
    def __init__(self):
        self.siguiente=None # Siguiente elemento.

def nuevoElemento():
    return Elemento()

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

class Elemento:
    def __init__(self):
        self.dato = 0 # int
        self.siguiente=None # Siguiente elemento.

def nuevoElemento():
    return Elemento()

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

```
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
```