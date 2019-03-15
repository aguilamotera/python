class Envoltorio:
    def __init__(self, valor):
        self.v = valor

def funcA(x):
    x.v = "adios"

def main():
    x = Envoltorio("hola")
    funcA(x)
    print(x.v)

main()