class NPC:
    def __init__(self, jmeno_NPC) -> None:
        self.jmeno_NPC = jmeno_NPC
        self.inventar = []
        self.penize = 0

    def nabidka(self): #vypisuje to, co ma NPC v inventari, nemusim specifikovat parametr inventar, podiva se sam do sebe
        inventar = []
        for i in self.inventar:
            inventar.append(i.nazev)
        print(f'{self.jmeno_NPC} vlastni tyto predmety: {inventar}.')   #rozsirit print, aby neprintoval objekty, ale nazvy

    
    def stav_penez(self):
        print(f'Stav penez NPC {self.jmeno_NPC} je: {self.penize}.')

    def pridej_penize(self, castka):
        self.penize = self.penize + castka
        print(f'{self.jmeno_NPC} vydelal {castka}, novy zustatek po obchode je: {self.penize}.')


    def nabidka_predmetu(self, predmet): #pridava predmet do NPC
        self.inventar.append(predmet)


    def odeber_predmet(self, predmet):
        self.inventar.remove(predmet)


class Kovar(NPC):
    def __init__(self, jmeno_NPC) -> None:
        super().__init__(jmeno_NPC)   


class Obchodnik(NPC):
    def __init__(self, jmeno_NPC) -> None:
        super().__init__(jmeno_NPC)
   
        
class Pekar(NPC):
    def __init__(self, jmeno_NPC) -> None:
        super().__init__(jmeno_NPC)
        

    
def vypis_inventare(inventar_predmetu):
        inventar = []
        for i in inventar_predmetu:
            inventar.append(i.nazev)
        return inventar