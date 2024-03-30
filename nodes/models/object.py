from .obj.gen_obj import gen_obj, N_ABS, N_NUM

class Object(gen_obj):
    """
    nodo con la capacidad de ser percibido por algún otro que nodo que 
    pueda moverse y tenga un ".inv" disponible
    """
    def __init__(self,
                 MAP,
                 X, 
                 Y, 
                 CHR,
                 DATA: dict | list= ...,
                 NMO="") -> None:
        N_NUM[4] += 1
        super().__init__(X, Y, CHR, N_ABS[4], N_NUM[4], NMO)
        super().__map__(MAP)
        
        self.data = DATA
        
        self._set_meta("data", self.data)
    
    def _refresh_meta(self):
        """
        actualiza el "meta" de "data"
        """
        self._set_meta("data", self.data)

    def set_data(self, nme: str, *arg):
        """
        Agrega/Edita nueva informacion de "data"
        """
        self.data[nme] = arg
        self._refresh_meta()

    def edit_data(self, nme_1: str, nme_2, arg):
        """
        edita informacion de "data"
        """
        if type(arg) == type([]) or type(arg) == type(()):
            if type(nme_2) != type(...):
                self.meta[nme_1][nme_2].append(arg)
            else:
                self.meta[nme_1].append(arg)
        else:
            self._set_meta(nme_1, arg)
        
        self._refresh_meta()
