import Kaart_class as cards
import Dek_functies as deks
import random
import pygame

def locatie_kaarten(X,Y):
    X_coordinaten = []
    breedte = (X-100)/3
    for i in range(3):
        X_coordinaten.append(50+int(i*breedte))

    Y_coordinaten = []
    hoogte = (Y-100)/4
    for j in range(4):
        Y_coordinaten.append(50+int(j*hoogte))
    
    return [X_coordinaten, Y_coordinaten] #lijst met coördinaten waar kaarten moeten worden geplaatst.


def tussen(positie_muis, hoekpunten, x_of_y):
    for i in range(len(hoekpunten)):
        if hoekpunten[i] <= positie_muis <= hoekpunten[i]+x_of_y:
            return i
    return 42

def waar_geklikt(positie_muis, plek_x_y):
    
    locatie_dict= {"00":0,"10":1,"20":2,
                   "01":3,"11":4,"21":5,
                   "02":6,"12":7,"22":8,
                   "03":9,"13":10,"23":11,}
    
    x = str(tussen(positie_muis[0], plek_x_y[0], 200))
    y = str(tussen(positie_muis[1], plek_x_y[1], 100))
    if x + y in locatie_dict:
        geklikte_kaart = locatie_dict[x+y]
        return geklikte_kaart
    else:
        return False




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        