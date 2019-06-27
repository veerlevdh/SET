#!/usr/bin/env python3

import Kaart_class as cards
import Dek_class as dek
import Display_functies as disp
import time, sys, random, pygame

#Functie om alle kaarten op het scherm af te drukken.
def print_scherm(scherm, gedeelde_kaarten, gekozen_kaarten):
    nummer = 0
    aantal_kaarten = len(gedeelde_kaarten)
    display_surface.fill(zwart) 

    for y in range(0, aantal_kaarten//3):
        for x in range(0, aantal_kaarten//4):
            scherm.blit(gedeelde_kaarten[nummer].image, (plek_x_y[0][x], plek_x_y[1][y]))
            nummer += 1

# bepaal de breedte (X) en hoogte (Y) van je scherm 
X = 900
Y = 600
plek_x_y = disp.locatie_kaarten(X,Y)

#kies kleuren
zwart=(0,0,0)
rood =(255,0,0) 
wit  =(255,255,255)

#start pygame.
pygame.init() 

#Laad de geluiden in.
Ding = pygame.mixer.Sound('Sounds/Ding.wav')
Fout = pygame.mixer.Sound('Sounds/Fout.wav')
Applause = pygame.mixer.Sound('Sounds/Applause.wav')
Game_over = pygame.mixer.Sound('Sounds/Game_over.wav')

#Functie om gekozen kaarten linksonder in beeld aftedrukken.
def print_gekozen_kaarten(gekozen_kaarten):
    string_gekozen = ""
    for kaart in gekozen_kaarten:
            string_gekozen = string_gekozen + " " + str(kaart+1)
    aangeklikte_kaarten = GameFont.render("Geselecteerde kaarten: "+ string_gekozen, 1, wit)
    display_surface.blit(aangeklikte_kaarten,(50,550))
    
#maak een scherm van grootte X bij Y 
display_surface = pygame.display.set_mode((X, Y))

#Geef het window een naam
pygame.display.set_caption('SET')

#initialiseer de Fonts
TitleFont = pygame.font.SysFont("Impact", 80)
GameFont = pygame.font.SysFont("Impact", 24)
Endfont = pygame.font.SysFont("Javanese Text", 40)

#Als SET opstart eerst het menu openen.
Menu = True

#main loop
while True:
    while Menu is True: #Start menu loop.
        pygame.display.flip()
        
        display_surface.fill(zwart) 

        Title = TitleFont.render("S E T", 1, rood)
        Title_rect = Title.get_rect(center=(X/2,Y/3))
        display_surface.blit(Title, Title_rect)

        start_message = GameFont.render("Druk op 1,2 of 3 om moeilijkhiedsgraad te kiezen", 1, wit)
        start_message_rect = start_message.get_rect(center=(X/2,Y/2))
        display_surface.blit(start_message, start_message_rect)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:#Start spel 
                    tijd_moeilijkheid = 30
                    Spel = True
                    Menu = False
                if event.key == pygame.K_2:#Start spel
                    tijd_moeilijkheid = 20
                    Spel = True
                    Menu = False
                if event.key == pygame.K_3:#Start spel
                    tijd_moeilijkheid = 10
                    Spel = True
                    Menu = False

            if event.type == pygame.QUIT: #sluit window
                pygame.quit() 
    
                quit()
        
    #initialiseer alle waarden om een nieuw spel te starten.
    start_tijd = int(time.time())
    het_spel = dek.spel() 
    gekozen_kaarten = []
    punten = 0 
    aantal_keer_gedeeld = []

    while Spel is True: 
        #update het scherm
        pygame.display.flip()
        # plak de afbeeldingen van de twaalf kaarten op de locaties die we eerder met de functie locatie_kaarten hebben bepaald
        print_scherm(display_surface, het_spel.gedeelde_kaarten, gekozen_kaarten)
    
        #puntentelling  

        Punten_telling = GameFont.render('Aantal punten: ' + str(punten), 1, wit) 
        display_surface.blit(Punten_telling,(50,15))
        print_gekozen_kaarten(gekozen_kaarten)
        #Tijd bijhouden
        if disp.tijd_over(start_tijd,tijd_moeilijkheid)[0] is True:
            text = GameFont.render(("Tijd: " + str(disp.tijd_over(start_tijd,tijd_moeilijkheid)[1])  +" seconden"), 1, wit)
            display_surface.blit(text, (plek_x_y[0][2],15))
            
        else: #computer verwijdert een set
            text = GameFont.render("Te laat!", 1, wit)
            display_surface.blit(text, (plek_x_y[0][2], 15))
            het_spel.set_vervangen(het_spel.computer_set())
            aantal_keer_gedeeld.append(1)
            print(len(aantal_keer_gedeeld))
            pygame.mixer.Sound.play(Fout)
            gekozen_kaarten = []

            start_tijd = int(time.time())
            punten -= 1

        if len(aantal_keer_gedeeld) == 22:
            Spel = False
            Einde = True
            #geluid afhankelijk van score
            if punten > 0:
                pygame.mixer.Sound.play(Applause)
            if punten <= 0:
                pygame.mixer.Sound.play(Game_over)

        # Haal alle events op
        for event in pygame.event.get() : 
            #Sla (x,y) van muis op  
            positie_muis = pygame.mouse.get_pos() 
            
            if event.type == pygame.MOUSEBUTTONDOWN: #Als er op muis is geklikt 
                klik_locatie = disp.waar_geklikt(positie_muis, plek_x_y)
                if klik_locatie is not False: #Als op een kaart geklikt
                    if klik_locatie not in gekozen_kaarten:
                        gekozen_kaarten.append(klik_locatie)    
                    else:
                        gekozen_kaarten.remove(klik_locatie)

                #Zodra er drie kaarten zijn gevonden
                if len(gekozen_kaarten) == 3:
                    print(het_spel.gevonden_sets)
                    gekozen_kaarten.sort()
                    if het_spel.set_aanwijzen(gekozen_kaarten) is True:
                        pygame.mixer.Sound.play(Ding) #Geluidje
                    
                        het_spel.set_vervangen(gekozen_kaarten) 
                        aantal_keer_gedeeld.append(1)
                        print(len(aantal_keer_gedeeld))
                        print(het_spel.gevonden_sets)
                        start_tijd = int(time.time())
                        punten += 1
                        
                    else: #min een punt bij verkeerde set ingeven
                        pygame.mixer.Sound.play(Fout)
            
                        punten -= 1
                    
                    #reset de gekozen kaarten naar lege lijst
                    gekozen_kaarten = []



            #Spel stoppen met kruisje boven in window 
            if event.type == pygame.QUIT : 
                pygame.quit() 
    
                quit() 

    while Einde is True:
        pygame.display.flip()
        
        #maak achtergrond zwart
        display_surface.fill(zwart) 

        #druk aantal behaalde punten af in het midden van het scherm
        klaar = Endfont.render("Het spel is klaar, je hebt  "+ str(punten)+" punten behaald!!!", 1, rood)
        klaar_rect = klaar.get_rect(center=(X/2,Y/2))
        display_surface.blit(klaar, klaar_rect)

        #wacht 5 seconden in dit scherm voordat terug naar menu.
        start_tijd - int(time.time())
        if disp.tijd_over(start_tijd,5)[1] == 0:
            Menu = True
            Einde = False

        for event in pygame.event.get(): #Maak window sluitbaar.

            if event.type == pygame.QUIT : 
                pygame.quit() 
    
                quit()