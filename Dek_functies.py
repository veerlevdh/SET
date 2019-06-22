import random
import Kaart_class as cards

def maak_dek(): #maak alle mogelijke kaarten en returned deze in willekeurige volgorde
    dek = [] #81 kaarten in een set dek
    for aantal in [-1,0,1]:
        for kleur in [-1,0,1]:
            for vulling in [-1,0,1]:
                for vorm in [-1,0,1]:
                    dek.append(cards.kaart(aantal, kleur, vulling, vorm))
    random.shuffle(dek)
    return dek

def set_of_niet(first, second, third): #bepaalt of een set voldoet of niet
    if first + second == third.vector:
        return True
    else:
        return False

def alle_sets_vinden(gedeelde_kaarten): #geeft alle sets uit een verzameling kaarten terug
    gevonden_sets=[]
    aantal_kaarten = len(gedeelde_kaarten)
    for i in range(0,aantal_kaarten-2): 
        for j in range(i+1,aantal_kaarten-1):
            first = gedeelde_kaarten[i]
            second = gedeelde_kaarten[j]
            for k in range(j+1, aantal_kaarten):
                third = gedeelde_kaarten[k]
                if set_of_niet(first, second, third):
                    gevonden_sets.append([i,j,k])
                    print(gevonden_sets)
    if len(gevonden_sets) == 0:
        print("geen set")
        gevonden_sets.append([0,1,2])
    return gevonden_sets 

def computer_set(gevonden_sets): # geeft een willekeurige set terug uit de lijst met gevonden sets
    return gevonden_sets[random.randint(0,len(gevonden_sets)-1)]

def print_gedeeld(gedeeld):# drukt alle kaarten in gedeeld af
    for i in range(0,len(gedeeld)):
        print(gedeeld[i])

def eerste_keer_delen(dek):#pakt de laatste twaalf kaarten uit de lijst. 
    gedeeld=[]
    for _ in range(0,12):
        gedeeld.append(dek.pop()) #verwijder kaarten uit dek en voeg toe aan uitgedeelde kaart
    return gedeeld

def set_aanwijzen(gevonden_sets, gekozen_kaarten): #Zijn de gegeven kaarten een set
    index_eerste, index_tweede, index_derde = [kaart for kaart in gekozen_kaarten]
    if [index_eerste,index_tweede, index_derde] in gevonden_sets:
        return True
    else:
        return False
    
def set_vervangen(gedeeld, dek, gekozen_kaarten):
    if len(dek) > 3: #Als er nog nieuwe kaarten zijn
        for index in gekozen_kaarten:
            del gedeeld[index]
            gedeeld.insert(index, dek.pop())
        return gedeeld
    else: #geen kaarten meer in het dek
        for index in gekozen_kaarten:
            del gedeeld[index]
        return gedeeld
