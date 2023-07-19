import Nepritel
import Hrdina
import random
from NPC import vypis_inventare


def __init__souboj(nepritel, hrdina):
        zivoty_hrdina = hrdina.zivoty
        zivoty_nepritel = nepritel.zivoty    
        sila_hrdina = hrdina.sila
        sila_nepritel = nepritel.sila
        obrana_hrdina = hrdina.obrana
        obrana_nepritel = nepritel.obrana
        penize_hrdina = hrdina.penize
        penize_nepritel = nepritel.penize
        predmety_hrdina = hrdina.inventar_predmetu
        predmety_nepritel  = nepritel.inventar_predmetu
        return zivoty_hrdina, zivoty_nepritel, sila_hrdina, sila_nepritel, obrana_hrdina, obrana_nepritel, predmety_hrdina, predmety_nepritel, penize_hrdina, penize_nepritel 


def bitva(nepritel, hrdina):
            # zivoty_hrdina, zivoty_nepritel, penize_nepritel = __init__souboj(nepritel,hrdina)
    utok(nepritel, hrdina)
    if hrdina.zivoty <= 0:
        print(f'Hrdina {hrdina.jmeno} zemrel. Game over.')
    if nepritel.zivoty <= 0:
        hrdina.penize += nepritel.penize
        for x in nepritel.inventar_predmetu:
            hrdina.inventar_predmetu.append(x)
        print(f'Nepritel {nepritel.jmeno} zemrel a byl porazen. Hrdina {hrdina.jmeno} ziskala: {nepritel.penize} penez a {vypis_inventare(nepritel.inventar_predmetu)}.')


def utok(nepritel, hrdina):
    while nepritel.zivoty > 0 and hrdina.zivoty > 0:
        if poradi_utoku():  #if true     
            utok_hrdina(nepritel, hrdina)
            if nepritel.zivoty <= 0:
                break
            utok_nepritel(nepritel, hrdina) #nepritel zautoci hned po hrdinovi, aby se negenerovaly treba jenom 0 bez utoku nepritele
        else:    
            utok_nepritel(nepritel, hrdina)
            if hrdina.zivoty <= 0:
                break
            utok_hrdina(nepritel, hrdina)


def utok_hrdina(nepritel, hrdina):
    # zivoty_nepritel, sila_hrdina, obrana_nepritel = __init__souboj(nepritel,hrdina)
    utok_hrdiny = hrdina.sila - nepritel.obrana
    if utok_hrdiny < 0:
        utok_hrdiny = 0
    print(f'Utok hrdiny: {utok_hrdiny}')
    nepritel.zivoty -= utok_hrdiny
    print(f'Zivoty nepritele: {nepritel.zivoty}')


def utok_nepritel(nepritel, hrdina):
    # zivoty_hrdina, sila_nepritel, obrana_hrdina  = __init__souboj(nepritel,hrdina)
    utok_nepritele = nepritel.sila - hrdina.obrana
    if utok_nepritele < 0:
        utok_nepritele = 0
    print(f'Utok nepritele: {utok_nepritele}')
    hrdina.zivoty -= utok_nepritele
    print(f'Zivoty hrdiny: {hrdina.zivoty}')


def poradi_utoku():
    return random.randint(0,1)