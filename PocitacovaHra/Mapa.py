import numpy as np

class Mapa:
    def __init__(self,  energie) -> None:
        self.energie = energie

        def __str__(self):
            return f"energie: {self.energie}"
    

class Hory(Mapa):
    def __init__(self, energie) -> None:
        super().__init__( energie)
        

class Les(Mapa):
    def __init__(self,  energie) -> None:
        super().__init__( energie)


class Reka(Mapa):
    def __init__(self,  energie) -> None:
        super().__init__( energie)


class Vesnice(Mapa):
    def __init__(self,  energie) -> None:
        super().__init__( energie)
        self.nabidkaNPC = []

    def pridej_NPC(self, NPC):
        self.nabidkaNPC.append(NPC)


#mapa definovana dopredu 5x5 poli s jasnym rozvrzenim
# R H L L R
# H R V L R
# V R L H H
# L V H R L
# H R L V R

mapa = [
    ["R","H","L","L","R"], 
    ["H","R","V","L","R"],
    ["V","R","L","H","H"],
    ["L","V","H","R","L"],
    ["H","R","L","V","R"]
]

array_object = []

for radek in mapa:
    row = 0
    for index in radek:
        column = 0
        if index == "R":
            array_object.append(Reka(15))
        if index == "H":
            array_object.append(Hory(25))
        if index == "V":
            array_object.append(Vesnice(0))
        if index == "L":
            array_object.append(Les(10))
        column += 1
    row += 1

print(array_object)

for each in array_object:
    print(each.__class__)