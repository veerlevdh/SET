import random

import pygame

kleur_dict = {-1:"green",
               0: "red",
               1: "purple"}  

vulling_dict = {-1:"filled",
                 0: "shaded",
                 1: "empty"}
    
vorm_dict = {-1:"diamond",  
              0: "oval",
              1: "squiggle"}
        
aantal_dict = {-1: "1",
                0: "2",
                1: "3"}

class kaart:
    
    def __init__(self, aantal, kleur, vulling, vorm):
        self.aantal = aantal
        self.kleur = kleur
        self.vulling = vulling
        self.vorm = vorm
        self.vector = [aantal, kleur, vulling, vorm]
        #lijst met alle eigenschappen in vector vorm
        
        plaatje =  str(kleur_dict[self.kleur]) + str(vorm_dict[self.vorm]) + str(vulling_dict[self.aantal]) + str(aantal_dict[self.vulling])
        self.image = pygame.image.load("img/" + plaatje + ".png")
    
    def welk(self, eerste, tweede): #welke eigenschap is er nodig om een set te kunnen maken. Let op checkt maar voor een eigenschap
        if eerste + tweede == 2:
            return 1
        if eerste + tweede == 1:
            return -1
        if eerste + tweede == 0:
            return 0 
        if eerste + tweede == -1:
            return 1
        if eerste + tweede == -2:
            return -1
    
    def derde_kaart(self, ander):#als twee kaarten zijn gekozen staat de derde kaart vast. We maken een functie om te bepalen welke dit is.
        return [self.welk(self.aantal,ander.aantal), self.welk(self.kleur,ander.kleur),
                self.welk(self.vulling,ander.vulling), self.welk(self.vorm,ander.vorm)]
                #vector die hieraan voldoet vervolgens in set zoeker kijken of kaart in gedeelde kaarten zit.
    
    def __add__(self, ander):#zelfde functie als boven maar aan te roepen met +
        return self.derde_kaart(ander)
