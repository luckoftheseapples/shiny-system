import random
dice = "Y"
while dice == "Y":

    diceFactor = input("Press Y to roll")

    intDecide = random.randint(1, 6)
    
    if intDecide == 1:
        print("[   ]")
        print("[ 1 ]")
        print("[   ]")
    
    if intDecide == 2:
        print("[2  ]")
        print("[   ]")
        print("[  2]")

    if intDecide == 3:
        print("[3  ]")
        print("[ 3 ]")
        print("[  3]")

    if intDecide == 4:
        print("[4 4]")
        print("[   ]")
        print("[4 4]")

    if intDecide == 5:
        print("[5 5]")
        print("[ 5 ]")
        print("[5 5]")

    if intDecide == 6:
        print("[6 6]")
        print("[6 6]")
        print("[6 6]")
