from typing_extensions import Literal

from nodes.models.obj.const.const import DEFAULT

from .obj.tools.debug import _insert

from .obj.gen_obj import gen_obj, N_NUM, N_ABS
from .obj.gen_wns import gen_wns

class Structure(gen_obj, gen_wns):
    def __init__(self, 
                 MAP,
                 X, 
                 Y, 
                 SZ_X,
                 SZ_Y,
                 CHR, 
                 IS_COLL:bool = False,
                 NMO="") -> None:
        N_NUM[3] += 1
        super().__init__(X, Y, CHR, N_ABS[3], N_NUM[3], NMO)
        super().__map__(MAP)
        super().__wns__()
        super().__transform__(SZ_X, SZ_Y)
        
        self.is_coll = IS_COLL
        
        self.__size = []
        
        if self.is_coll:
            self.map.set_coll(self)
        
        self._set_meta("is_coll", self.is_coll)
        self._set_meta("size", self.__size)
        
        self._create_square(self.transform)
        self._create_line_num()
        
    def create_geometry(self, 
                      TYPE:Literal["X", "Y", "-Y"], 
                      LN_Y_FROM:int, 
                      LN_Y_TO:int, 
                      LN_X_FROM:int,
                      LN_X_TO:int,
                      AUTO_APPLY:bool=True):
        """
        Crea y aplica coordenadas más facilmente o retorna la coordenada en cuestión
        """
        coord = []
        
        if TYPE == "Y":
            for line in range(LN_Y_FROM, LN_Y_TO):
                coord.append((LN_X_FROM, LN_X_TO, line))
                
        elif TYPE == "-Y":
            for line in range(LN_Y_TO, LN_Y_FROM, -1):
                coord.append((LN_X_FROM, LN_X_TO, line))
                
        elif TYPE == "X":
            coord.append((LN_X_FROM, LN_X_TO, LN_Y_FROM))
            
        #REGRESA O APLICA LAS VARIABLE
        if AUTO_APPLY:
            self.edit_geometry(coord)
        else:
            return coord
        
#####################################################
#       CONSEJO:  coord: list =[(X, Y)]             #
#####################################################
    def create_door(self, coods: list = [(0,0)], CHR =""):
        """
        Crea una puerta con base a las coordenadas locales del objeto
        """
        if CHR == "":
            self._edit_line(coods, DEFAULT[3])
        else:
            self._edit_line(coods, CHR)


#####################################################
#  CONSEJO:  coord: list =[(FROM, TO, LINE)]        #
#####################################################
    def edit_geometry(self, coord: list = [(0, 0, 0)]):
        """
        Forma basica de crear lineas con coordenadas locales del objeto
        """
        self._erase_pre_view()
        for in_ in range(len(coord)):
            if len(coord[in_]) == 3:
                if type(coord[in_][0] and coord[in_][1] and coord[in_][2]) is type(3):
                    if self.transform[1] <= coord[in_][2]:
                        print(f"la linea ingresada es mayor a la establecida por el objeto \n \
                              INFO: GENERAL: {coord[in_]}")
                        coord[in_] = [coord[in_][0], coord[in_][1], self.transform[1] - 1]
                    self.__size.append(coord[in_])

                    self.square[coord[in_][2]] = _insert(self.square[coord[in_][2]],
                                                              f"{self.character}" * (coord[in_][1] - coord[in_][0]),
                                                              coord[in_][0],
                                                              coord[in_][1])
                else:
                    print(
                        f"alguno de los datos no es 'int' como se esperaba. \n \
                        INFO: {coord[in_]}")
            else:
                print(
                    f"el N: {in_} comando entragado posee menos de 3 posiciones. \n \
                    INFO: {coord[in_]}")
                
        self.meta["size"].append(coord)
        self._create_pre_view()
        
