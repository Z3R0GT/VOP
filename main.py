from nodes import *

DEV[0] = False

pgn = Page(20, 10, "#")

def owo(*a):
    print(a[0][0]*int(a[0][1]))

def _in():
    print("Hola")


btn = Button(1, 1, "Imprime algo", owo)
btn.cast(("ingresa algo a imprimir", "¿Cuantas veces quieres que se repita?"))

btn_1 = Button(1, 2, "imprime algo", _in)
btn_1.cast((""))

btn_2 = Button(1, 3, DEFAULT="SAVE")
btn_2.cast((""))

btn_3 = Button(1, 4, DEFAULT="PLAY")
btn_3.cast((""))

btn_4 = Button(1, 5, DEFAULT="LOAD")
btn_4.cast((""))

btn_5 = Button(1, 6, DEFAULT="EXIT")
btn_5.cast((""))

pgn.add_btn(btn_2)
pgn.add_btn(btn_3)
pgn.add_btn(btn_4)
pgn.add_btn(btn_5)

mapa_principal = Mapa(50, 20, "#", "Mansión")


mansion = Structure(mapa_principal, 1, 1, 20, 10, "&", True)
mapa_principal.add_node(mansion)

player = Player(mapa_principal, 2, 2, "X")
mapa_principal.add_node(player)

cmr = Camera(mapa_principal, LOCK=False)
mapa_principal.add_node(cmr)

pgn.start_cast()
