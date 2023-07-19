from Obchod import obchod

class Hrdina:
    def __init__(self, jmeno, sila, obrana, zivoty, penize, energie) -> None:
        self.jmeno = jmeno
        self.sila = sila
        self.obrana = obrana
        self.zivoty = zivoty
        self.penize = penize
        self.energie = energie
        self.inventar_predmetu = []

    def __str__(self):
        return f"Hrdina - jmeno: {self.jmeno}, sila: {self.sila}, zivoty: {self.zivoty}, inventar: {self.inventar_predmetu}."    
    

    def pridej_predmet(self, predmet):
        self.inventar_predmetu.append(predmet)
        inventar = []
        for i in self.inventar_predmetu:
            inventar.append(i.nazev)
        print(f'Inventar hrdiny {self.jmeno} po obchodu: {inventar}.') 

                
    def odeber_predmet(self, predmet):
        self.inventar_predmetu.remove(predmet)   

    
    def zaplat(self, cena_zbozi):
        if self.penize < cena_zbozi:
            print("Nedostatek penez: {self.penize}")
        else:
            self.penize = self.penize - cena_zbozi
            print(f'Zustatek penez na uctu po obchodu pro hrace {self.jmeno} je: {self.penize}.')


    def pridej_penize(self, castka):
        self.penize = self.penize + castka