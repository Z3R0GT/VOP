from nodes.models.obj.tools.debug import print_debug
from .const.const import *

from re import search
                              # ABS     ID
def _set_name(nme, nme_dft = ("DEFAULT", "NRO")):
    if type(nme) == type(""):
        if nme != "":
            return nme
        else:
            return f"{nme_dft[0]}_{nme_dft[1]}"

def __check__(msg):
    """
    Verifica si el mensaje contiene números y los transforma
    """
    if search("[0-9]", msg):
        return int(msg)
    else:
        return msg

class gen_obj:
    """
    Clase generica para todo los objetos (nodos), contiene lo más 
    basico que todo nodo debe tener
    """
    def __init__(self, 
                 X,
                 Y,
                 CHR,
                 ABS,
                 ID, 
                 NMO= "") -> None:
        
        self.vec = [X,Y]
        self._temp_vec = [X, Y]
        
        self.abs = ABS
        self.id = ID

        self.character = CHR
        self.name = _set_name(NMO, (self.abs, self.id))
        
        self.meta = {
            "name": self.name,
            "vec": self.vec,
            "abs": self.abs,
            "id": self.id,
            "chr": self.character,
        }
    
    def __transform__(self, size_x, size_y):
        """
        Agrega los atributos necesarios para nodo que requieran editar su interior
        """
        self.transform = (size_x, size_y)
        self._set_meta("transform", self.transform)
    
    def __map__(self, map):
        """
        Agrega los atributos necesarios para nodo que requiera ser hijo de un mapa
        """
        self.map = map
        self._set_meta("map", (self.map.id, self.map.name))

    def _set_meta(self, nme, arg):
        """
        Agrega nuevos datos a la "meta" interna 
        """
        self.meta[nme] = arg
     
    def _edit_meta(self, nme_1, nme_2, arg):
        """
        edita datos de la "meta" interna 
        """
        if type(nme_2) != type(...):
            if type(arg) == type([]):     
                    self.meta[nme_1][nme_2].append(arg)
            elif type(arg) == type({}):
                    self.meta[nme_1][nme_2] = arg
            else:
                self.meta[nme_1].append(arg)
        else:
            self._set_meta(nme_1, arg)
    
    def get_meta(self, is_print=True):
        """
        imprime/retorna la "meta" interna 
        """
        if is_print:
            print(self.meta)
        else:
            return self.meta 


class gen_btn:
    """
    Clase general para todo nodo del tipo "boton"
    """
    def __start__(self, *msg):
        """
        imprime un texto en consola (solo sirve para prubea, no hace mayor cosa)
        """
        print_debug(msg)
        
    def __default__(self):
        CUR[3].append(self.__start__)

    def __action__(self, what):
        """
        agrega una acción (función) a la memoria interna, ademas que incluye un ID y la función en cuestión para
        el boton
        """
        ID = -1
        for func in CUR[3]:
            #YA EXISTE
            if func == what:
                break
            #NO EXISTE
            else:
                CUR[3].append(what)
                ID += 1
                break
        self.action = (ID, what)

    def __link__(self):
        """
        contecta el "input"(._in) con la función requerida
        """
        if not len(self._in) > 0:
            self.action[1]()
        else:
            self.action[1](self._in[0: len(self._in)])
            
        self._in = []

    def _input_(self, msg:tuple):
        """
        especifica al usuario con un "mensaje" lo que debe ingresar el usuario
        """
        self._in =[]

        for text in msg:
            self._in.append(input(f"{text}\n>  "))
        
        self.__link__()
        
    def execute(self, *arg):
        """
        efectua de manera inmediata el ".action" asginado al boton
        """
        self.action[1](arg)
           
        
