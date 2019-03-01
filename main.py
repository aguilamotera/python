import enum
from tkinter import *

class Jugadores:
    JUGADOR1=1
    JUGADOR2=2

gPuntuacionJugador1 = 0
gPuntuacionJugador2 = 0
gEnEspera = False

root = Tk()
root.title("hola mundo")
root.resizable(1,1)
frame = Frame(root)
#root.iconbitmap('hola.ico')

#frame.pack()
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
#frame.config(bd=25)
#frame.config(relief="sunken")
frame.config(width=480, height=320)

root.config(cursor="arrow")
root.config(bg="blue")
#root.config(bd=15)
#root.config(relief="ridge")
root.mainloop()

