import json
from os import getcwd
from datetime import datetime
from json import load, dump

from nodes.models.obj.tools.debug import print_debug

def load_save(path:str) -> dict:
    """
    Carga el contenido de un archivo 
    """
    return load(open(path))

def save_node(date:dict, name="", *other):
    """
    Guarda información del juego...
    """
    match name:
        case "":
            name = f"game_info_{datetime.now().date()}"
        case _:
            pass
    file = open(f"{getcwd()}/{name}.dat", "w")

    try:
        json.dump(date, file, indent=1)
    except TypeError:
        print_debug("ALGUN DATO GUARDADO ES UN ELLIPSIS Y NO SE PUEDE GUARDAR")
    
    return fr"{getcwd()}/{name}.dat"
