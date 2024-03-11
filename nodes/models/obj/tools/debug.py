import logging, sys
from os import system

from ..const.const import CUR, DEFAULT

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def _chk_window():
        if DEFAULT[1][2] or DEFAULT[1][1]: # IS IN MENU  
            x_cols = CUR[0][0].vec[0]+5
            y_lins = CUR[0][0].vec[1]+6
        else: #IS PLAYING MAP
            x_cols = CUR[1][DEFAULT[1][4]].transform[0]+5
            y_lins = CUR[1][DEFAULT[1][4]].transform[1]+6

        from os import system  
        system(f'mode con: cols={x_cols} lines={y_lins}')

def erase_screen():
    """
    Limpia la consola
    """
    system("cls")

def print_debug(*msg):
    logging.debug(msg)

def _insert(old_, new_, from_=..., to_=..., specific_=...) -> str:
    """
        inserta una cadena de texto y retorna una nueva desde unas coordenas o en especifico uno
        donde:

        old_: vieja cadena
        new_: nueva cadena
        from_: empieza a insertar
        to_: termina de insertar
        specific_: coordenada especifica
    """
    temp = []
    new = ""
    cont = 0

    #print(f"Viejo: {len(old_)}", f"Nuevo: {len(new_)}",f"Desde: {from_}",f"Hasta: {to_}", f"Especifico: {specific_}" )

    for i in range(len(old_)):
        temp.append(old_[i])

    if to_ is ... and from_ is not ...:
        to_ = len(new_) + from_

    for mw in range(len(temp)):
        if specific_ is not ...:
            if mw > 0 and mw == specific_:
                temp[mw] = new_
        elif mw in range(from_, to_):
            temp[mw] = new_[cont]
            cont += 1

    for i in range(len(temp)):
         new += temp[i]

    return new