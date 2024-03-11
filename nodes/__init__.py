#OFFICIAL
from .models.page import *
from .models.button import *
from .models.mapa import *
from .models.structure import *
from .models.camera import *
from .models.object import *
from .models.player import *

version: str = "1.3.12.23"
"""
version de la libreria, siendo:
{n lanzamiento}.{n update}.{mes}.{año}
"""

def set_dft_door(door:str):
    DEFAULT[3] = door