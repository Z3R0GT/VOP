from nodes import *
from nodes.models.obj.tools.debug import _chk_window

import time

#DEV[0] = False

yes = ["y", "yes", "ye", "ys", "si", "s", "i"]
no = ["n", "no"]
n = ["1","2","3","4","5","6","7","8","9","0"]



def _door():
    door = []    
    c = -1
    while True:
        c+=1
        if input("\n¿Quieres una puerta?\n>...") in yes:
            door.append(_x_y("la puerta", False))
            
            print(f"puerta creada en {c}")
            time.sleep(3)
        else:
            break

    return door

def _cood():
    cood = []
    while True:
        if input("\n¿Quiere editar el interior de la estructura?\n>...") in yes:
            print("CUIDADO AL ESCRIBIR LAS COORDENADAS, SE ACONSEJA TENER UN BOCETO ANTES DE HACER ESTO")
            time.sleep(5)

            ln = input("\n¿En que posición del lienzo aparecera?\n(X, Y, -Y)\n>...")
                            
            if not (len(ln) > 1) and (ln in ["X", "Y", "-Y"]):
                time.sleep(3)
                m1 = _x_y("la linea vertical")
                                
                time.sleep(3)          
                m2 = _x_y("la linea horizontal")
                                
                m = [ln]
                n = m1 + m2
                for i in n:
                    m.append(i)
                                    
                cood.append(m) 
                print("\nCoordenadas guardadas")
                time.sleep(3)
            else:
                print("\nSolo ingresa una posición dada")
        else:
            return cood



def _pre(node):
    try:
        _chk_window(node.transform[0], node.transform[1], True)
    except:
        _chk_window(node.vec[0], node.vec[1], True)
        
    node.get_pre_view()
    
    while True:
        if input("\n¿Terminaste? (si/no) \n>...") in yes:
            _chk_window()
            return

def _x_y(nm = "", co=True):
    while True:
        try:
            if co:
                x, y = input(f"\n¿Cuan largo y ancho debe ser {nm}? (separalos por   una coma)\n>...").split(",")
            else:
                x, y = input(f"\n¿En que posición debe ubicarse {nm}? (separalos por   una coma)\n>...").split(",")
            
            x = int(x)
            y = int(y)

            break
        except ValueError:
            try:  
                _chk_window()
                print(f"\nIntenta con números. \
                      \nTipos: x:{type(x)}, y:{type(y)} \
                      \nValores: x:{x}, y:{y}")
                time.sleep(5)
            except UnboundLocalError:
                _chk_window()
                print("\nDebe separar los números por una coma, o ingresar el   número faltante")
                time.sleep(5)

    return x, y

def _ch(nme):
    while True:
        ch = input(f"\n¿Cual es la letra que usara tu {nme}? \
                    \n>...")
        
        if not ch == "":
            break
        elif len(ch) > 1:
            _chk_window()
            print("\nSolo puedes usar una letra")
            time.sleep(4)
        else:
            _chk_window()
            print("\nDebes ingresarlo otra vez")
            time.sleep(4)

    return ch

def _nm(nm):
    return input(f"\n¿Como quieres que llame tu {nm}? (opcional)\
                   \n>...")

def _mp(nm):
    while True:
        print("Mapa IDs:")
        for i in CUR[2]:
            print(f"ID: {i.id}; NOMBRE: {i.name}")
        
        try:
            return int(input(f"\nIngresa el ID del mapa para añadir {nm}\n>..."))
        except:
            print("\nIngresa un valor numerico")
            time.sleep(3)
            _chk_window()
              
def _dt():
    while True:
        dt = input("\nIngresa los atributos y los valores respectivos\
\nrecuerda separarlos por comas y que sea el total de datos par\
\n{atributos}, {valores}\n>...").split(",")
        if not len(dt)%2 == 0:
            print("\nIngresa los datos en pares para tener conversión automatica\n")
            time.sleep(7)
            _chk_window()
        else:
            l = {}
            for i in range(0, len(dt), 2):
                match dt[i+1][1]:
                    case "[":
                        l[dt[i]] = list(dt[i+1].replace("[", "").replace("]", "").replace(" ", ""))
                    case "{":
                        l[dt[i]] = dict(one=dt[i+1].replace("{", "").replace("}", "").replace(" ", ""))
                    case "(":
                        l[dt[i]] = tuple(dt[i+1].replace("(", "").replace(")", "").replace(" ", ""))
                    case _:
                        if dt[i+1][1] in n:
                            l[dt[i]] = float(dt[i+1].replace(" ", ""))
                        else:
                            l[dt[i]] = dt[i+1]    
            break
        
    return l




