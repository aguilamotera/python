```
import gc

class S:
    def __init__(self):
        self.siguiente=None # Siguiente elemento.

def nuevoElmento():
    return S()

def main():
    p = None
    p = nuevoElmento()
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

def nuevoElmento():
    return S()

def main():
    p = None
    q = None

    p = nuevoElmento()
    q = nuevoElmento()
    q.siguiente = p
    p = q
    gc.collect

    q=q.siguiente
    print(q)

    q=q.siguiente
    print(q)

main()
```