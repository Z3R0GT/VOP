#OFFICIAL
from .models.page import *
from .models.button import *
from .models.mapa import *
from .models.structure import *
from .models.camera import *
from .models.object import *
from .models.player import *

version: str = "1.4.02.24"
"""
version de la libreria, siendo:
{n lanzamiento}.{n update}.{mes}.{año}
"""

def set_dft_door(door:str):
    """
    Asgina una letra para identificar una "puerta"
    de el nodo "structure"
    """
    DEFAULT[3] = door
    

