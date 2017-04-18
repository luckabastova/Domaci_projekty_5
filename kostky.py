from random import randrange

pocet_hodu_max = (0,0)
for hrac in range (1,5):
    print("Hody hráče {}:".format(hrac))
    pocet_hodu = 0
    while True:
        pocet_hodu += 1
        hod_kostkou = randrange (1,7)
        print("{}, ".format(hod_kostkou), end = "")
        if hod_kostkou==6:
            if pocet_hodu>pocet_hodu_max[0]:
                pocet_hodu_max = (pocet_hodu, hrac)
            print()
            break

print("Vyhrál hráč {} s počtem hodů {}.".format(pocet_hodu_max[1], pocet_hodu_max[0]))
