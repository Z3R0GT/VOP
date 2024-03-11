from nodes import *
from random import randint

DEV[0] = False

pgn = Page(50, 20, "#")
pgn.create_text("RECOLECTOR DE MONEDAS", "UPPER")

def creadits():
    pgn = Page(50, 20, "#")
    pgn.create_text("DIRECTOR: JEREMIT SANCHEZ", "CUSTOM", (13,2))
    pgn.create_text("PROGRAMADOR: JEREMIT SANCHEZ", "CUSTOM", (10,3))
    pgn.create_text("LIBRERIA: VOP by: SCO Studios (1.3.12.23)", "CUSTOM", (5,4))
    pgn.create_text("VOP by: SCO Studios 1.3.12.23", "LOWER")

    btn = Button(18, 15, DEFAULT="BACK")
    btn.cast((""))
    
    pgn.add_btn(btn)
    
    pgn.start_cast()

btn = Button(10, 2, DEFAULT="PLAY")
btn.cast((""))
pgn.add_btn(btn)

btn = Button(10, 4, DEFAULT="LOAD")
btn.cast((""))
pgn.add_btn(btn)

btn = Button(10, 6, "Creditos", creadits)
btn.cast((""))
pgn.add_btn(btn)

mapa_principal = Mapa(120, 29, "#", "Mansion")

mansion = Structure(mapa_principal, 1, 1, 116, 20, "&", True)

mansion.edit_geometry([(1, 115, 1), (1, 115, 18)])

#CUADRADO INTERIOR
mansion.create_geometry("Y", 2, 18, 1, 2)
mansion.create_geometry("Y", 2, 18, 114, 115)

#CUARTO 1
mansion.create_geometry("X", 3, 4, 2, 17)
mansion.create_geometry("X", 9, 10, 2, 17)

mansion.create_geometry("Y", 2, 10, 16, 17)

#ENTRADA
mansion.create_geometry("Y", 12, 18, 52, 53)
mansion.create_geometry("Y", 12, 18, 67, 68)

mansion.create_geometry("X", 11, 12, 44, 82)
mansion.create_geometry("Y", 4, 12, 43, 44)
mansion.create_geometry("Y", 2, 12, 82, 83)

mansion.create_geometry("X", 4, 5, 44, 82)

#PASADISO 1
mansion.create_geometry("X", 4, 5, 17, 44)
mansion.create_geometry("X", 9, 10, 17, 44)

#OTROS
mansion.create_geometry("Y", 10, 18, 27, 28)

mansion.create_geometry("X", 8, 9, 83, 115)

#PUERTA
door = [(59, 19), (60, 19), 
        (59, 18), (60, 18),
        (59,11), (60, 11),
        (59, 4), (60, 4),
        (14, 9), (43, 8),
        (27, 17), (40, 9),
        (9, 9), 
        (82, 7), (83, 8), (82, 3), 
        (16, 2)]

mansion.create_door(door, "M")
mapa_principal.add_node(mansion)

player = Player(mapa_principal, 40, 25, "X", [], "", ["w", "s", "a", "d"])
mapa_principal.add_node(player)

camara_principal = Camera(mapa_principal, LOCK=False)
mapa_principal.add_node(camara_principal)

for i in range(randint(0, 15)):
    obj = Object(mapa_principal, randint(4, 27), randint(12, 19), "N", {"valor":15}, "moneda de oro")
    mapa_principal.add_node(obj)
for i in range(randint(0, 9)):           
    obj = Object(mapa_principal, randint(4, 27), randint(12, 19), "k", {"valor":1}, "moneda de plata")
    mapa_principal.add_node(obj)

for i in range(randint(0, 15)):
    obj = Object(mapa_principal, randint(85, 115), randint(11, 19), "N", {"valor":15}, "moneda de oro")
    mapa_principal.add_node(obj)
for i in range(randint(0, 9)):           
    obj = Object(mapa_principal, randint(85, 115), randint(11, 19), "K", {"valor":1}, "moneda de plata")
    mapa_principal.add_node(obj)

for i in range(randint(0, 15)):
    obj = Object(mapa_principal, randint(85, 115), randint(2, 9), "N", {"valor":15}, "moneda de oro")
    mapa_principal.add_node(obj)
for i in range(randint(0, 9)):           
    obj = Object(mapa_principal, randint(85, 115), randint(2, 9), "K", {"valor":1}, "moneda de plata")
    mapa_principal.add_node(obj)

for i in range(randint(0, 15)):
    obj = Object(mapa_principal, randint(30, 44), randint(11, 19), "N", {"valor":15}, "moneda de oro")
    mapa_principal.add_node(obj)
   
for i in range(randint(0, 9)):           
    obj = Object(mapa_principal, randint(30, 44), randint(11, 19), "K", {"valor":1}, "moneda de plata")
    mapa_principal.add_node(obj)

pgn.start_cast()

