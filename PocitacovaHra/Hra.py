import Predmety
import Hrdina as h
import NPC as n
import Nepritel as ne
import Mapa
import Obchod as o
import Souboj as s

brneni1 = Predmety.Brneni("zelezne brneni", 100, 10)
brneni2 = Predmety.Brneni("drevene brneni", 50, 2)
hrdina1 = h.Hrdina("Adela", 80, 15, 200, 100, 80)
npc1 = n.NPC("Pepa")
nepritel1 = ne.Nepritel('Adam',20,15,10,100)

npc1.nabidka_predmetu(brneni1)          #pridavam predmet pouze danemu NPC
npc1.nabidka_predmetu(brneni2)


# print(brneni1)
# print(f'Inventar hrdiny {hrdina1.jmeno} pred obchodem: {hrdina1.inventar_predmetu}')
# o.obchod(hrdina1, brneni2, npc1)
# print(f'Inventar hrdiny {hrdina1.jmeno} po obchodu: {hrdina1.inventar_predmetu}')
# print(npc1.penize)
# print(hrdina1.penize)
# npc1.nabidka()
# print(hrdina1)
# npc1.stav_penez()
# nepritel1.inventar_predmetu = [brneni2]
# s.bitva(nepritel1,hrdina1)


def pricti_deset(x):
    return x + 10

cisla = [1,2,3,4]

vysledek = map(pricti_deset,cisla)
print(list(vysledek))