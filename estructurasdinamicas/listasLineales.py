import gc

class Envoltorio:
    pass

class Nodo:
    def __init__(self):
        self.elemento = None
        self.sig = None

def reservar():
    return Nodo()

def insertar(_, elemento):
    auxi = None
    auxi = reservar()
    auxi.elemento = elemento
    if _.anterior == None:
        auxi.sig = _.inic
        _.inic = auxi
    else:
        auxi.sig = _.anterior.sig
        _.anterior.sig = auxi

    _.anterior = auxi

def inicializar(_):
    _.inic = None

def vacia(_):
    _.inic = None

def suprimir(_):
    if _.anterior == None:
        _.inic = _.posic.sig
    else:
        _.anterior.sig = _.pos.sig

    del _.posic
    _.anterior = None
    _.posic = _.inic

def recorrer(_):
    posic = _.inic
    while posic != None:
        print(posic.elemento)
        posic = posic.sig

def contar(_):
    _.n = 0
    p = _.primero

def nuevaVenta(_):
    repetir = True
    while repetir
        print("Introduzca * en el código para terminar")
        input("Código: ")
        


def main():
    _ = Envoltorio()
    #_.inic = None
    _.posic = None
    _.anterior = None
    #elemento = None
    #encontrado = False
    inicializar(_)
    #insertar(_,1)
    repetir = True
    while repetir:
        print("1.- Ventas")
        print("2.- Devoluciones")
        print("3.- Mostrar lista")
        print("4.- Fin")
        opcion = input("Elija opción: ")
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            #recorrer(_.inic, )
            pass
        elif opcion == "4":
            repetir = False

main()