def _rtr(nme, tu=False):
    if input(f"\n¿Vas a crear otro {nme}? (si/no) \n>...").lower() in no:
        if not tu:
            btn_sim = Button(0, 0, "a", DEFAULT="BACK")
            btn_sim.execute(1) 
        else:
            return False
    else:
        if not tu:
            return True
        else:
            return False

def _rtc():
    return input("\n¿Todos lo datos están correctos? (si/no)\n>...").lower() in yes

def _rtm(nm):
    if len(CUR[2]) > 1:
        mp = _mp(nm)
    else:
        mp = 0
    return mp

def _rts(door=..., cood=..., spc=...):
    
    if type(spc) == type(...):
        spc = input("\n¿Desea ver las posiciones de las puertas o modificaciones? (1, 2, 3)\n>...").lower()
    
    while True:
        c = -1
        match spc:
            case "1":
                for i in range(len(door)):
                    if not len(door) < 3:
                        c+=2
                        print(f"{i}: {door[i]}; {i+1}: {door[i+1]}; {i+2}: {door[i+2]}")
                    else:
                        c+=1
                        print(f"{i}: {door[i]}")
                    if i-2 == c:
                        break
                while True:
                    if input("\n¿Desea modificar las posiciones? (si/no)\n>...") in yes:
                        try:
                            n = input("\n¿Cuál es la ubicación? (en caso quiera agregar uno nuevo, ingresa ´ _ ´)\n>...")
                            if n == "_":
                                for i in _door():
                                    door.append(i)
                                else:
                                    door[int(n)] = _x_y("la puerta", False)
                        except ValueError:
                            print("\nIngresa un valor númerico valido")
                            time.sleep(5)
                            _chk_window()
                    else:
                        break
            case "2":
                c = -1
                for i in range(len(cood)):
                    if len(cood) < 1:
                        c+=2
                        print(f"{i}: {cood[i]}; {i+1}: {cood[i+1]}; {i+2}: {cood[i+2]}")
                    else:
                        c+=1
                        print(f"{i}: {cood[i]}")
                    if i-2 == c:
                        break
                while True:
                    if input("\n¿Desea modificar las posiciones? (si/no)\n>...") in yes:
                        try:
                            n = input("\n¿Cuál es la ubicación? (en caso quiera agregar uno nuevo, ingresa ´ _ ´)\n>...")
                            if n == "_":
                                for i in _cood():
                                    cood.append(i)
                            else:
                                cood[int(n)] = [input("\n¿En que posición del lienzo aparecera?\n(X, Y, -Y)\n>..."),
                                _x_y("la linea vertical") + _x_y("la linea horizontal")]
                        except ValueError:
                            print("\nIngresa un valor númerico valido")
                            time.sleep(5)
                            _chk_window()
                    else:
                        break
            case "3":
                break
            case _:
                print("\nIngresa alguno de los números ofrecidos\n")
                time.sleep(7)
                _chk_window()
        break
    
    if type(door) == type(...):
        return cood
    elif type(cood) == type(...):
        return door
    else:
        return door, cood



