"""
 Por ref, a la función se le pasa la dirección de cada argumento y no su valor.
 En C/C++ se utiliza el operador & para pasar la dirección de un argumento, por otro lado en el
 parámetro tendremos: tipo *nombrePuntero (indicamos que contendrá una dirección de memoria)

 intercambio(&a, &b);

 void intercambio(int *x, int *y){ 
     int z = *x; // Observese *x (contenido de la dirección)
     *x = *y;
     *y = z;
 }

 puntero genérico
 void fnx(void *p) {...}
"""

class Envoltorio:
    def __init__(self, valor):
        self.v = valor

def intercambio(xRef, yRef):
    z = xRef.v
    xRef.v = yRef.v
    yRef.v = z

def main():
    clear()
    aRef = Envoltorio(20); bRef = Envoltorio(30)
    intercambio(aRef, bRef) # a y b son pasados por referencia
    print("a vale " + str(aRef.v) + " b vale " + str(bRef.v))

def clear():
    print("\033c", end="")

main()