from .admin_dir import *

from os import getcwd, chdir, listdir, path, remove

cwd = getcwd()

def _check_save():
    """
    Verifica la ubicación de la carpeta "saves"
    """
    if getcwd() == f"{cwd}\saves":
        return True
    else:
        for pat in list(filter(path.isdir, listdir())):
            if pat == "saves":
                chdir(r"./saves")
                return True
        print("CURRENT: " + getcwd())
        chdir("..")
        _check_save()
        
                
def refresh_saves(CUR) -> list:
    CUR[4] = list(filter(path.isfile, listdir()))
    return CUR[4]

def start_test():
    _check_save()
    if getcwd()[-5:-1] == "save":
        n = save_node({"Test": True}, "test")

        try:
            if load_save(n)["Test"]:
                remove(n)
                print("PASSED")
                return True
        except KeyError:
            print("NOT CREATE \nTRY AGAIN...")
            start_test()
    else:
        print("NOT FOUND")
        _check_save()
        print("TRY AGAIN...")
        start_test()
        
