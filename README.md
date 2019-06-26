# Set
Aanschouw onze implementatie van het spel SET.
## Pygame
Voor het spelen van SET is het nodig om Pygame te hebben geïnstalleerd. Dit kan via pip install in de Python console. 
## Spel runnen
Wanneer dit is gebeurd moet in het Anaconda Prompt het bestand Run.py geactiveerd worden. Er komt nu een display tevoorschijn met twaalf kaarten waarin het spel gespeeld kan worden. Zorg ervoor dat je geluid aan staat.
## Hoe werkt het
Links onderin verschijnen de nummers van de kaarten die geselecteerd zijn. Als de kaart al geselecteerd is en er wordt nog een keer op geklikt, dan is de kaart weer gedeselecteerd. De nummering van de kaarten gaat als volgt: nummer 1 is de kaart linksboven, nummer 2 is de middelste kaart van de bovenste rij, nummer 3 is de kaart rechtsboven en zo verder. Rechtsboven loopt een timer (die standaard op 30 seconden staat). De tijd van deze timer kan handmatig in het bestand Run.py veranderd worden om de moeilijkheid van het spel aan te passen. Als er geen set is gevonden binnen de gegeven tijd krijg je een punt aftrek en worden er drie kaarten verwisseld. Als je een set vindt krijg je een punt, wordt de set vervangen voor drie nieuwe kaarten en wordt de tijd weer herstelt naar de begintijd van de timer. Als je drie kaarten selecteert die geen set zijn krijg je ook een punt aftrek. Het aantal punten is rechtsboven te zien. Als de kaarten op zijn stopt het spel en wordt het aantal punten afgedrukt op het scherm.






