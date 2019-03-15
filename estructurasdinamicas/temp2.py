class Envoltorio:
    pass

def funcA(env): # ref: x
    env.obj = None
    env.obj = Envoltorio()
    env.obj.x = "adios"

def main():
    env = Envoltorio()
    env.obj = Envoltorio()
    env.obj.x = "hola"
    funcA(env)
    print(env.obj.x)

main()