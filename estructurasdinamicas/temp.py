
class Elemento:
    def __init__(self):
        self.a=None

class Envoltorio:
    def __init__(self):
        self.v = None

def funcA(var):
    var = "A"

def funcB(envoltorio):
    #elemento.a = "adios" #funciona perfectamente
    #elemento = None # No cuela
    
    m = Elemento()
    m.a = "adios"
    #elemento = m
    #del elemento
    #elemento = Elemento()
    envoltorio.v = m
    
def main():
    el = Elemento()
    el.a = "hola"
    env = Envoltorio()
    env.v = el
    funcB(env)
    print(env.v.a)
main()