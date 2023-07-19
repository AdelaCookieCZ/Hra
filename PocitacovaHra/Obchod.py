def obchod(hrdina, predmet, npc):
    hrdina.zaplat(predmet.cena)
    npc.pridej_penize(predmet.cena)
    npc.odeber_predmet(predmet)
    hrdina.pridej_predmet(predmet)
    print(f'Obchod probehl.')

    
    
