import random

import Kaart_class as cards


class spel:
    def __init__(self):
        self.dek = self.maak_dek()  # Alle kaarten
        self.gedeelde_kaarten = self.eerste_keer_delen(
            self.dek)  # Lijst met de twaalf gedeelde kaarten
        # lijst met lijsten waarin de indexen staan van de sets in gedeelde_kaarten
        self.gevonden_sets = self.alle_sets_vinden(self.gedeelde_kaarten)
        # ALs er Sets in gevonden_Sets zijn dan False anders True zodat er geen punt wordt afgetrokken bij de speler
        self.geen_sets = False


    @staticmethod
    def maak_dek():  # maak alle mogelijke kaarten en returned deze in willekeurige volgorde
        dek = []  # 81 kaarten in een set dek
        for aantal in [-1, 0, 1]:
            for kleur in [-1, 0, 1]:
                for vulling in [-1, 0, 1]:
                    for vorm in [-1, 0, 1]:
                        dek.append(cards.kaart(aantal, kleur, vulling, vorm))
        random.shuffle(dek)  # Dek schudden
        return dek

    @staticmethod
    def eerste_keer_delen(dek):  # Deel twaalf kaarten uit.
        gedeeld = []
        for _ in range(0, 12):
            # verwijder kaarten uit dek en voeg toe aan uitgedeelde kaart
            gedeeld.append(dek.pop())
        return gedeeld

    def set_of_niet(self, first, second, third):  # bepaalt of een set voldoet of niet
        # vergelijk de gezochte vector met vercor van de derde kaart
        return (first + second == third.vector)

    # geeft alle sets uit een verzameling kaarten terug
    def alle_sets_vinden(self, gedeelde_kaarten):
        self.geen_sets = False
        gevonden_sets = []
        aantal_kaarten = len(gedeelde_kaarten)
        for i in range(0, aantal_kaarten-2):
            first = gedeelde_kaarten[i]
            for j in range(i+1, aantal_kaarten-1):
                second = gedeelde_kaarten[j]
                for k in range(j+1, aantal_kaarten):
                    third = gedeelde_kaarten[k]
                    if self.set_of_niet(first, second, third):
                        gevonden_sets.append([i, j, k])
        if not gevonden_sets:  # Als er geen sets in de gedeelde kaarten zit
            gevonden_sets.append([0, 1, 2])
            self.geen_sets = True
        return gevonden_sets

    def set_aanwijzen(self, gekozen_kaarten):  # Zijn de gegeven kaarten een set
        index_eerste, index_tweede, index_derde = [
            kaart for kaart in gekozen_kaarten]
        if [index_eerste, index_tweede, index_derde] in self.gevonden_sets:
            return True
        else:
            return False

    def set_vervangen(self, gekozen_kaarten):
        if len(self.dek) > 3:  # Als er nog nieuwe kaarten zijn
            for index in gekozen_kaarten:
                del self.gedeelde_kaarten[index]
                self.gedeelde_kaarten.insert(index, self.dek.pop())
        else:  # geen kaarten meer in het dek
            for index in gekozen_kaarten:
                del self.gedeelde_kaarten[index]
        self.gevonden_sets = self.alle_sets_vinden(self.gedeelde_kaarten)

    def computer_set(self):  # geeft een willekeurige set terug uit de lijst met gevonden sets
        return self.gevonden_sets[random.randint(0, len(self.gevonden_sets)-1)]
