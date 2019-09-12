folk0 = 307357870

ar_str = input("Years: ")
ar = int(ar_str)

if(ar < 0):
    print("Invalid input!")

else:     

    #Til að athuga breytingar, þarf að vita sekúndufjöldann, svo auðvelt er að
    #deila. 3600 sekúndur í klst, 24 klst í sólarhring, 365 sólarhringir í ári

    ar_sek = 3600*24*365*ar
    
    #Finnum hversu margir fæðast á gefnum tíma.

    ar_fæd = ar_sek / 7

    #Finnum hversu margir deyja á gefnum tíma

    ar_rip = ar_sek / 13

    #Finnum hversu margir innflytjendur mæta á gefnum tíma

    ar_trump = ar_sek / 35

    #Fæ heildabreytinguna í sér breytu, til að einfalda restina

    ar_breyting = ar_fæd + ar_trump - ar_rip

    folk_lok = int(folk0 + ar_breyting)

    print("New population after", ar, "years is", folk_lok)
