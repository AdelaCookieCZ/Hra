def run_game():
    init_game()
    """ 
        tady dostane hráč možnost se pohybovat, podle toho, kde se nachází + jeho energie pohyb()

        pokud hrdina vstoupi do oblasti s neprateli, inicializuje se souboj s neprateli v dane oblasti + po souboji presun predmetu atd.
            pokud souboj dopdne pro hrdinu špatně, return z funkce run_game() -> vypis konecne obrazovky, po stisknuti libovolne klavesy ukonci program.
            pokud dopadne dobre, dostane to hrdina vedet, dostane predmety a vola se fce pohyb()

        pokud hrdina vstoupi do oblasti kde je NPC, dostane možnost obchodovat - fce v obchod/npc, vypisou se npc v oblasti a vypise se inventar npc a hrdina si muze zvolit co si koupi:
                1. kovar
                2. pekar
                3. odejit -> vola fci pohyb()
                
                    __KOVAR__
                    1. nakup 
                    2. prodej -> fce v obchod.py -> hrdina bude moci prodat predmety za penize
                    3. odejit -> vola znovu fci vypis_npc_v_oblasti() ->ta by mohla být v rámci Mapa.py

                        1. zelezne brneni (+5 obrany, 50 penez)
                        2. drevene boty (+2 energie, 20 penez)
                        3. odejit -> vola predchozi menu



    """


def init_game(): #vsechny jsou zpracovany v daném souboru (napr. vytvoreni vsech predmetu probiha ve file Predmety.py - potreba vytvorit fci)
    init_predmety() #vytvori vsechny predmety
    init_npcs()  #vytvori npcs a da jim predmety a umisti je na mapu
    init_nepratele() #vytvori nepratele a da jim predmety a umisti je na mapu
    init_mapa()  #vytvori mapu vc. oblasti
    init_hrdina() # vytvori hrdinu, da mu predmety/statistiky a umisti ho na mapu


def pohyb():
    pass

    """ 
    if oblast je na hornim okraji muzes jit vlevo, vpravo, dolu..., přičemž místo vlevo, vpravo, dolů bude např. Les(20 energie, máš 50 [3 nepratele..]), Vesnice.., Řeka..
    """
