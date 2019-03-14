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