def cr_mp(tu=False): 
    #bucle base
    while True:
        #limpieza
        _chk_window()

        print("\nEstas por crear un mapa, asegurate de responder todas  las preguntas según corresponda \n\
\n Recuerda que solo puedes crear de largo hasta 120     casillas, \
con un máximo definitivo de 209 y un ancho de hasta 46, con un máximo de 48 \
esto para pantallas con una resolución de 1920x1080 \n\
\n Nota: Puede crear libremente con cualquier tamaño,    pero toma en cuenta que esas son medidas recomendadas")
        time.sleep(7)
            
        cood_x, cood_y = _x_y("el mapa")
        ch = _ch("mapa")
        nm = _nm("mapa")
        
        if cood_x < 120 or cood_y < 46:
            print("Estas superando el limite recomendado")
        elif cood_x < 209 or cood_y < 48:
            print("Estás superando el límite máximo recomendado, le recomiendo cambiarlo")
            
        _chk_window()
        
        print(f"\
              \nDatos:\n\
              Parte 1: largo: {cood_x}\n\
              Parte 1: ancho: {cood_y}\n\
              Parte 2: letra: {ch}\n\
              Parte 3: nombre:{nm}")
        if _rtc():
            ...
        else:
            while True:
                _chk_window()
                print(f"\
                      \nDatos:\n\
                      Parte 1: largo: {cood_x}\n\
                      Parte 1: ancho: {cood_y}\n\
                      Parte 2: letra: {ch}\n\
                      Parte 3: nombre:{nm}")
                match input("\n¿En que parte fallaste? (1, 2, 3)\n>..."):
                    case "1":
                        cood_x, cood_y = _x_y("el mapa")
                    case "2":
                        ch = _ch("mapa")
                    case "3":
                        nm = _nm("mapa")
                    case _:
                        print("Ingresa alguno de los números ofrecidos")
                time.sleep(3)    
                _chk_window()
                if input("\n¿Terminaste?(si/no)\n>...").lower() in yes:
                    break

        
        n = Mapa(cood_x, cood_y, ch, nm)
        print("\n Su pre-visualización esta cargando, un momento")
        time.sleep(3)
        _pre(n)
        break
    
    if _rtr("mapa", tu):
        cr_mp()
    
def cr_st(tu=False):
    while True:
        _chk_window()
        print("\nEstas por crear una estructura, asegurate de responder todas  las preguntas según corresponda \n")
        time.sleep(3)
        
        while True:
            mp = _rtm("estructura")
            if mp > len(CUR[2]):
                print("\nDebes ingresar un ID correcto\n")
                
                time.sleep(3)
                _chk_window()
            else:
                break
        
        cood_x, cood_y = _x_y("la estructura", False)
        
        tr1, tr2 = _x_y("la estructura")
        
        ch = _ch("estructura")
        
        if input("\n¿Se puede golpear contra la estructura?\n>...").lower() in yes:
            co = True
        else:
            co = False
            
        nm = _nm("estructura")
        
        if tu:
            door = []
            cood = []
        else:
            door = _door()
            cood = _cood()
            
        if len(door) > 0:
            md = _ch("puerta")
        else:
            md = DEFAULT[3]

        _chk_window()

        print(f"\
              \nDatos:\n\
              Parte 1: ID:             {mp}\n\
              Parte 2: X:              {cood_x}\n\
              Parte 2: Y:              {cood_y}\n\
              Parte 3: largo:          {tr1}\n\
              Parte 3: ancho:          {tr2}\n\
              Parte 4: letra:          {ch}\n\
              Parte 5: Conlisionable:  {co}\n\
              Parte 6: nombre:         {nm}\n\
              Parte 7: letra de puerta:{md}")

        if _rtc:
            ...
        else:
            while True:
                _chk_window()
                print(f"\
                      \nDatos:\n\
                      Parte 1: ID:             {mp}\n\
                      Parte 2: X:              {cood_x}\n\
                      Parte 2: Y:              {cood_y}\n\
                      Parte 3: largo:          {tr1}\n\
                      Parte 3: ancho:          {tr2}\n\
                      Parte 4: letra:          {ch}\n\
                      Parte 5: Conlisionable:  {co}\n\
                      Parte 6: nombre:         {nm}\n\
                      Parte 7: letra de puerta:{md}")
                match input("\n¿En que parte fallaste? (1-7)\n>..."):
                    case "1":
                        mp = _rtm("la estructura")
                    case "2":
                        cood_x, cood_y = _x_y("la estructura", False)
                    case "3":
                        tr1, tr2 = _x_y("la estructura")
                    case "4":
                        ch = _ch("la estructura")
                    case "5":
                        if input("¿Se puede golpear contra la estructura?").lower() in yes:
                            co = True
                        else:
                            co = False
                    case "6":
                        nm = _nm("estructura")
                    case "7":
                        if len(door) > 0:
                            md = _ch("puerta")
                    case _:
                        print("\nIngresa alguno de los números ofrecidos\n")
                time.sleep(3)    
                _chk_window()
                if input("\n¿Terminaste?(si/no)\n>...").lower() in yes:
                    break
        
        n_c = Structure(CUR[2][mp], cood_x, cood_y, tr1, tr2, ch, co, nm)
        
        if not tu:
            door, cood = _rts(door, cood)
            while True:
                match input("\nPuede aplicar modificaciones de puertas u estructurales o también que sea automaticamente (1, 2, 3)\n>..."):
                    case "1":
                        while True:
                            print("\nAplicando modificaciones de puertas")
                    
                            for i in door:
                                print(i)
                        
                            print("Puertas aplicadas, imprimiendo...")
                            _chk_window(n_c.transform[0], n_c.transform[1], True)
                            time.sleep(3)

                            n_c.get_pre_view()
                    
                            if input("¿Mantienes los cambios?(si/no)") in yes:
                                break
                            else:
                                _rts(door, ... , spc=1)    
                    case "2":
                        print("\nAplicando modificaciones estructurales")
                    
                        for i in cood:
                            print(i)
                        
                        print("Modificaciones aplicadas, imprimiendo")
                        _chk_window(n_c.transform[0], n_c.transform[1], True)
                        time.sleep(3)
                    
                        n_c.get_pre_view()
                    
                        if input("¿Mantienes los cambios?(si/no)") in yes:
                            break
                        else:
                            _rts(..., cood , spc=2)
                    case "3":
                        _chk_window(n_c.transform[0], n_c.transform[1], True)
                        print("PROCEDE APLICANDO LO MODIFICADORES")
                        if len(door) > 0:
                            n_c.create_door(door)
                        
                        if len(cood) > 0:
                            for i in cood:
                                n_c.create_geometry(i[0], i[1], i[2], i[3], i[4])

                        n_c.get_pre_view()
                        time.sleep(5)
                        break
                    case _:
                        print("\nIngresa alguno de los números ofrecidos\n")
        else:
            ...
            
        CUR[2][mp].add_node(n_c)
        _chk_window(n_c.transform[0], n_c.transform[1], True)
        print("\n Su pre-visualización esta cargando, un momento")
        time.sleep(3)
        
        n_c.get_pre_view()
        break
    
    if _rtr("estructura", tu):
        cr_st()
   
