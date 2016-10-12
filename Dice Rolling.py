
leave_program = 0
import random

while leave_program != "q":
    print("This is a Rolling Dice Game")
    print("Press Enter to Roll")
    input()
    number=random.randint(1,6)
    if number==1:
        print("[---------------]")
        print("[               ]")
        print("[       0       ]")
        print("[               ]")
        print("[---------------]")
        leave_program = input()
    if number==2:
        print("[---------------]")
        print("[               ]")
        print("[    0     0    ]")
        print("[               ]")
        print("[---------------]")
        leave_program = input()
    if number==3:
        print("[---------------]")
        print("[       0       ]")
        print("[               ]")
        print("[    0     0    ]")
        print("[---------------]")
        leave_program = input()
    if number==4:
        print("[---------------]")
        print("[    0     0    ]")
        print("[               ]")
        print("[    0     0    ]")
        print("[---------------]")
        leave_program = input()
    if number==5:
        print("[---------------]")
        print("[    0     0    ]")
        print("[       0       ]")
        print("[    0     0    ]")
        print("[---------------]")
        leave_program = input()
    if number==6:
        print("[---------------]")
        print("[    0     0    ]")
        print("[    0     0    ]")
        print("[    0     0    ]")
        print("[---------------]")
        leave_program = input()
    
        
