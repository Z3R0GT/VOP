from ..obj.const.const import DEFAULT


class gen_move():
    def __coords__(self):
        """
        Agrega coordenadas a objetos con base a su posición en el espacio
        """
        self.global_x = self.vec[0]
        self.global_y = self.vec[1]

    def _zero_in(self):
        """
        Agrega entradas para objetos que puedan moverse
        """
        self.__in_x = 0
        self.__in_y = 0

    def _check_nxt_foot(self, coll: list) -> tuple:
        """
        Verifica si el siguiente movmiento no tiene un caracter de colision, sean
        True || False los indicadores
        """
        self.lim = (self.map.vec[0], self.map.vec[1])

        if len(coll) == 0:
            return False, ""

        x = self.__in_x
        y = self.__in_y

        for collision in coll:
            # Verifica que las cordenas no pasen el limite
            if (self.global_x + x != self.lim[0] and self.global_x + x < self.lim[0]) and (
                    self.global_y + y != self.lim[1] and self.global_y + y < self.lim[1]):
                
                if x != 0:
                    if self.map.square[self.global_y][self.global_x + x] == collision:
                        return False, collision
                    return True, collision
                elif y != 0:
                    if self.map.square[self.global_y + y][self.global_x] == collision:
                        return False, collision
                    return True, collision
                
            else:
                print("Limite excedido")
                return False, collision

    def __get_objs(self) -> list:
        """
        Retorna la información de los objetos registrados del mapa 
        al momento de crearse (si se modifican más adelante no aparecen aqui)
        """
        chr_obj = []
        nme_obj = []
        dat_obj = []

        obj_lst = self.map.meta["node_lst"]["obj"]
        for lst in range(len(obj_lst)):
            if not obj_lst[lst]["chr"] in chr_obj:
                chr_obj.append(obj_lst[lst]["chr"])
                nme_obj.append(obj_lst[lst]["name"])
                dat_obj.append(obj_lst[lst]["data"])

        return chr_obj, nme_obj, dat_obj

    def __take_obj(self, info, check):
        n = 0
        for i in info[0]:
            n += 1
            if i == check[1]:
                try:
                    if self.inv[info[1][n-1]]:
                        self.inv[info[1][n-1]][0] += 1
                except KeyError:
                    self.inv[info[1][n-1]] = [1, info[2][n-1]]
                
                break

    def _move_body(self, in_):
        """
        Función general que simula el movmiento 
        """
        if DEFAULT[1][2]:
            return

        self._zero_in()
        w, s, a, d = self.controll

        if in_ == w:
            self.__in_y = -1
        elif in_ == s:
            self.__in_y = 1
        elif in_ == a:
            self.__in_x = -1
        elif in_ == d:
            self.__in_x = 1

        self.input = (self.__in_x, self.__in_y)

        if self._check_nxt_foot(self.coll)[0]:
            info = self.__get_objs()
            
            for nma in range(len(info[0])):
                check = self._check_nxt_foot(info[0][nma])
                if not check[0]:
                    self.__take_obj(info, check)
            self._appear_map()