from escrutinio import Escrutinio
gEscrutinio = None

def llenarModo2():
    global gEscrutinio

    gEscrutinio = Escrutinio(3)
    gEscrutinio.agregar("A", 4000)
    gEscrutinio.agregar("B", 10000)
    gEscrutinio.agregar("C", 2000)
    gEscrutinio.agregar("D", 6000)
    print("Gestión de Escanios en las Elecciones")
    print("Introduce el número de Escaños: " + str(gEscrutinio.numEscanios) )
    print("Introduce el número de Partidos: " + str(len(gEscrutinio.partidos)) )

    for partido in gEscrutinio.partidos:
        print("Introduce el nombre del Partido: " + partido.nombre)
        print("Introduce el número de votos del Partido: " + str(partido.votos))

def resultados():
    for partido in gEscrutinio.partidos:
        print("El partido: " + partido.nombre + " ha obtenido " + str(partido.escanios) + " escaños")

def main():
    llenarModo2()
    gEscrutinio.asignarEscanios()
    resultados()

main()