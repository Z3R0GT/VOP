from ..obj.tools.debug import _insert, print_debug

import random as rn

class gen_pla:
    """
    Clase encargada para todo nodo que requiera moverse o sea interactivo
    """
    def __start__(self,
                 EXPT_COLL,
                 CONTROLL,
                 CIFS):
        """
        Hecho para objetos que se puedan mover e "interactuar"
        """
        self.controll = CONTROLL

        self.__in_x: int = 0
        self.__in_y: int = 0
        self.input = (0, 0)

        self.cifs = CIFS

        self.expt_coll = EXPT_COLL
        self.coll = [""]
        self._refresh_coll()

        self._set_meta("controll", self.controll)
        self._set_meta("cifs", self.cifs)
        self._set_meta("expt_coll", self.expt_coll)
        self._set_meta("coll", self.coll)

        temp = self.vec

        #error x2
        c = -1
        while True:
            if c == 10:
                return print_debug("TIENE QUE AGREGAR ALMENOS UNA LETRA DE COLISIÓN")
            c+= 1
            if self._apper_check():
                break
            else:
                self._apper_check()

        if temp != self.vec:
            print(
                f"LAS CORDENADAS FUERON CAMBIADAS DE (X:{self._temp_vec[0]};Y:{self._temp_vec[1]}) A (X:{self.vec[0]};Y:{self.vec[1]}" +
                f"POR ESTAR CHOCANDO CON EL CARACTER: {self.coll}")

        self._appear_map()

        self._set_meta("global_x", self.global_x)
        self._set_meta("global_y", self.global_y)

    def _apper_check(self) -> bool:
        """
        Verifica si la posición donde aparecera no tiene un caracter de colisión, sino,
        aleatoriamente buscara uno que no lo tenga
        """
        for coll in self.coll:
            if coll == self.map.square[self.vec[1]][self.vec[0]]:
                self.vec[0] += rn.randrange(-1, 2)
                if coll == self.map.square[self.vec[1]]:
                    self.vec[1] += rn.randrange(-1, 2)
                    self.__coords__()
                    return False
                else:
                    pass
                self.__coords__()
                return False
            else:
                return True

    def _refresh_coll(self):
        """
        actualiza los caracteres de colisión del objeto
        """
        if len(self.expt_coll) != 0:
            for coll_gen in self.map.coll:
                for coll_expt in self.expt_coll:
                    if coll_gen != coll_expt:
                        self.coll.append(coll_gen)
        else:
            self.coll = self.map.coll

    def _appear_map(self):
        """
        Inserta al objeto dentro del mapa sea las coordenada .global_x & .global_y las posiciones
        :return: .map.square[global_y][global_x]
        """

        self.map.square[self.global_y] = _insert(
            self.map.square[self.global_y],
            self.map.character,
            specific_=self.global_x)

        self.global_x += self.input[0]
        self.global_y += self.input[1]

        self._edit_meta("global_x", ..., self.global_x)
        self._edit_meta("global_y", ..., self.global_y)

        self.map.square[self.global_y] = _insert(
            self.map.square[self.global_y],
            self.character,
            specific_=self.global_x)

        self.map._create_pre_view()

    def some_info(self):
        """
        Información importante respecto al objeto que se mueve
        """
        n = f"¿{self.name} ({self.abs}), Coordenadas de entrada: (X:{self.input[0]};Y:{self.input[1]}) Posición actual: (X:{self.global_x};Y:{self.global_y})"
        #sb.run([sys.executable, "-c", f"print('{n}')"])
        print(n)
