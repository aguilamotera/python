
def intercambio(x, y):
    z = x
    x = y
    y = z

def main():
    clear()
    a = 20; b = 30
    intercambio(a, b) # a y b son pasados por valor
    print("a vale " + str(a) + " b vale " + str(b))


def clear():
    print("\033c", end="")

main()