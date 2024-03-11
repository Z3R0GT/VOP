from .obj.gen_obj import gen_obj, N_ABS, N_NUM, DEFAULT, N_WN, CUR, DEV
from .obj.gen_wns import gen_wns

class Camera(gen_obj, gen_wns):
#####################################################
#       CONSEJO:  coord: list = [-X, X, -Y, Y]      #
#####################################################
    def __init__(self, 
                 MAP,
                 COORD=[-5, 10, -2, 5],
                 NMO: str= "",
                 LOCK:bool = True):
        N_NUM[5] += 1
        super().__init__(COORD[0], COORD[2], "BARRETO ALCANTARA IMANOL EL MAS GRANDE", N_ABS[5], N_NUM[5], NMO)
        super().__wns__()
        super().__map__(MAP)
        super().__transform__(COORD[1], COORD[3])

        CUR[1].append(self)

        self.focus = DEFAULT[0]

        self._set_meta("pla", (self.focus.id, self.focus.name))
        self.render_image(LOCK)

    def fp(self):
        """
        Actualiza valor a los fotogramas impresos
        """
        if N_WN[1] < N_WN[0]:
            N_WN[1] += 1
        else:
            N_WN[1] = 0
            
    def render_image(self, is_lock:bool = False):
        """
        Crea una fotograma de la actual vista con base a "vec"(vector) dado en "COORD"  
        """
        self.fp()
        
        self._erase_pre_view()
        self._erase_square()

        #¿ESTA MIRANDO?
        if not is_lock:
            cur_ren_x = self.focus.global_x
            cur_ren_y = self.focus.global_y
        else:
            cur_ren_x = self.focus.vec[0]
            cur_ren_y = self.focus.vec[1]
        
        #CREA EL FOTOGRAMA
        for y in range(self.map.vec[1]):
            if y in range(cur_ren_y + self.vec[1], cur_ren_y + self.transform[1]):
                for x in range(self.map.vec[0]):
                    if x in range(cur_ren_x + self.vec[0], cur_ren_x + self.transform[0]):
                        self.pre_view += self.map.square[y][x]
                if DEV[0]:
                    self.square.append(self.pre_view + f"     line {self.map.abs}: {y}")
                else:
                   self.square.append(self.pre_view)
                self._erase_pre_view()
        self._create_pre_view()