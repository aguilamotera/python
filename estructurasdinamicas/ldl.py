"""
Listas Doblemente Ligadas
"""

class Envoltorio:
    def __init__(self, valor):
        self.v = valor

class Nodo:
    def __init__(self):
        self.LIGAIZQ = None
        self.INFOR = None
        self.LIGADER = None

def insertarPrincipio(p, dato):
    q = Nodo()
    q.INFOR = dato
    q.LIGADER = p.v
    p.v.LIGAIZQ = q
    #q.LIGAIZQ = None
    #p.v = q

"""
    q          +-> p
    +------+   |  +------+
    | b    |   |  | a    |
    +------+   |  +------+
 Nil| izq  |   |  | izq  | q
    +------+   |  +------+
    | der  | --+  | der  |
    +------+      +------+
"""


def main():
    print("\033c", end="")
    p = Envoltorio(None)
    insertarPrincipio(p, "a")

main()