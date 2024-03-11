import time
from typing_extensions import Literal

from .obj.tools.debug import erase_screen, _chk_window

from .internal.admin_dir import save_node
from .internal.archives import refresh_saves, start_test, _check_save

from .obj.const.const import CUR, DEFAULT


from .obj.gen_wns import gen_wns
from .obj.gen_obj import gen_obj, gen_btn, N_NUM, N_ABS

def __loader(*ID):
    
    print("FUNCION EN DESARROLLO")
    print(CUR[4])

def __main_return__():
    DEFAULT[1][1] = True
    erase_screen()
    _chk_window()

    CUR[0][0].start_cast()

def __continue__():
    erase_screen()
    DEFAULT[1][2] = True
    _chk_window()

    #REEPLANTEARSE EL CODGIO LOGICO PARA EL INICIO DEL JUEGO

def __play__():
    DEFAULT[1][1] = False
    _chk_window()
    
    #BORRAME LUEGO DE LA PRUEBA
    erase_screen()
    print("Objetivo: Recoger: 10 monedas de oro y 5 de plata")
    time.sleep(3)
    #BORRAME LUEGO DE LA PRUEBA

    DEFAULT[0].move()

    while not DEFAULT[1][1]:
        if not DEFAULT[1][2]:
            CUR[1][DEFAULT[1][4]].render_image(False)
            
            erase_screen()
            
            CUR[1][DEFAULT[1][4]].get_pre_view()
        else:
            ...
        
        if DEFAULT[1][1]:
            continue
        
        try:
            #BORRAME LUEGO DE LA PRUBEA
            if DEFAULT[0].inv["moneda de oro"][0] >= 10 and DEFAULT[0].inv["moneda de plata"][0] >= 5:
                erase_screen()
                print("GANASTE")
                time.sleep(3)
                import sys    
                sys.exit()
        except KeyError:
            pass
       

def __queque__():
    import sys    
    sys.exit()

def __load__():
    if _check_save():  
        lst = refresh_saves(CUR)
        
        from nodes.models.page import Page
        
        if len(max(lst)) < CUR[0][0].vec[0] or len(max(lst)) < CUR[0][0].vec[1]:
            pgn = Page(CUR[0][0].vec[0], CUR[0][0].vec[1], CUR[0][0].character)
        else:
            pgn = Page(len(max(lst)), len(lst)+7, CUR[0][0].character)
            
        for text in lst:
            pgn.create_text(text[:len(text)-4], "UPPER")
        btn = Button(1, pgn.vec[1]-5, "Cargar", __loader)
        btn.cast(("Ingrese el archivo a cargar",))
        
        btn_1 = Button(1, pgn.vec[1]-3, DEFAULT="BACK")
        btn_1.cast()

        pgn.add_btn(btn)
        pgn.add_btn(btn_1)

        pgn.start_cast()
    
def __save__():
    temp = {}
    for mapa in CUR[2]:
        temp[f"{mapa.id}"] = mapa.meta
    
    if start_test():
        save_node(temp)
        
    __main_return__()
    return

class Button(gen_wns, gen_obj, gen_btn):
    def __init__(self, 
                 X:int, 
                 Y:int, 
                 CHR:str="", 
                 ACTION=..., 
                 DEFAULT:Literal["PLAY",
                                 "EXIT",
                                 "LOAD", 
                                 "SAVE", 
                                 "BACK", 
                                 "CONTINUE",
                                 "CUSTOM"]=...,
                 NMO="",
                 ) -> None:
        N_NUM[1] +=1
        super().__init__(X, Y, CHR, N_ABS[1], N_NUM[1], NMO)
        
        self.select = DEFAULT

        if self.id == 1:
            super().__default__()
        
        match self.select:
            case "PLAY":
                if CHR == "":
                    self.character = "Jugar"
                super().__action__(__play__)
            case "SAVE":
                if CHR == "":
                    self.character = "Guardar"
                super().__action__(__save__)
            case "EXIT":
                if CHR == "":
                    self.character = "Salir"
                super().__action__(__queque__)
            case "LOAD":
                if CHR == "":
                    self.character = "Cargar"
                super().__action__(__load__)
            case "BACK":
                if CHR == "":
                    self.character = "Regresar"
                super().__action__(__main_return__)
            case "CONTINUE":
                if CHR == "":
                    self.character = "Continuar"
                super().__action__(__continue__)
            case "CUSTOM":
                super().__action__(ACTION)
            case _:
                super().__action__(ACTION)
    
    def cast(self, msg:tuple=("")):
        self.cast = msg
        
