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

def alle_sets_vinden(dek): #geeft alle sets uit een verzameling kaarten terug
    gevonden_sets=[]
    for i in range(0,10): 
        for j in range(i+1,11):
            first = dek[i]
            second = dek[j]
            for k in range(j+1, 12):
                third = dek[k]
                if set_of_niet(first, second, third):
                    gevonden_sets.append([i,j,k])
    return gevonden_sets 

def computer_set(gevonden_sets): # geeft een willekeurige set terug uit de lijst met gevonden sets
    gekozen_set_index = random.randint(0,len(gevonden_sets)-1)
    return gevonden_sets[gekozen_set_index]

def print_gedeeld(gedeeld):# drukt alle kaarten in gedeeld af
    for i in range(0,12):
        print(gedeeld[i])

def eerste_keer_delen(dek):#pakt de laatste twaalf kaarten uit de lijst. 
    gedeeld=[]
    for i in range(0,12):
        gedeeld.append(dek.pop()) #verwijder kaarten uit dek en voeg toe aan uitgedeelde kaart
    return gedeeld

def set_aanwijzen(gedeeld, gekozen_kaarten):
    index_eerste, index_tweede, index_derde = [kaart for kaart in gekozen_kaarten]
    mogelijke_sets = alle_sets_vinden(gedeeld)
    if [index_eerste,index_tweede, index_derde] in mogelijke_sets:
        return True
    else:
        return False
    
def set_vervangen(gedeeld, dek, gekozen_kaarten=[0,1,2]):
    for index in gekozen_kaarten:
        del gedeeld[index]
        gedeeld.insert(index, dek.pop())
    return gedeeld
