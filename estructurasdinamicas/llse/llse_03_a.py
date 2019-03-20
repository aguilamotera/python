import gc

"""
Listas lineales simplemente enlazadas (llse)

Operaciones básicas:
1. Insertar un elemento en una lista.
2. Buscar un elemento en una lista.
3. Borrar un elemento en una lista.
4. Recorrer los elementos de una lista.
5. Borrar todos los elementos de una lista.
"""

class Envoltorio:
    def __init__(self, valor):
        self.v = valor

class Nodo:
    def __init__(self):
        self.dato = None
        self.sig = None

"""
 Insertar un elemento al comienzo de una lista.
    q      p      | pq      
    +----+ +----+ | +----+ +-> +----+
    | b  | | a  | | | b  | |   | a  |
    +----+ +----+ | +----+ |   +----+
    |    | |    | | |    |-+   |    |
    +----+ +----+ | +----+     +----+
"""
def insertarAlComienzo(p, x):
    q = Nodo()
    q.dato = x
    q.sig = p.v
    p.v = q

"""
 Insertar a continuación de R
           q          |             q                    
           +----+     |         +-> +----+               
           |    |     |         |   | x  |               
           +----+     |         |   +----+               
           |    |     |         |   |    |             
           +----+     |         |   +----+               
r                     |  r      |      |                   
+----+ +-> +----+ +-> |  +----+ |      +-> +----+ +-> 
|    | |   |    | |   |  |    | |          |    | |    
+----+ |   +----+ |   |  +----+ |          +----+ |    
|    |-+   |    |-+   |  |    |-+          |    |-+    
+----+     +----+     |  +----+            +----+      

"""
def insertarAContinuacionDeR(r, x):
    q = Nodo()
    q.dato = x
    q.sig = r.sig
    r.sig = q

"""
 Insertar antes de R
           q                   |                        q                    
           +----+              |                    +-> +----+               
           |    |              |                    |   | b  |               
           +----+              |                    |   +----+               
           |    |              |                    |   |    |              
           +----+              |                    |   +----+   
                               |                    |      |    
           r                   |             r      |      |         
+----+ +-> +----+ +-> +-       |  +----+ +-> +----+ |      +-> +-
| a  | |   | b  | |   |        |  | a  | |   | x  | |          |
+----+ |   +----+ |   +-       |  +----+ |   +----+ |          +-
|    |-+   |    |-+   |        |  |    |-+   |    |-+          |
+----+     +----+     +-       |  +----+     +----+            +-

"""
def insertarAntesDeR(r, x):
    q = Nodo()
    q.dato = r.dato
    q.sig = r.sig

    r.dato = x
    r.sig = q

"""
 Borrar a continuacion de R
      r          q           |      r          q           
  +-> +----+ +-> +----+ +->  |  +-> +----+  +----+ +->  
  |   | b  | |   | c  | |    |  |   | b  |  | c  | |    
  |   +----+ |   +----+ |    |  |   +----+  +----+ |    
 -+   |    |-+   |    |-+    | -+   |    |  |    |-+    
      +----+     +----+      |      +----+  +----+ |
                                       |           |
                                       +-----------+   
"""
def borrarAContinuacionDeR(r):
    q = r.sig
    r.sig = q.sig
    del q; gc.collect

"""
 Borrar R
      r          q           |      r          q           
  +-> +----+ +-> +----+ +->  |  +-> +----+  +----+ +->  
  |   | b  | |   | c  | |    |  |   | c  |  | c  | |    
  |   +----+ |   +----+ |    |  |   +----+  +----+ |    
 -+   |    |-+   |    |-+    | -+   |    |  |    |-+    
      +----+     +----+      |      +----+  +----+ |
                                       |           |
                                       +-----------+   
"""
def borrarR(r):
    if r.sig == None:
        del r
    else:
        q = r.sig
        r.dato = q.dato
        r.sig = q.sig
        del q
        gc.collect

"""
 Buscar dato:
 Si no lo encuentra retorna None, se puede considerar False. 
 Si lo encuentra retorna el nodo, se puede considerar True.
"""
def buscarDatoX(p, x):
    r = p.v
    while r != None and r.dato != x:
        r = r.sig

    return r

def recorrerLista(p):
    q = p.v
    while q != None:
        print(q.dato)
        q = q.sig

def borrarTodo(p):
    while p.v != None:
       q = p.v
       p.v = p.v.sig
       del q; gc.collect

def main():
    repetir = True
    p = Envoltorio(None)
    while repetir:
        clear()
        print("Menu:")
        print("1.- Introducir Datos.")
        print("2.- Buscar.")
        print("3.- Recorrer lista.")
        print("4.- Insertar a continuación de R.")
        print("5.- Insertar antes de R.")
        print("6.- Borrar a continuación de R.")
        print("7.- Borrar R.")
        print("s.- Salir")
        
        eleccion = input("Elija opción: ")
        if eleccion == "s":
            repetir = False
        elif eleccion == "1":
            introducirDatos(p)
        elif eleccion == "2":
            buscarDatos(p)
        elif eleccion == "3":
            recorrerLista(p)
            input()
        elif eleccion == "4":
            insertarAContinuacionDeX(p)
        elif eleccion == "5":
            insertarAntesDeX(p)
        elif eleccion == "6":
            borrarAContinuacionDeX(p)
        elif eleccion == "7":
            borrarX(p)

def clear():
    print("\033c", end="")

def mostrarLista(p):
    recorrerLista(p)

def introducirDatos(p):
    print("Introducir datos. Para finalizar presionar Enter.")
    n = input("dato: ")
    while n != "":
        insertarAlComienzo(p, n)
        n = input("dato: ")

def buscarDatos(p):
    x = input("Dato a buscar: ")
    nodo = buscarDatoX(p, x)
    if nodo == None:
        print("No encontrado")
    else:
        print("Encontrado")
    input()

def insertarAContinuacionDeX(p):
    x = input("Dato a buscar: ")
    r = buscarDatoX(p, x)
    if r != None:
        x = input("Dato: ")
        insertarAContinuacionDeR(r, x)

def insertarAntesDeX(p):
    x = input("Dato a buscar: ")
    r = buscarDatoX(p, x)
    if r != None:
        x = input("Dato: ")
        insertarAntesDeR(r, x)

def borrarAContinuacionDeX(p):
    x = input("Dato a buscar: ")
    r = buscarDatoX(p, x)
    if r != None:
        borrarAContinuacionDeR(r)

def borrarX(p):
    clear()
    print("Borrar R\n--------\n")
    
    mostrarLista(p)
    x = input("\nDato a borrar: ")
    if x != "":
        r = buscarDatoX(p, x)
        if r != None:
            borrarR(r)
        
        clear()
        mostrarLista(p)
        input("\nPara volver al Menú presione Enter.")

main()