def vyhodnot (retezec_piskvorky):
    "Vyhodnocení hry 1-D piškvorky pomocí řetězce."
    if "xxx" in retezec_piskvorky:
        return "x"
    elif "ooo" in retezec_piskvorky:
        return "o"
    elif "-" not in retezec_piskvorky:
        return "!"
    else:
        return "-"

v = vyhodnot ("xooxxoooxooxxoxoxxoo")
if v == "x":
    print ("Vyhrál hráč s křížky.")
elif v == "o":
    print ("Vyhrál hráč s kolečky.")
elif v != "-":
    print ("Remíza.")
else:
    print ("Hra ještě neskončila.")
