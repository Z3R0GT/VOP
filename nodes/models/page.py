from time import sleep
from .obj.tools.debug import _chk_window, print_debug

from .obj.gen_obj import gen_obj, N_ABS, N_NUM, CUR
from .obj.gen_wns import gen_wns, gen_ui

class Page(gen_obj, gen_wns, gen_ui):
    """
    Un nodo especial encargado de ser un menu en pantalla, puede interactuar con 
    botones si son agregados a este
    """
    def __init__(self, 
                 X, 
                 Y, 
                 CHR, 
                 NMO="") -> None:
        N_NUM[0] += 1
        
        super().__init__(X, Y, CHR, N_ABS[0], N_NUM[0], NMO)
        super().__wns__()
        
        CUR[0].append(self)
        
        self.btns = [...]

        self._create_square(self.vec)
        #self._create_line_num()
    
    def add_btn(self, btn:gen_obj):
        """
        Agrega un boton
        """
        self.create_text(btn.character, "CUSTOM", tuple(btn.vec))
        self.btns.append(btn)
    
    def start_cast(self):
        """
        Empieza a grabar el teclado esperando alguna entrada para algún 
        boton que sea requerido
        en la 1.4 el boton debe ser selecionado por número
        """
        _chk_window()
        self.get_pre_view()
        
        input("VERIFICADO, PRESIONE *ENTER* POR FAVOR... \n>   ")
        try:
            _in = int(input("Ingrese el número de boton \n>   "))
            self.btns[_in]._input_(self.btns[_in].cast)
        except ValueError:
            print_debug("DEBE DE INGRESAR ALGUN NUMERO DE BOTON, INTENTE OTRA VEZ")
            sleep(3)
            self.start_cast()
        
    
    
        

        
