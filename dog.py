class Pet:
    def __init__(self, name, species="Арчібальд"):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50

    def eat(self):
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} поїв Голод {self.hunger}.")

    def sleep(self):
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} поспав Енергія {self.energy}.")

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.hunger += 10
            print(f"{self.name} пограв Енергія {self.energy}, Голод: {self.hunger}.")

    def status(self):
        print(f"{self.name} — {self.species}. Голод {self.hunger}, Енергія {self.energy}.")

pet = Pet("Арчібальд", )
pet.status()
pet.eat()
pet.play()
pet.sleep()
pet.status()

print()