def cr_pl():
    while True:
        _chk_window()
        print("\nEstas por crear un jugador, asegurate de responder todas  las preguntas según corresponda \n")
        time.sleep(7)
        
        mp = _rtm("el jugador")

        cood_x, cood_y = _x_y("el jugador", False)
        
        ch = _ch("jugador")

        co = input("¿Con qué letra no puede golpearse el jugador? (recuerda separarlo por comas)\n...").replace(" ", "").split(",")

        nm = _nm("jugador")

        print("El jugador tiene usa las teclas ´wasd´ para controlar el movimiento")
        time.sleep(5)

        _chk_window()
        
        print(f"\
              \nDatos:\n\
              Parte 1: ID:              {mp}\n\
              Parte 2: X:               {cood_x}\n\
              Parte 2: Y:               {cood_y}\n\
              Parte 3: letra:           {ch}\n\
              Parte 4: No se golpea con:{co}\n\
              Parte 5: nombre:          {nm}")

        if _rtc:
            ...
        else:
            while True:
                _chk_window()
                print(f"\
                      \nDatos:\n\
                      Parte 1: ID:              {mp}\n\
                      Parte 2: X:               {cood_x}\n\
                      Parte 2: Y:               {cood_y}\n\
                      Parte 3: letra:           {ch}\n\
                      Parte 4: No se golpea con:{co}\n\
                      Parte 5: nombre:          {nm}")
                match input("\n¿En que parte fallaste? (1, 2, 3, 4, 5)\n>...").replace(" ", ""):
                    case "1":
                        mp = _rtm("el jugador")
                    case "2":
                        cood_x, cood_y = _x_y("el jugador")
                    case "3":
                        ch = _ch("jugador")
                    case "4":
                        co = input("¿Con que letra no puede golpearse el jugador? (recuerda separar lo por comas)\n>...").replace(" ", "").split(",")
                    case "5":
                        nm = _nm("jugador")
                    case _:
                        print("\nIngresa alguno de los números ofrecidos\n")
                time.sleep(3)
                _chk_window()
                print(f"\
                      \nDatos:\n\
                      Parte 1: ID:              {mp}\n\
                      Parte 2: X:               {cood_x}\n\
                      Parte 2: Y:               {cood_y}\n\
                      Parte 3: letra:           {ch}\n\
                      Parte 4: No se golpea con:{co}\n\
                      Parte 5: nombre:          {nm}")
                if input("\n¿Terminaste?(si/no)\n>...").lower() in yes:
                    break
        p = Player(CUR[2][mp], cood_x, cood_y, ch, co, nm)
        CUR[2][mp].add_node(p)
        break
    
    if _rtr("jugador"):
        cr_pl()
    
