from time import sleep
from typing_extensions import Literal

from .obj.tools.debug import erase_screen, _chk_window, set_console_font

from .internal.admin_dir import save_node, load_save
from .internal.archives import refresh_saves, start_test, _check_save

from .obj.const.const import CUR, DEFAULT, N_WN, N_NUM, N_ABS

from .obj.gen_wns import gen_wns
from .obj.gen_obj import gen_obj, gen_btn

def __loader(*ID):
    """
    Se encarga de cargar una partida guardada dado la posición (ID) de un archivo guardado en una carpeta
    (siempre sera "saves")
    """
    
    ld = load_save(CUR[4][int(ID[0][0])-1])
    
    from .mapa import Mapa
    from .camera import Camera
    from .object import Object
    from .player import Player
    from .structure import Structure
    
    CUR[2] = []
    CUR[1] = []
    
    for i in range(len(N_NUM)):
        if i > 1:
            N_NUM[i] = 0
        
    #RECORRE CADA APARTADO DEL MAPA
    for i in range(len(ld)):
        id = ld[f"{i+1}"]
        vc = id["vec"]
        chr = id["chr"]
        nma = id["name"]
        lst = id["node_lst"]
        #asb = id["abs"] ?????
        
        m = Mapa(vc[0], vc[1], chr, nma)
        for node in lst:
            #RECORRE LOS OBJETOS GUARDADOS PARA CREARLOS
            for obj in lst[node]:
                match obj["abs"]:
                    case "obj":
                        n = Object(m, 
                                      obj["vec"][0], 
                                      obj["vec"][1],
                                      obj["chr"],
                                      obj["data"],
                                      obj["name"]
                                      )
                        m.add_node(n)
                    case "pla":
                        p = Player(m, 
                                   obj["global_x"], 
                                   obj["global_y"], 
                                   obj["chr"], 
                                   obj["expt_coll"], 
                                   obj["name"],
                                   obj["controll"],
                                   obj["cifs"]
                                   )
                        p.inv = obj["inv"]
                        m.add_node(p)
                    case "cam":
                        c = Camera(m,
                                   [obj["vec"][0], obj["transform"][0], obj["vec"][1], obj["transform"][1]], 
                                   obj["name"],
                                   obj["lck"]
                                   )
                        
                        m.add_node(c)                        
                    case "npc":
                        print("er")
                    case "stu":
                        s = Structure(m,
                                      obj["vec"][0],
                                      obj["vec"][1],
                                      obj["transform"][0],
                                      obj["transform"][1],
                                      obj["chr"],
                                      obj["is_coll"],
                                      obj["name"])
                        
                        for i in obj["size"]:
                            if len(i) == 3:
                                s.edit_geometry([i])
                            else:
                                for n in i:
                                    s.edit_geometry([n])

                        for i in range(len(obj["_chr"])):
                            s.create_door(obj["_door"][i], obj["_chr"][i])
                            
                        m.add_node(s)
        #CUANDO TERMINA EMPIEZA AUTOMATICAMENTE EL JUEGO YA SE
        #ASUME QUE ESO QUIERE EL JUGADOR                
        __play__()

def __main_return__(id=...):
    #REGRESA A LA PANTALLA PRINCIPAL
    DEFAULT[1][1] = True
    erase_screen()
    _chk_window()

    if type(id) == type(...):
        CUR[0][0].start_cast()
    else:
        CUR[0][id[0]].start_cast()
        
def __continue__():
    #LUEGO QUE TERMINA EL "PAUSE" CONTINUARA LA EJECUCIÓN 
    #1.4 ESTO NO FUNCIONA
    erase_screen()
    DEFAULT[1][2] = True
    _chk_window()

    #REEPLANTEARSE EL CODGIO LOGICO PARA EL INICIO DEL JUEGO

def __play__():
    #EMPIEZA EL JUEGO
    
    DEFAULT[1][1] = False
    _chk_window()
    #1.4 EL JUGADOR SIEMPRE SERA SOLO 1
    DEFAULT[0].move()


    #EMPIEZA EL JUEGO
    while not DEFAULT[1][1]:
        if not DEFAULT[1][2]:
            set_console_font("Terminal", 900,15)
            sleep(N_WN[2])
            
            CUR[1][DEFAULT[1][4]].render_image(False)
            
            erase_screen()
            
            CUR[1][DEFAULT[1][4]].get_pre_view()
        else:
            ...
        
        if DEFAULT[1][1]:
            continue
    #FIN DE LA EJECUCIÓN :C
       

def __queque__():
    #TERMINA EL PROGRAMA INMEDIATAMENTE
    import sys    
    sys.exit()

def __load__():
    #CARGA UNA PANTALLA DONDE SE APARECEN SOLO EL ULTIMO ARCHIVO DE GUARDADO
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
    #GUARDA LOS OBJETOS CREADOS HASTA EL MOMENTO 
    temp = {}
    for mapa in CUR[2]:
        temp[f"{mapa.id}"] = mapa.meta
    
    temp["1"]["node_lst"]["pla"] = [DEFAULT[0].meta]
    
    if start_test():
        save_node(temp)
        
    __main_return__()
    return

class Button(gen_wns, gen_obj, gen_btn):
    """
    Diseñado para guardar funciones, puede ejecutar cualquier "action" que le indique y diferenciar
    entre cuando no tiene y cuando si argumentos
    
    ACTION  --> Función
    DEFAULT --> Funciones pre-definidas
    """
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
        
        #ASIGNA UNA FUNCIÓN PRE-DEFINIDA O SOLO AGREGA LA ESCOGIDA
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
        """
        Un mensaje que aparecera para el usuario, puede un indicardo que tiene que hacer en todo caso
        """
        self.cast = msg
        
