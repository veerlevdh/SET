#!/usr/bin/env python3
import Kaart_class as cards
import Dek_class as dek
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

spel_klaar = False
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
blauw = (0,0,255)
geel = (0,255,0)
aantal_keer_gedeeld = []

pygame.init() 

def print_gekozen_kaarten(gekozen_kaarten):
    string_gekozen = ""
    for kaart in gekozen_kaarten:
            string_gekozen = string_gekozen + " " + str(kaart+1)
    aangeklikte_kaarten = myFont.render("Geselecteerde kaarten: "+ string_gekozen, 1, wit)
    display_surface.blit(aangeklikte_kaarten,(50,550))
# maak een scherm van grootte X bij Y 
display_surface = pygame.display.set_mode((X, Y))

# geef je scherm een naam
pygame.display.set_caption('SET')

#initialiseer het font
myFont = pygame.font.SysFont("Impact", 24)
Punten_telling = myFont.render('Aantal punten: ' + str(punten), 1, wit)

#haal huidige tijd op  
start_tijd = int(time.time())


while spel_klaar is False: 
    #update het scherm
    pygame.display.flip()

# Maak de achtergrond zwart

# plak de afbeeldingen van de twaalf kaarten op de locaties die we eerder met de functie locatie_kaarten hebben bepaald
    print_scherm(display_surface, het_spel.gedeelde_kaarten, gekozen_kaarten)
    
#puntentelling  
    Punten_telling = myFont.render('Aantal punten: ' + str(punten), 1, wit)
    display_surface.blit(Punten_telling,(50,15))
    print_gekozen_kaarten(gekozen_kaarten)
#Tijd bijhouden
    if disp.tijd_over(start_tijd)[0] is True:
        text = myFont.render(("Tijd: " + str(disp.tijd_over(start_tijd)[1])  +" seconden"), 1, wit)
        display_surface.blit(text, (plek_x_y[0][2],15))
    else: #computer verwijdert een set
        text = myFont.render("Te laat!", 1, wit)
        display_surface.blit(text, (plek_x_y[0][2], 15))
        het_spel.set_vervangen(het_spel.computer_set())
        aantal_keer_gedeeld.append(1)
        print(len(aantal_keer_gedeeld))
        pygame.mixer.music.load('Fout.wav')
        pygame.mixer.music.play(0)
        gekozen_kaarten = []

        start_tijd = int(time.time())
        punten -= 1
    if len(aantal_keer_gedeeld) == 22:
        spel_klaar = True

    # Haal alle events op
    for event in pygame.event.get() : 
        #Haal (x,y) van muis op  
        positie_muis = pygame.mouse.get_pos() 
        
        if event.type == pygame.MOUSEBUTTONDOWN: #Als er op muis is geklikt 
            klik_locatie = disp.waar_geklikt(positie_muis, plek_x_y)
            if klik_locatie is not False: #als op een kaart geklikt
                if klik_locatie not in gekozen_kaarten:
                    gekozen_kaarten.append(klik_locatie)    
                else:
                    gekozen_kaarten.remove(klik_locatie)

            #zodra er drie kaarten zijn gevonden
            if len(gekozen_kaarten) == 3:
                print(het_spel.gevonden_sets)
                gekozen_kaarten.sort()
                if het_spel.set_aanwijzen(gekozen_kaarten) is True:
                    pygame.mixer.music.load('ding.wav')
                    pygame.mixer.music.play(0)
                    het_spel.set_vervangen(gekozen_kaarten)
                    aantal_keer_gedeeld.append(1)
                    print(len(aantal_keer_gedeeld))
                    print(het_spel.gevonden_sets)
                    start_tijd = int(time.time())
                    punten += 1
                    #BLIJ GELUID
                
                else: #min een punt bij verkeerde set ingeven
                    pygame.mixer.music.load('Fout.wav')
                    pygame.mixer.music.play(0)
                    punten -= 1
                    #STOM GELUID
                #reset de gekozen kaarten naar lege lijst
                gekozen_kaarten = []



        #Spel stoppen met kruisje boven in window 
        if event.type == pygame.QUIT : 
            pygame.quit() 
  
            quit() 

pygame.mixer.music.load('applause.wav')
pygame.mixer.music.play(0)
while spel_klaar is True:

    endFont = pygame.font.SysFont("Javanese Text", 40)
    display_surface.fill(zwart) 
    klaar = endFont.render("Het spel is klaar, je hebt:  "+ str(punten)+" behaald!!!", 1, rood)
    klaar_rect = klaar.get_rect(center=(X/2,Y/2))
    display_surface.blit(klaar, klaar_rect)
    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT : 
            pygame.quit() 
  
            quit()