def cr_ob(tu=False):
    while True:
        _chk_window()
        
        print("\nEstas por crear un objeto, asegurate de responder todas  las preguntas según corresponda \n")
        time.sleep(7)
        
        mp = _rtm("el objecto")
        
        cood_x, cood_y = _x_y("el objeto", False)
        
        ch = _ch("objeto")
        
        dt = _dt()
        
        nm = _nm("objeto")
        
        _chk_window()
        
        print(f"\
              \nDatos:\n\
              Parte 1: ID:     {mp}\n\
              Parte 2: largo:  {cood_x}\n\
              Parte 2: ancho:  {cood_y}\n\
              Parte 3: letra:  {ch}\n\
              Parte 4: Datos:  {dt}\n\
              Parte 5: nombre: {nm}")
        
        if _rtc:
            ...
        else:
            while True:
                _chk_window()
                print(f"\
                      \nDatos:\n\
                      Parte 1: ID:     {mp}\n\
                      Parte 2: largo:  {cood_x}\n\
                      Parte 2: ancho:  {cood_y}\n\
                      Parte 3: letra:  {ch}\n\
                      Parte 4: Datos:  {dt}\n\
                      Parte 5: nombre: {nm}")
                match input("\n¿En que parte fallaste? (1, 2, 3, 4, 5)\n>...").replace(" ", ""):
                    case "1":
                        mp = _rtm("el objecto")
                    case "2":
                        cood_x, cood_y = _x_y("el objeto", False)
                    case "3":
                        ch = _ch("objeto")
                    case "4":
                        dt = _dt()
                    case "5":
                        nm = _nm()
                    case _:
                        print("\nIngresa alguno de los números ofrecidos\n")
                time.sleep(3)
                _chk_window()
                print(f"\
                    \nDatos:\n\
                      Parte 1: ID:     {mp}\n\
                      Parte 2: largo:  {cood_x}\n\
                      Parte 2: ancho:  {cood_y}\n\
                      Parte 3: letra:  {ch}\n\
                      Parte 4: Datos:  {dt}\n\
                      Parte 5: nombre: {nm}")
                if input("\n¿Terminaste?(si/no)\n>...").lower() in yes:
                    break

        p = Object(CUR[2][mp], cood_x, cood_y, ch, dt, nm)
        CUR[2][mp].add_node(p)
        break
    if _rtr("objeto", tu):
        cr_ob()

