class Envoltorio:
    def __init__(self, valor):
        self.v = valor

def funcA(x):
    x.v = None
    x.v = Envoltorio("adios")

def main():
    x = Envoltorio(Envoltorio("hola"))
    funcA(x)
    print(x.v.v)

main()