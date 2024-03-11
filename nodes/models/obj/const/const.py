
CUR = [[],  #0    PGN
       [],  #1    CAM
       [],  #2    MAP
       [],  #3    ACTIONS
       [],  #4    DIR SAVES
       
       ]

DEV = [True]

N_ABS = ["pgn",  #0
         "btn",  #1
         "map",  #2
         "stu",  #3
         "obj",  #4
         "cam",  #5
         "pla",  #6
         ]

N_NUM = [0,
         0,
         0,
         0,
         0,
         0,
         0, 
         
         ]

N_WN = [10,     #0  LIM_FP
        0,      #1  FP
        0.15,   #2  TIME_PER_FRAME
        5       #3  TIME_PER_CHECK
        ]  

DEFAULT = [...,              #0    PLAYER
           
                             #1    EXECUTE PROGRAM
           
           [True,            #0    IS MENU
            True,            #1    IS EJECUTE
            False,           #2    IS PAUSE
            0,               #3    ID MAP 
            0                #4    ID CAM
            ],     
                             #2    SIZE PROGRAM
                             
           [True,            #0    AUTO SIZE
            ],
            
           "M"               #3    DFT_DOOR  
            
           ]




