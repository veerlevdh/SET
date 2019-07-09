#!/usr/bin/env python3

import random
import sys
import time

import Spel_class as dek
import Display_functies as disp
import Kaart_class as cards
import pygame


# Functie om alle kaarten op het scherm af te drukken.
def print_scherm(scherm, dek, gekozen_kaarten):
    nummer = 0
    display_surface.fill(zwart)
    for y in range(0, 4):
        for x in range(0, 3):
            scherm.blit(
                dek.gedeelde_kaarten[nummer].image, (plek_x_y[0][x], plek_x_y[1][y]))
            if len(gekozen_kaarten) > 0 and  (y*3)+x == gekozen_kaarten[0] :
                    scherm.blit(
                          dek.gedeelde_kaarten[nummer].image, (plek_x_y[0][x]+10, plek_x_y[1][y]+10))
            if len(gekozen_kaarten)>1 and (y*3)+x == gekozen_kaarten[1]:            
                    scherm.blit(
                          dek.gedeelde_kaarten[nummer].image, (plek_x_y[0][x]+10, plek_x_y[1][y]+10))            
            nummer += 1

def toon(scherm, dek, gekozen_kaarten):
    nummer = 0
    for y in range(0, 4):
        for x in range(0, 3):
            scherm.blit(
                dek.gedeelde_kaarten[nummer].image, (plek_x_y[0][x], plek_x_y[1][y]))
            if (y*3)+x == gekozen_kaarten[0] :
                    scherm.blit(
                          dek.gedeelde_kaarten[nummer].image, (plek_x_y[0][x]+10, plek_x_y[1][y]+10))
            if (y*3)+x == gekozen_kaarten[1]:            
                    scherm.blit(
                          dek.gedeelde_kaarten[nummer].image, (plek_x_y[0][x]+10, plek_x_y[1][y]+10))            
            if (y*3)+x == gekozen_kaarten[2]:            
                    scherm.blit(
                          dek.gedeelde_kaarten[nummer].image, (plek_x_y[0][x]+10, plek_x_y[1][y]+10))            
            nummer += 1
  

# bepaal de breedte (X) en hoogte (Y) van het scherm
X = 900
Y = 600
plek_x_y = disp.locatie_kaarten(X, Y)

# kies kleuren
zwart = (0, 0, 0)
rood = (255, 0, 0)
wit = (255, 255, 255)

# start pygame.
pygame.init()

# Laad de geluiden in.
Ding = pygame.mixer.Sound('Sounds/Ding.wav')
Fout = pygame.mixer.Sound('Sounds/Fout.wav')
Applause = pygame.mixer.Sound('Sounds/Applause.wav')
Game_over = pygame.mixer.Sound('Sounds/Game_over.wav')

# Functie om gekozen kaarten linksonder in beeld aftedrukken.


def print_gekozen_kaarten(gekozen_kaarten):
    string_gekozen = ""
    for kaart in gekozen_kaarten:
        string_gekozen = string_gekozen + " " + str(kaart+1)
    aangeklikte_kaarten = GameFont.render(
        "Geselecteerde kaarten: " + string_gekozen, 1, wit)
    display_surface.blit(aangeklikte_kaarten, (50, 550))


# maak een scherm van grootte X bij Y
display_surface = pygame.display.set_mode((X, Y))

# Geef het window een naam
pygame.display.set_caption('SET')

# initialiseer de Fonts
TitleFont = pygame.font.SysFont("Impact", 200)
GameFont = pygame.font.SysFont("Impact", 24)
Endfont = pygame.font.SysFont("Javanese Text", 40)

# Als SET opstart eerst het menu openen.
Menu = True

