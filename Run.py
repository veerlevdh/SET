#!/usr/bin/env python3

import Dek_class as dek
import Kaart_class as cards
import Display_functies as disp
import time, sys, random, pygame



    

def print_scherm(scherm, gedeelde_kaarten, gekozen_kaarten):
    nummer = 0
    aantal_kaarten = len(gedeelde_kaarten)

    display_surface.fill(zwart) 
    for y in range(0, aantal_kaarten//3):
        for x in range(0, aantal_kaarten//4):
            scherm.blit(gedeelde_kaarten[nummer].image, (plek_x_y[0][x], plek_x_y[1][y]))
            nummer += 1

#setup voor het spel
het_spel = dek.spel() 
gekozen_kaarten = []
punten = 0 

# bepaal de breedte (X) en hoogte (Y) van je scherm 
X = 1000
Y = 600
plek_x_y = disp.locatie_kaarten(X,Y)
#kies kleuren
zwart=(0,0,0)
rood =(255,0,0) 
wit  =(255,255,255)


pygame.init() 
# maak een scherm van grootte X bij Y 
display_surface = pygame.display.set_mode((X, Y))

# geef je scherm een naam
pygame.display.set_caption('SET')

#initialiseer het font
myFont = pygame.font.SysFont("Impact", 24)
Punten_telling = myFont.render('Aantal punten: ' + str(punten), 1, wit)

#haal huidige tijd op  
start_tijd = int(time.time())


while True: 
    #update het scherm
    pygame.display.flip()

# Maak de achtergrond zwart

# plak de afbeeldingen van de twaalf kaarten op de locaties die we eerder met de functie locatie_kaarten hebben bepaald
    print_scherm(display_surface, het_spel.gedeelde_kaarten, gekozen_kaarten)
    
#puntentelling  
    Punten_telling = myFont.render('Aantal punten: ' + str(punten), 1, wit)
    display_surface.blit(Punten_telling,(50,15))
    
#Tijd bijhouden
    if disp.tijd_over(start_tijd)[0] is True:
        text = myFont.render(("Tijd: " + str(disp.tijd_over(start_tijd)[1])  +" seconden"), 1, wit)
        display_surface.blit(text, (plek_x_y[0][2],15))
    else: #computer verwijdert een set
        text = myFont.render("Te laat!", 1, wit)
        display_surface.blit(text, (plek_x_y[0][2], 15))
        het_spel.set_vervangen(het_spel.computer_set())
        gekozen_kaarten = []

        start_tijd = int(time.time())
        punten -= 1
    

    # Haal alle events op
    for event in pygame.event.get() : 
       
        #Haal (x,y) van muis op  
        positie_muis = pygame.mouse.get_pos() 
        
        if event.type == pygame.MOUSEBUTTONDOWN: #Als er op muis is geklikt 
            klik_locatie = disp.waar_geklikt(positie_muis, plek_x_y)
            if klik_locatie is not False: #als op een kaart geklikt
                if klik_locatie not in gekozen_kaarten:
                    gekozen_kaarten.append(klik_locatie)    
                    print(gekozen_kaarten)
             
            

            #zodra er drie kaarten zijn gevonden
            if len(gekozen_kaarten) == 3:
                print(het_spel.gevonden_sets)
                if het_spel.set_aanwijzen(gekozen_kaarten) is True:
                    het_spel.set_vervangen(gekozen_kaarten)
                    start_tijd = int(time.time())
                    punten += 1
                
                else: #min een punt
                    punten -= 1
                #reset de gekozen kaarten naar lege lijst
                gekozen_kaarten = []
             
        #Spel stoppen met kruisje boven in window 
        if event.type == pygame.QUIT : 
            pygame.quit() 
  
            quit() 
  