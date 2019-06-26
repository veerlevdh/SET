import random
import Kaart_class as cards

class spel:
    def __init__(self):
        self.dek = self.maak_dek()
        self.gedeelde_kaarten = self.eerste_keer_delen(self.dek)
        self.gevonden_sets = self.alle_sets_vinden(self.gedeelde_kaarten)
        self.kaartenOver = True
    
    def set_vervangen(self, gekozen_kaarten):
        if len(self.dek) > 3: #Als er nog nieuwe kaarten zijn
            for index in gekozen_kaarten:
                del self.gedeelde_kaarten[index]
                self.gedeelde_kaarten.insert(index, self.dek.pop())
        else: #geen kaarten meer in het dek
            for index in gekozen_kaarten:
                del self.gedeelde_kaarten[index]
        self.gevonden_sets = self.alle_sets_vinden(self.gedeelde_kaarten)
        
    def set_aanwijzen(self, gekozen_kaarten): #Zijn de gegeven kaarten een set
        index_eerste, index_tweede, index_derde = [kaart for kaart in gekozen_kaarten]
        if [index_eerste,index_tweede, index_derde] in self.gevonden_sets:
            return True
        else:
            return False
    
    
    @staticmethod
    def maak_dek(): #maak alle mogelijke kaarten en returned deze in willekeurige volgorde
        dek = [] #81 kaarten in een set dek
        for aantal in [-1,0,1]:
            for kleur in [-1,0,1]:
                for vulling in [-1,0,1]:
                    for vorm in [-1,0,1]:
                        dek.append(cards.kaart(aantal, kleur, vulling, vorm))
        random.shuffle(dek)
        return dek
    
    @staticmethod
    def eerste_keer_delen(dek):#pakt de laatste twaalf kaarten uit de lijst. 
        gedeeld=[]
        for _ in range(0,12):
            gedeeld.append(dek.pop()) #verwijder kaarten uit dek en voeg toe aan uitgedeelde kaart
        return gedeeld
     
    def set_of_niet(self, first, second, third): #bepaalt of een set voldoet of niet
        if first + second == third.vector:
            return True
        else:
            return False
    
    def alle_sets_vinden(self, gedeelde_kaarten): #geeft alle sets uit een verzameling kaarten terug
        gevonden_sets=[]
        aantal_kaarten = len(gedeelde_kaarten)
        for i in range(0,aantal_kaarten-2): 
            for j in range(i+1,aantal_kaarten-1):
                first = gedeelde_kaarten[i]
                second = gedeelde_kaarten[j]
                for k in range(j+1, aantal_kaarten):
                    third = gedeelde_kaarten[k]
                    if self.set_of_niet(first, second, third):
                        gevonden_sets.append([i,j,k])
        if len(gevonden_sets) == 0:
            print("geen set")
            gevonden_sets.append([0,1,2])
        return gevonden_sets 
        
    def computer_set(self): # geeft een willekeurige set terug uit de lijst met gevonden sets
        return self.gevonden_sets[random.randint(0,len(self.gevonden_sets)-1)]
