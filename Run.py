#!/usr/bin/env python3

import Dek_functies as dek
import Kaart_class as cards
import Display_functies as disp
import time, sys, random, pygame
import time

#setup voor het spel
alle_kaarten = dek.maak_dek()
gedeelde_kaarten = dek.eerste_keer_delen(alle_kaarten)
gevonden_sets = dek.alle_sets_vinden(gedeelde_kaarten)
zwart = (0,0,0) 
rood=(255,0,0)  
# bepaal de breedte (X) en hoogte (Y) van je scherm 
X = 1000
Y = 600
pleky, plekx = disp.locatie_kaarten(X,Y)

gekozen_kaarten = []
punten = 0

def print_scherm():
    nummer = 0
    for y in range(0,4):
        for x in range(0,3):
            display_surface.blit(gedeelde_kaarten[nummer].image, (plekx[x], pleky[y]))
            nummer+=1

pygame.init() 

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('SET')

myFont = pygame.font.SysFont("Impact", 24)
Punten_telling = myFont.render('Aantal punten: ' + str(punten), 1, (255,0,0))
# maak een scherm van grootte X bij Y 
 

  
# geef je scherm een naam
 
start_tijd = int(time.time())

while True : 
    
# vul je scherm zwart
    display_surface.fill(zwart) 

# plak de afbeeldingen van de twaalf kaarten op de locaties die we eerder met de functie locatie_kaarten hebben bepaald
    print_scherm()
    
#puntentelling    
    display_surface.blit(Punten_telling,(50,15))
    
#Tijd bijhouden
    huidige_tijd = time.time()
    tijd_verstreken = 30 - (int(huidige_tijd) - start_tijd)
    

    if tijd_verstreken > 0:
        text = myFont.render(("Tijd: " + str(tijd_verstreken)  +" seconden"), 1, (255,0,0))
        display_surface.blit(text, (plekx[2],15))
        #pygame.display.flip()
    else:
        text = myFont.render("Te laat!", 1, (255,0,0))
        display_surface.blit(text, (plekx[2], 15))
        dek.set_vervangen(gedeelde_kaarten, alle_kaarten)
        gevonden_sets = dek.alle_sets_vinden(alle_kaarten)
        gekozen_kaarten = []

        start_tijd = int(time.time())
        punten -= 1
    #pygame.display.update()

    # Haal alle events op
    for event in pygame.event.get() : 
        positie_muis = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN: #Als er op muis is geklikt
            #haal (x,y) van muis op   
            klik_locatie = disp.waar_geklikt(positie_muis, plekx, pleky)
            if klik_locatie is not "zwart": #als op een kaart geklikt
                if klik_locatie not in gekozen_kaarten:
                    gekozen_kaarten.append(klik_locatie)  
                
                print(gekozen_kaarten)
             
            

            #zodra er drie kaarten zijn gevonden
            if len(gekozen_kaarten) == 3:
                gekozen_kaarten.sort() #sorteer omdat det herkenning werkt met gesorteerde lijst
                
                if dek.set_aanwijzen(gevonden_sets, gekozen_kaarten) is True:
                    dek.set_vervangen(gedeelde_kaarten, alle_kaarten, gekozen_kaarten)
                    gevonden_sets = dek.alle_sets_vinden(alle_kaarten)
                    punten += 1
                
                else:
                    punten -= 1
                #reset de gekozen kaarten naar lege lijst
                gekozen_kaarten = []
             
               
        
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 

            pygame.quit() 
  
            quit() 
  