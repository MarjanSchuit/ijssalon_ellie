from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs - (prijs * korting)
    return [smaak, prijs, korting]

uitkomst_aanbieding = aanbieding_1('aardbei', 4, 0.1)
print (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {uitkomst_aanbieding[0]},van {uitkomst_aanbieding[1]} euro voor {"%.2f" % uitkomst_aanbieding[2]} euro.")


def inkomsten_totaal(inkomsten):
    inkomsten = (sum(inkomsten))
    BTW = int (inkomsten * 0.09)
    return [inkomsten, BTW]
    
uitkomst_inkomsten_totaal = inkomsten_totaal([220, 430, 125, 160, 205, 90, 345])
print (f"Het totaal van alle inkomsten van deze week is {uitkomst_inkomsten_totaal[0]} euro, waarover {uitkomst_inkomsten_totaal[1]} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    min_getal = min(mijn_lijst)
    max_getal = max(mijn_lijst)
    return [min_getal, max_getal]

uitkomst = laag_en_hoog([220, 430, 125, 160, 205, 90, 345])
print (uitkomst)

def gemiddelde(mijn_lijst):
    mijn_lijst = (sum(mijn_lijst)/len(mijn_lijst))
    return mijn_lijst

uitkomst_gemiddelde = gemiddelde([220, 430, 125, 160, 205, 90, 345])
print (f"De gemiddelde inkomsten deze week zijn {"%.2f" % uitkomst_gemiddelde} euro.")

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

uitkomst_meervoudig = meervoudig([10,5,3,2,1,2,9])
print(uitkomst_meervoudig)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer 

uitkomst_combi = combinatie([2,6,9])
print (uitkomst_combi)