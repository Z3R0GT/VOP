from .obj.gen_obj import gen_obj, N_NUM, N_ABS, CUR, DEFAULT
from .obj.gen_wns import gen_wns

from .obj.tools.debug import print_debug, _insert

class Mapa(gen_obj, gen_wns):
    """
    Lienzo en el que puedes agregar nodos tanto visible como no, usado
    también como "Mundo" donde ocurre todo
    """
    def __init__(self, 
                 X, 
                 Y, 
                 CHR,  
                 NMO="") -> None:
        N_NUM[2] += 1
        super().__init__(X, Y, CHR, N_ABS[2], N_NUM[2], NMO)
        super().__wns__()
        
        CUR[2].append(self)
        
        self.coll = []
        
        self.node_list = {
            "obj": [],
            "stu": [],
            "pla": [],
            "cam": [],
            "npc": []
            }
        
        self._set_meta("coll", self.coll)
        self._set_meta("node_lst", self.node_list)

        self._create_line()
        self._create_line_num()

    def _check_own(self, node) -> bool:
        """
        Verifica si un cierto nodo pertecene al mapa
        """
        return self.id != node.meta["map"][0]
    
    def erase_coll(self, obj):
        """
        Elimina una letra con la que otros nodos puedan chocar
        """
        if self._check_own(obj):
            return
        
        c = -1
        for coll in self.choll:
            c += 1
            if coll == obj.character:
                self.coll[c] = f"{obj.abs}_{self.id}"
        self._set_meta("coll", self.coll)
    
    def add_coll(self, obj):
        """
        Agrega una letra con la que otros nodos puedan chocar
        """
        if self._check_own(obj):
            return
        
        c = -1
        for coll in self.coll:
            c+=1
            if len(coll) > 1:
                if coll[0:3] == obj.abs and coll[4] == obj.id:
                    self.coll[c] = obj.character
                    
        if obj.character not in self.coll:
            self.coll.append(obj.character)
        
        self._set_meta("coll", self.coll)
        
    def add_node(self, node, exception:bool=False):
        """
        Agrega un nodo dentro del lienzo del mapa o "meta" interno
        (se aplica cada objeto visible no boton o pagina/page)
        """
        if self._check_own(node):
            print_debug(f"{node.name} no pertenece a {self.name}")
            return
        
        if node.abs == "stu":
            if self.vec[0] < node.vec[0] or self.vec[1] < node.vec[1]:
                print_debug("Nodo escede los limites")
                return
            
            c = 0
            for y in range(self.vec[1]):
                if y in range(node.vec[1], (node.vec[1] + node.transform[1])):
                    c += 1
                    for x in range(self.vec[0]):
                        if x in range(node.vec[0], (node.vec[0] + node.transform[0])):
                            self.square[y] = _insert(
                                self.square[y],
                                node.square[(c - 1)],
                                node.vec[0],
                                (node.transform[0] + 1)
                            )
            ck = True
            
        elif node.abs == "obj":
            self.square[node.vec[1]] = _insert(
                self.square[node.vec[1]],
                node.character,
                specific_=node.vec[0]
                )
            ck = True
            
        elif node.abs == "pla":
            DEFAULT[0] = node
            ck = True
            
        else:
            ck = True
            
        if ck:
            if not exception:
                self.node_list[node.abs].append(node.meta)
                self._set_meta("node_lst", self.node_list)
            
            self._create_pre_view()
    """   
    #1.4: NO EXISTE YA QUE SE REQUIERE PULIR ALGUNAS COSAS
    def del_node(self, node):
        if self._check_own(node):
            return

        a = None

        # TODO:CAMBIAR DE SER NECESARIO U AGREGAR
        if node.abs == "stu":
            from nodes.models.structure import Struture

            a = Struture(self, node.vec[0], node.vec[1], node.transform[0], node.transform[1], self.character, False,f"del_stu_{node.id}")
        elif node.abs == "obj":
            from nodes.models.object import Object

            a = Object(self, node.vec[0], node.vec[1], self.character, f"del_obj_{node.id}", False, DATA=None)
        else:
            ...

        n = 0
        for nodes in self.node_list[node.abs]:
            if nodes[0] == node.id:
                self.node_list[node.abs][n - 1] = [a.id, a.name]
            n += 1
        self.add_node(a, True)
    """
