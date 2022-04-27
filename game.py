from this import d


class Unit:
    def __init__(self, n, d, h) -> None:
        self.damage = d
        self.health = h
        self.name = n
    def attack(self, unit):
        print(self.name, "attack", unit.name, "by", self.damage)
        unit.health -= self.damage


elf = Unit("Elf",5,100)
ork = Unit("Ork",3,90)
elf.attack(ork)
ork.attack(elf)
print(elf.name,"health", elf.health)
print(ork.name,"health", ork.health)