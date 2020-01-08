from random import randint

# Function to print the die face each time it rolls
def Dice(value):
   if(value==1):
    print("[---------------]")
    print("[               ]")
    print("[       0       ]")
    print("[               ]")
    print("[---------------]")
    print("\n")
   if(value==2):
    print("[---------------]")
    print("[               ]")
    print("[     0   0     ]")
    print("[               ]")
    print("[---------------]")
    print("\n")
   if(value==3):
    print("[---------------]")
    print("[     0         ]")
    print("[       0       ]")
    print("[         0     ]")
    print("[---------------]")
    print("\n")
   if(value==4):
    print("[---------------]")
    print("[     0   0     ]")
    print("[               ]")
    print("[     0   0     ]")
    print("[---------------]")
    print("\n")
   if(value==5):
    print("[---------------]")
    print("[     0   0     ]")
    print("[       0       ]")
    print("[     0   0     ]")
    print("[---------------]")
    print("\n")
   if(value==6):
    print("[---------------]")
    print("[     0   0     ]")
    print("[     0   0     ]")
    print("[     0   0     ]")
    print("[---------------]")
    print("\n")
    
while(True):
   print("press Enter to roll the dice")
   enter = input()
   value = randint(1, 6)
   Dice(value)
   
   

  