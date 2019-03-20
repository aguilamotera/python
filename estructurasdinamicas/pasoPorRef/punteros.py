"""
Se pretende hacer algo parecido a C/C++, 
la adaptación resulta ser más fácil y obvia de entender.

int a, *p, **pp;
a = 10;
p = &a;
pp = &p;

printf("En la dirección %.4X está el valor %d\n", p, *p);
printf("En la dirección %.4X está el valor %.4X\n", pp, *pp);
"""

class Envoltorio:
    def __init__(self, valor):
        self.v = valor

def main():
    clear()

    a = Envoltorio(10)
    p = Envoltorio(a)
    pp = Envoltorio(p)
    print("En la dirección " + hex(id(a)) + " está el valor " + str(a.v))
    print("En la dirección " + hex(id(p)) + " está el valor " + hex(id(p.v)))
    print("En la dirección " + hex(id(pp)) + " está el valor " + hex(id(pp.v)))

def clear():
    print("\033c", end="")

main()
