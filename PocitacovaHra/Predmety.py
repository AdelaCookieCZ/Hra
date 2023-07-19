class Predmet:
    def __init__(self, nazev, cena) -> None:
        self.nazev = nazev
        self.cena = cena

    def __str__(self):
        return f"nazev: {self.nazev}, cena: {self.cena}"
    

class Brneni(Predmet):
    def __init__(self, nazev, cena, obrana) -> None:
        super().__init__(nazev, cena)
        self.obrana = obrana
        
    
class Zbran(Predmet):    
    def __init__(self, nazev, cena, sila) -> None:
        super().__init__(nazev, cena)
        self.sila = sila


class Lektvar(Predmet):
    def __init__(self, nazev, cena, zivot) -> None:
        super().__init__(nazev, cena)
        self.zivot = zivot


class Pecivo(Predmet):
    def __init__(self, nazev, cena, energie) -> None:
        super().__init__(nazev, cena)
        self.energie = energie