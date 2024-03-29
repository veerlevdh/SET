import Kaart_class as cards
import Dek_functies as deks
import random
import pygame

def locatie_kaarten(X,Y):
    Y_coordinaten = []
    hoogte = (Y-100)/4
    X_coordinaten = []
    breedte = (X-100)/3
    for i in range(3):
        X_coordinaten.append(50+int(i*breedte))
    for j in range(4):
        Y_coordinaten.append(50+int(j*hoogte))
    return Y_coordinaten, X_coordinaten #lijst met coördinaten waar kaarten moeten worden geplaatst.


def tussen(positie_muis, hoekpunten, x_of_y):
    for i in range(len(hoekpunten)):
        if hoekpunten[i]<=positie_muis<=hoekpunten[i]+x_of_y:
            return i
    return 42

def waar_geklikt(positie_muis, plekx, pleky):
    
    locatie_dict= {"00":0,"10":1,"20":2,
                   "01":3,"11":4,"21":5,
                   "02":6,"12":7,"22":8,
                   "03":9,"13":10,"23":11,}
    
    x = str(tussen(positie_muis[0], plekx, 200))
    y = str(tussen(positie_muis[1], pleky, 100))
    if x+y in locatie_dict:
        geklikte_kaart = locatie_dict[x+y]
        return geklikte_kaart
    else:
        return "zwart"

def print_gedeelde_kaarten(gedeelde_kaarten, plekx, pleky):
    nummer = 0
    for y in range(0,4):
        for x in range(0,3):
            display_surface.blit(gedeelde_kaarten[nummer].image, (plekx[x], pleky[y]))
            nummer+=1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        