def cr_cm():
    """
    INCLUIRLO EN EL CODIGO
    
    if len(CUR[2]) == 0:
        _chk_window()
        print("\n TIENES QUE CREAR UN MAPA PRIMERO ANTES DE CONTINUAR\n")
        btn_sim = Button(0, 0, "a", DEFAULT="BACK")
        btn_sim.execute() 
        return
    else:
        for i in CUR[2]:
            try:
                if len(i.meta["node_lst"]["pla"][0]["coll"]) == 0:
                    _chk_window()
                    print("\nDEBES CREAR UNA ESTRUCTURA QUE EL JUGADOR PUEDE CHOCAR\n")
                    return
            except IndexError:
                print("\nDebes crear un jugador/agregar un jugador")
    """       
    while True:
        _chk_window()
        
        print("\n Estas por crear una cámara, asegurate de responder    todas las preguntas según corresponda \n")

        time.sleep(7)
        
        mp = _rtm("camara")
            
        print("\nPrevio a crear una cámara, se recomienda usar la       configuración -5 10 | -2 5 \n\
(ingresalo de a dos como aparecen), recuerda se        requiere 4 coordenadas respecto al jugador, \
además que se ordena en: X; -X; -Y; Y\n")
        
        if input("\nSeguro que quiere personalizar tu cámara? (si,no)\n>...") in yes:
            cood_x, _cood_x, cood_y, _cood_y = _x_y("la camara") + _x_y("la camara")
        else:
            cood_x, _cood_x, cood_y, _cood_y = [-5, 10, -2, 5]

        nm = _nm("camara")

        if input("\n¿La cámara seguira al jugador? (si/no)\n>...").lower() in yes:
            co = False
        else:
            co = True
        
        while True:
            _chk_window()
            DEV[0] = True

            mc = Camera(CUR[2][mp], [cood_x, _cood_x, cood_y, _cood_y], nm, co)
            CUR[2][mp].add_node(mc)
            print("\nLa pre visualización esta cargando...\n")
            time.sleep(3)

            mc.get_pre_view()
            
            time.sleep(10)

            print(f"\
              \nDatos: \n\
              Parte 1: ID:                  {mp}\n\
              Parte 2: X:                   {cood_x}\n\
              Parte 2: -X:                  {_cood_x}\n\
              Parte 2: Y:                   {cood_y}\n\
              Parte 2: -Y:                  {_cood_y}\n\
              Parte 3: nombre:              {nm}\n\
              Parte 4: persigue al jugador: {co}")
            
            DEV[0] = False
            
            if _rtc():
                ...
            else:
                while True:
                    _chk_window()
                    print(f"\
              \nDatos: \n\
              Parte 1: ID:                  {mp}\n\
              Parte 2: X:                   {cood_x}\n\
              Parte 2: -X:                  {_cood_x}\n\
              Parte 2: Y:                   {cood_y}\n\
              Parte 2: -Y:                  {_cood_y}\n\
              Parte 3: nombre:              {nm}\n\
              Parte 4: persigue al jugador: {co}")
                    match input("\n¿En que parte fallaste? (1, 2, 3, 4)\n>..."):
                        case "1":
                            mp = _rtm("camara")
                        case "2":
                            cood_x, _cood_x, cood_y, _cood_y = _x_y("la camara") + _x_y("la camara") 
                        case "3":
                            nm = _nm("camara")
                        case "4":
                            if input("\n¿Quieres que la cámara siga el jugador, o solo se       queda quieta?").lower() in yes:
                                co = False
                            else:
                                co = True
                        case _:
                            print("\nIngresa alguno de los números ofrecidos\n")
                    break
            break
        break
    
    if _rtr("camara"):
        cr_cm()

"""
conocimiento avanzado: la camara, uso de ID para mapas multiples, 
modificación de estructuras con añadir puertas, jugador
"""

