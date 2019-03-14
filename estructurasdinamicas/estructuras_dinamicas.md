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