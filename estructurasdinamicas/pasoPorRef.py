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