def tut():

    _chk_window()


    print("¡Bienvenido al tutorial! \
\n Primero que nada, antes de empezar, ten a la mano un  cuaderno cuadriculado, lápiz, borrador y un sacapunta.\
\n ahora, vamos a mirar unos conceptos básicos: primero, la hoja cuadriculada, representa el lienzo donde se \
   trabajará todo el juego este, lo llamaremos ´mapa´, \
   dentro, puedes dibujar diferentes casillas con varias \
 formas, y unirlas para crear cuadrados o rectángulos, a\
La unión de todas, la llamaremos ´estructura´. \n \
\n como estas creando un juego, vas a tener que agregar \
 una casilla dibujada diferente a las demás, a esta la \
  llamaremos ´jugador´ que seria alguien como tú o como \
yo pero que vivirá seguramente una gran aventura. \n \
\n el ´jugador´ podrá moverse por todo el ´mapa´, pero \
va a tener que interactuar con algo ¿no?, ¿de que \
sirve  una aventura sin una recompensa?, bueno, al \
igual que  el jugador, podemos dibujar una de las \
casillas del    ´mapa´ diferente a las demás, a esta,\
la llamaremos     ´objeto´ que tendrá que tener \
ciertos           ´atributos´ con diferentes ´valores´.")
    
    if input("\n¿Desea la versión interactiva?(si/no)\n>...") in yes: 
        _chk_window(45, 8, True)
    
        pgn = Page(70, 20, "#")
        pgn.create_text("Usando la hoja cuadricula, dibuja un cuadrado usando las casillas    como referencia, luego,\
    anota en horizontal y vertical la cantidad de  casillas que usaste, empezando desde el 0 hasta el \
    máximo que         empleaste, ahora, pintalas, dibuja alguna cosa dentro de todas las   casillas.\
    (le recomendamos solo usar el lápiz para llenar cada           cuadrado, úselo de manera suave para \
    más adelante lo pueda borrar)", "CUSTOM", (1,2))
    
        pgn.create_text("    Cuando lo tengas, presiona el botón *ENTER*, ya que es necesario  para que podemos registrar tu teclado \
    (esto se hace de manera          constantemente), luego, cuando veas un número y un texto seguido a    este, significa \
    que es un ´boton´, y el número, significa el orden    en el que puedes interactuar, es decir, que si \
    ves un total de 4      números seguidos de un texto, significa que solo puedes interactuar   con 4 botones", "CUSTOM", (1, 9))
     
        pgn.create_text(" 1. Continuar", "CUSTOM", (2, 17))

        pgn.get_pre_view()
    

        input("VERIFICADO, PRESIONE *ENTER* POR FAVOR... \n>   ")
        input("Ingrese el número de boton \n>   ")
    
        _chk_window(45, 8, True)
    
        print("¡Muy bien!, ahora que ya entiendes como va la cosa, entonces,              a continuación, ingrese \
    el total de casillas en horizontal y vertical que   usaste, luego, presiona alguna letra del teclado \
    para representar ese      color/dibujo que usaste en tu hoja cuadriculada anteriormente, al final,   colocale \
    algún nombre a tu mapa, yo le coloqué al mío Minecraft.")

        input("\nPresiones *ENTER* para continuar\n>...")
    
        cr_mp(tu=True)

        _chk_window(45, 10, True)
    
        pgn = Page(70, 25, "#")
        pgn.create_text("  Ok, ahora, dibujemos algo con las casillas, ¡vamos a crear una      estructura!, recuerda que las \
    estructuras deben ser cuadradas,        también puede modificarlas y añadirles puertas, pero ese es \
    un tema   más avanzado que puede consultar al final de este tutorial.", "CUSTOM", (1,2))
    
        pgn.create_text("  Regresando a lo nuestro, del mismo modo que dibujaste el mapa,      ahora, dentro de este dibuja \
    algún cuadrado o rectángulo, luego,      nota la posición del primer cuadro que dibujaste, luego \
    haz el       mismo proceso de contar y si quieres, enumerar, cada casilla de la     estructura, tanto en \
    horizontal como en vertical.", "CUSTOM", (1,7))

        pgn.create_text("  Para mayor comodidad, debajo o a un lado del mapa, anota el nombre que quieres que tenga tu \
    estructura, debajo, coloca todos los datos   anteriormente solicitados e incluye si el jugador puede \
    o no           transpasar la estructura.", "CUSTOM", (1, 13))

        pgn.create_text(" Como no es necesario *por el momento*, no hace falta que modifiques el interior de la estructura \
    o coloques puertas, con todo lo anterior es más que suficiente", "CUSTOM", (1, 18))

        pgn.create_text("(si quieres usar las modificaciones, te recomendamos nuestro canal de YouTube para que veas como \
    puedes usarlo)", "CUSTOM", (1, 22))
    
        pgn.get_pre_view()

        input("\nPresiones *ENTER* para continuar\n>...")
    
        cr_st(tu=True)
    
        _chk_window(72, 10, True)

        pgn = Page(70, 23, "#")
        pgn.create_text(" ¿Lo terminaste?, ¡Perfecto!", "CUSTOM", (1,1))
    
        pgn.create_text(" Pues, ahora vamos a crear un objeto, ¿un tener?, ¿plato?,           ¿dólares?, muchas cosas, pero antes, \
    es necesario aclarar que todo en  tu entorno tiene un nombre, y está conformado por atributos que \
    a    su vez tienen valores.","CUSTOM",(1,3))

        pgn.create_text(" Como la computadora que usas, su nombre puede ser ´Laptop´ o ´PC´,   este tiene como principal \
    atributo que es un electrónico y los       valores que podrían tener por ser un eléctrico van \
    desde el precio,    hasta el consumo de batería, que si lo piensas, también el consumo    de batería \
    es otro atributo en sí mismo que tiene un valor, como por  ejemplo que cada 10 minutos, la \
    Laptop disminuye un 1% de batería.", "CUSTOM", (1, 8))    

        pgn.create_text(" Entonces, un objeto, usando el ejemplo anterior, nuestro objeto    debería llamarse ´laptop´, con \
    el atributo ´consumo de bateria´ con el  valor de ´diminuir en 1% cada 10 minutos la bateria´, \
    aunque no       necesariamente tiene que ser solo uno, pueden ser muchos más.", "CUSTOM", (1, 15))    

        pgn.create_text("(recuerda anotar estos datos debajo del mapa para que no te olvides   e ingreses a continuación)", "CUSTOM", (1, 20))
        pgn.get_pre_view()

        input("\nPresiones *ENTER* para continuar\n>...")
        _chk_window(45, 8, True)
    
        cr_ob(tu=True)
    
        _chk_window(45, 8, True)

        pgn = Page(50, 14, "#")
        pgn.create_text("Excelente, vamos a pasar por el momento la      creación de un jugador para el mapa, y saltar directamente al \
    juego.", "CUSTOM", (1,1))   

        pgn.create_text(" Si quieres usar la versión completa de VOP,      debes cerrar esta ventana y volver abrir el     juego, ahora negando\
    el tutorial, puede mandarnos    cualquier duda al correo:                        sco.studio.es@gmail.com o escribir algún mensaje \
      por Twitter, estamos como @ScoStudios, gracias   por elegirnos y ¡disfruta de tu juego!", "CUSTOM", (1, 6))

        pgn.get_pre_view()    


        input("\nPresiones *ENTER* para continuar\n>...")
    else:
        
        ...
    DEV[0] = False
    
    p = Player(CUR[2][0],int(CUR[2][0].vec[0]/2) , int(CUR[2][0].vec[1]/2), "X", [], "", ["w", "s", "a", "d"])
    CUR[2][0].add_node(p)
    
    c = Camera(CUR[2][0], [-5*10, 10*10, -2*15, 5*10])
    CUR[2][0].add_node(c)
    
    btn = Button(1,1,DEFAULT="PLAY")
    btn.execute()

