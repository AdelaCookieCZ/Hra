class Nepritel:
    def __init__(self, jmeno, sila, obrana, zivoty, penize) -> None:
        self.jmeno = jmeno
        self.sila = sila
        self.obrana = obrana
        self.zivoty = zivoty
        self.penize = penize
        self.inventar_predmetu = []

    def __str__(self):
        return f"Nepritel - jmeno: {self.jmeno}, sila: {self.sila}, zivoty: {self.zivoty}. "  