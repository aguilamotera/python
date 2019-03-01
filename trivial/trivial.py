import re

class Trivial():
    def comenzar(self):
        repetir=True
        while repetir:
            print("\nTrivial\n\n", end="")
            print("1. Nuevo juego\n", end="")
            print("2. Ranking\n", end="")

            print("0. Salir\n\n", end="")
            
            ch=input("¿Qué desea hacer?: ")
            patron=re.compile('[0-2]+')
            if patron.match(ch):
                if ch == "1":
                    pass
                elif ch == "2":
                    pass
            
            if ch == "0":
                repetir=False
        
tri=Trivial()
tri.comenzar()