def tot():
    _chk_window()
    pgn = Page(50,20, "#")
    pgn.create_text("VOP: Virtual Object Procces, crea juegos desde 0", "UPPER")
    pgn.create_text("*En el orden que aparece, se recomienda crearlos, principalmente el ´Mapa", "CUSTOM", (1,2))

    btn = Button(10, 4, "1. Mapa", cr_mp)
    btn.cast((""))
    pgn.add_btn(btn)

    btn = Button(10, 5, "2. Estructura", cr_st)
    btn.cast((""))
    pgn.add_btn(btn)

    btn = Button(10, 7, "3. Jugador", cr_pl)
    btn.cast((""))
    pgn.add_btn(btn)

    btn = Button(10, 8, "4. Objeto", cr_ob)
    btn.cast((""))
    pgn.add_btn(btn)

    btn = Button(10, 9, "5. Camara", cr_cm)
    btn.cast((""))
    pgn.add_btn(btn)

    btn = Button(10, 12, DEFAULT="SAVE")
    btn.cast((""))
    pgn.add_btn(btn)

    btn = Button(10, 13, DEFAULT="LOAD")
    btn.cast((""))
    pgn.add_btn(btn)
    
    pgn.create_text("(la UI puede no funcionar, use codigo)", "CUSTOM", (1, 14))

    btn = Button(10, 16, DEFAULT="EXIT")
    btn.cast((""))
    pgn.add_btn(btn)

    pgn.create_text("VERSION: a1.4", "LOWER")
    
    pgn.start_cast()

    
DEV[0] = False

pgn = Page(50, 20, "#")
pgn.create_text("Bievenido a Virtual Object Procces (VOP)", "CUSTOM", (1, 1))
pgn.create_text("Aqui empezará tu experiencia como lo que en un\
    principio era un programador analógico, ten \
      lapíz y papel cuadriculado a la mano antes de\
     empezar.(cuando termines, habrás hecho un juego)", "CUSTOM", (1, 3))

pgn.create_text("Pero ¿Quieres usar el tutorial? (se recomienda \
    si es tu primera vez, lo hagas)", "CUSTOM",(1,8))

btn = Button(2,11, "1. Si", tut)
btn.cast((""))
pgn.add_btn(btn)

btn = Button(2, 12, "2. No", tot)
btn.cast((""))
pgn.add_btn(btn)

pgn.start_cast()


#Recomendado
#set_console_font("Terminal", 4000,20)