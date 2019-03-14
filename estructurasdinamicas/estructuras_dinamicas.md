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
class Envoltorio:
    def __init__(self):
        pass

def funcA(obj):
    obj.x = "adios"

def main():
    p = Envoltorio()
    p.x = "hola"
    funcA(p)
    print(p.x)

main()
```

### Caso 2
Similar al caso 1, la salida obtenida es hola
```
class Envoltorio:
    def __init__(self):
        pass

def funcA(obj):
    obj = None
    obj = Envoltorio()
    obj.x = "adios"

def main():
    p = Envoltorio()
    p.x = "hola"
    funcA(p)
    print(p.x)

main()
```
Una posible solución es, no reasignar el paso por referencia, repetir la idea de envoltorios.
```
class Envoltorio:
    def __init__(self):
        pass

def funcA(obj):
    obj.hijo = None
    obj.hijo = Envoltorio()
    obj.hijo.x = "adios"

def main():
    p = Envoltorio()
    p.hijo = Envoltorio()
    p.hijo.x = "hola"
    funcA(p)
    print(p.hijo.x)

main()
```

# Listas, arboles y grafos.
No hace falta el envoltorio, lo puse para preparar el camino al paso por referencia.
```
import gc

class Envoltorio:
    pass

class Elemento:
    def __init__(self):
        self.siguiente=None # Siguiente Elemento.

def nuevoElemento():
    return Elemento()

def main():
    _ = Envoltorio()
    _.p = None
    _.p = nuevoElemento()
    _.p.siguiente = None
    _.p = None
    gc.collect

main()
```

```
import gc

class Envoltorio:
    pass

class Elemento:
    def __init__(self):
        self.siguiente=None # Siguiente Elemento.

def nuevoElemento():
    return Elemento()

def main():
    _ = Envoltorio()
    _.q = None
    _.p = None

    _.q = nuevoElemento()
    _.p = nuevoElemento()
    
    _.q.siguiente = _.p
    _.p = _.q
    gc.collect

    _.q = _.q.siguiente
    print(_.q)

    _.q = _.q.siguiente
    print(_.q)

main()
```

```
import gc

class Envoltorio:
    pass

class Elemento:
    def __init__(self):
        self.dato = 0 # int
        self.siguiente=None # Siguiente Elemento.

def nuevoElemento():
    return Elemento()

def main():
    _ = Envoltorio()
    _.p = None
    _.q = None
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

                _.q = nuevoElemento()
                _.q.dato = n
                _.q.siguiente = _.p
                _.p = _.q
            except:
                print("No es un entero.")
            #finally:
           
    
    print("terminado")

main()
```

```
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
```

```
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