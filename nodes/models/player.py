from tkinter import BUTT
import pynput as pn

from .obj.tools.debug import erase_screen

from .page import *
from .button import *

from .pla.gen_puppet import *
from .pla.gen_move import *

from .obj.gen_obj import gen_obj, N_NUM, N_ABS, DEFAULT

#FALTA CAMBIAR LA ENTRADA DE LAS TECLAS

class Player(gen_obj, gen_pla, gen_move):

    def __init__(self,
                 MAP,
                 X: int,
                 Y: int,
                 CHR: str,
                 EXPT_COLL: list = [],
                 NMO: str = "",
                 CONTROLLS: list = ["w", "s", "a", "d"],
                 CIFS: bool = False):
        N_NUM[6] += 1
        super().__init__(X, Y, CHR, N_ABS[6], N_NUM[6], NMO)
        super().__map__(MAP)
        
        self.__coords__()
        self.__start__(EXPT_COLL, CONTROLLS, CIFS)

        self.inv = {}
        self.key = pn.keyboard

        self._set_meta("inv", self.inv)

    def __on_press(self, key):
        """
        cuando la tecla es presionada, sumara o actualizara sea
        .__in_x y .__in_y las entrada
        """
        try:
            if key.char == "i":
                if not DEFAULT[1][2]:
                    DEFAULT[1][2] = True
                    pgn = Page(CUR[0][0].vec[0], CUR[0][0].vec[1], CUR[0][0].character)
                    pgn.create_text("Objetos en inventario:", "UPPER")

                    c = 0
                    for name in self.inv:
                        pgn.create_text(f"{name}: {self.inv[name][0]}", "CUSTOM", (1, 3+c))
                        pgn.create_text(f"Atributos: {self.inv[name][1]}", "CUSTOM", (1, 4+c))
                        c +=3

                    erase_screen()
                    pgn.get_pre_view()
                    
                else:
                    erase_screen()
                    DEFAULT[1][2] = False
            else:
                self._move_body(key.char)
        except AttributeError:
            # Caracteres especiales (ESC, SPACE)
            #PUEDE SER CAMBIADO
            if key == pn.keyboard.Key.esc:
                DEFAULT[1][1] = True
            elif key == pn.keyboard.Key.space:
                if not DEFAULT[1][2]:
                    DEFAULT[1][2] = True
                    
                    erase_screen()
                    pgn = Page(CUR[0][0].vec[0], CUR[0][0].vec[1], CUR[0][0].character)
                    pgn.create_text("Juego pausado", "UPPER")
                    
                    btn_1 = Button(1, CUR[0][0].vec[1]-5, DEFAULT="BACK")
                    btn_1.cast((""))
                    btn_2 = Button(1, CUR[0][0].vec[1]-4, DEFAULT="SAVE")
                    btn_2.cast((""))
                    btn_4 = Button(1, CUR[0][0].vec[1]-3, DEFAULT="EXIT")
                    btn_4.cast((""))
                    btn_3 = Button(1, CUR[0][0].vec[1]-2, DEFAULT="CONTINUE")
                    btn_3.cast((""))

                    pgn.add_btn(btn_1)
                    pgn.add_btn(btn_2)
                    pgn.add_btn(btn_3)
                    pgn.add_btn(btn_4)
                    
                    pgn.start_cast()
                else:
                    DEFAULT[1][2] = False

    def __on_realease(self, key):
        """
        Cuando la tecla dejo de ser presionada
        """
        if key == pn.keyboard.Key.esc:
            return False

    def move(self):
        """
        comienza a capturar el moviento de teclado en todo momento 
        hasta el final de la ejecución
        """
        lst = self.key.Listener(on_press=self.__on_press, on_release=self.__on_realease)
        lst.start()
       
