import jul_stat as js
import jul_ev as jev

counter = 1
while counter == 1:
    print ("\n[1] Stat Calculator")
    print ("[2] EV Calculator")
    n0 = int(input("Choose number: "))

    bs = int(input("\nBase Status: "))
    lvl = int(input("Level: "))
    iv = int(input("EVHP: "))
    ev = int(input("IVHP: "))
    stat = int(input("Desire increase in stat: "))

    if n0 == 1:
        print ("\nHP = ", js.jairah.hpcal(bs,iv,ev,lvl))
        print ("Attack = ", js.jairah.otherstat(bs,iv,ev,lvl))
        print ("Defend = ", js.jairah.otherstat(bs,iv,ev,lvl))
        print ("SP. Attack = ", js.jairah.otherstat(bs,iv,ev,lvl))
        print ("SP. Defend = ", js.jairah.otherstat(bs,iv,ev,lvl))
        print ("Speed = ", js.jairah.otherstat(bs,iv,ev,lvl))
        print ("\nThe needed EVs to increase stat is ", jev.lopez.evneed(stat,bs,iv,ev,lvl))

    elif n0 == 1:
        print ("\n[1]Single Stat")
        print ("[2]All Stat")
        n1 = int(input("Choose number: "))

        if n1 == 1:
            print ("\n[1] Attack")
            print ("[2] Defend")
            print ("[3] SP. Attack")
            print ("[4] SP. Defend")
            print ("[5] Speed")
            print ("[6] HP")
            n20 = int(input("Choose stat: "))

            if n20 == 1 or 2 or 3 or 4 or 5:
                print ("\nThe stat is: ", js.jairah.otherstat(bs,iv,ev,lvl))
            elif n20 == 6:
                print ("\nHP = ", js.jairah.hpcal(bs,iv,ev,lvl))

        elif n1 == 2:
            print ("\nHP = ", js.jairah.hpcal(bs,iv,ev,lvl))
            print ("Attack = ", js.jairah.otherstat(bs,iv,ev,lvl))
            print ("Defend = ", js.jairah.otherstat(bs,iv,ev,lvl))
            print ("SP. Attack = ", js.jairah.otherstat(bs,iv,ev,lvl))
            print ("SP. Defend = ", js.jairah.otherstat(bs,iv,ev,lvl))
            print ("Speed = ", js.jairah.otherstat(bs,iv,ev,lvl))
    
    print ("\n[1] Perform another calculation")
    print ("[2] End the program")
    n3 = int(input("Choose a number: "))
    if n3 == 2:
        break
    elif n3 == 1:
        continue