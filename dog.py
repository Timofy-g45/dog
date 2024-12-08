class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 6

    def feed(self):
        print(f"{self.name} поїв")
        self.hunger += 12
        if self.hunger < 0:
            self.hunger = 0

    def status(self):
        print(f"{self.name} має голод: {self.hunger}")

my_pet = Pet("Барсик")
my_pet.status()
my_pet.feed()
my_pet.status()
