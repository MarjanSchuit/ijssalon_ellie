from helper import *


def presenteer(dict):
    uitvoer = ['']
    for key, value in dict.items():
        regel = f"{key} : {value} euro"
        print (regel)
        uitvoer = onderstreep(regel)
    print (uitvoer[1])  
    totaal = som(dict)
    print(f"totaal : {totaal} euro")