# main loop
while True:
    # Start menu loop.
    while Menu:
        pygame.display.flip()

        display_surface.fill(zwart)

        Title = TitleFont.render("S E T", 1, rood)
        Title_rect = Title.get_rect(center=(X/2, Y/4))
        display_surface.blit(Title, Title_rect)

        start_message = GameFont.render(
            "Druk op 1,2 of 3 om moeilijkheidsgraad te kiezen", 1, wit)
        start_message_rect = start_message.get_rect(center=(X/2, Y/2))
        display_surface.blit(start_message, start_message_rect)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Start spel
                    tijd_moeilijkheid = 30
                    Spel = True
                    Menu = False
                if event.key == pygame.K_2:  # Start spel
                    tijd_moeilijkheid = 20
                    Spel = True
                    Menu = False
                if event.key == pygame.K_3:  # Start spel
                    tijd_moeilijkheid = 10
                    Spel = True
                    Menu = False
                if event.key == pygame.K_t:  # Ga naar laatste scherm.
                    tijd_moeilijkheid = 1
                    Spel = False
                    Menu = False
                    Einde = not Menu

            if event.type == pygame.QUIT:  # sluit window
                pygame.quit()

                quit()

    # initialiseer alle waarden om een nieuw spel te starten.
    start_tijd = int(time.time())
    het_spel = dek.spel()
    gekozen_kaarten = []
    punten = 0
    aantal_keer_gedeeld = 0
    
    while Spel:
        # update het scherm
        pygame.display.flip()
        # plak de afbeeldingen van de twaalf kaarten op de locaties die we eerder met de functie locatie_kaarten hebben bepaald
        print_scherm(display_surface, het_spel, gekozen_kaarten)

        # puntentelling

        Punten_telling = GameFont.render(
            'Aantal punten: ' + str(punten), 1, wit)
        display_surface.blit(Punten_telling, (50, 15))
        print_gekozen_kaarten(gekozen_kaarten)
        # Tijd bijhouden
        if disp.tijd_over(start_tijd, tijd_moeilijkheid)[0]:
            text = GameFont.render(
                ("Tijd: " + str(disp.tijd_over(start_tijd, tijd_moeilijkheid)[1]) + " seconden"), 1, wit)
            display_surface.blit(text, (plek_x_y[0][2], 15))

        # computer verwijdert een set
        else:
            pygame.mixer.Sound.play(Fout)

            if not het_spel.geen_sets:
                punten -= 1

            to_show = het_spel.computer_set()
            print_scherm(display_surface, het_spel, [])
            toon(display_surface, het_spel, to_show)
            pygame.display.flip()
            niet_gezien = True
            while niet_gezien:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        niet_gezien = False
            het_spel.set_vervangen(to_show)


            
            aantal_keer_gedeeld += 1
            gekozen_kaarten = []
            start_tijd = int(time.time())

        if aantal_keer_gedeeld == 22:
            Spel = False
            Einde = not Menu
            # geluid afhankelijk van score
            if punten > 0:
                pygame.mixer.Sound.play(Applause)
            if punten <= 0:
                pygame.mixer.Sound.play(Game_over)

        # Haal alle events op
        for event in pygame.event.get():
            # Sla (x,y) van muis op
            positie_muis = pygame.mouse.get_pos()

            # Als er op muis is geklikt
            if event.type == pygame.MOUSEBUTTONDOWN:
                klik_locatie = disp.waar_geklikt(positie_muis, plek_x_y)
                # Als op een kaart is geklikt
                if klik_locatie is not False:
                    if klik_locatie not in gekozen_kaarten:
                        gekozen_kaarten.append(klik_locatie)
                    else:
                        gekozen_kaarten.remove(klik_locatie)

                # Zodra er drie kaarten zijn gevonden
                if len(gekozen_kaarten) == 3:
                    gekozen_kaarten.sort()
                    if het_spel.set_aanwijzen(gekozen_kaarten):
                        pygame.mixer.Sound.play(Ding)  # Geluidje omdat goed

                        het_spel.set_vervangen(gekozen_kaarten)
                        aantal_keer_gedeeld += 1
                        start_tijd = int(time.time())
                        punten += 1

                    else:  # min een punt bij verkeerde set ingeven
                        pygame.mixer.Sound.play(Fout)

                        punten -= 1

                    # reset de gekozen kaarten naar lege lijst
                    gekozen_kaarten = []

            # Spel stoppen met kruisje boven in window
            if event.type == pygame.QUIT:
                pygame.quit()

                quit()

    start_tijd - int(time.time())

    alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letter = 0 
    eerste_tweede_derde_letter = 0
    lettertjes = ['A','A','A']

    while Einde:


        pygame.display.flip()

        # maak achtergrond zwart
        display_surface.fill(zwart)

        lettertjes[eerste_tweede_derde_letter % 3] = alfabet[letter % 26]



        # druk aantal behaalde punten af in het midden van het scherm
        klaar = Endfont.render(
            "Het spel is klaar, je hebt  " + str(punten) + " punten behaald!!!", 1, rood)
        klaar_rect = klaar.get_rect(center=(X/2, Y/2))

        initials = Endfont.render(
            lettertjes[0] + lettertjes[1] + lettertjes[2], 1, wit)
        initials_rect = initials.get_rect(center=(X/2, Y/2+40))

        display_surface.blit(klaar, klaar_rect)
        display_surface.blit(initials, initials_rect)
        


        for event in pygame.event.get():  # Maak window sluitbaar.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Start spel
                    letter += 1
                
                if event.key == pygame.K_DOWN:  # Start spel
                    letter -= 1

                if event.key == pygame.K_RIGHT:  # Start spel
                    eerste_tweede_derde_letter += 1
                    letter = alfabet.index(lettertjes[eerste_tweede_derde_letter%3])
                if event.key == pygame.K_LEFT:  # Ga naar laatste scherm.
                    eerste_tweede_derde_letter -= 1
                    letter = alfabet.index(lettertjes[eerste_tweede_derde_letter%3])
                if event.key == pygame.K_SPACE:  # Ga naar laatste scherm.
                    Menu = True
                    Einde = not Menu
                
            if event.type == pygame.QUIT:
                pygame.quit()

                quit()
