class human:
    def __init__(self,parent1,parent2):
        self.parent1 = parent1
        self.parent2 = parent2
    
    def birth(self):
        print(f"youre the child of {self.parent1} and {self.parent2}")

class anath_bacha:
    def birth(self):
        print("you're anath")

bacha1 = human("bdshsdsdj","aeuhfsuyfr")
bacha2 = human ("hgdesuuders","ursfdrjd")
bacha3 = human ("hgdesuuders","ursfdrjd")
bacha4 = human ("hgdesuuders","ursfdrjd")
bacha5 = human ("hgdesuuders","ursfdrjd")
bacha6 = human ("hgdesuuders","ursfdrjd")
bacha7 = human ("hgdesuuders","ursfdrjd")
bacha8 = human ("hgdesuuders","ursfdrjd")
bacha9 = human ("hgdesuuders","ursfdrjd")
bacha10 = anath_bacha ()
bacha11 = anath_bacha ()
bacha12 = human ("hgdesuuders","ursfdrjd")


print(bacha1,bacha2,bacha3,bacha4,bacha5,bacha6,bacha7,bacha8,bacha9,bacha10,bacha11,bacha12)

bacha7.birth()
bacha10.birth()