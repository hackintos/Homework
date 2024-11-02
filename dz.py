class Pet:
    def __init__(self, name, type_pet="котик"):
        self.name = name
        self.type_pet = type_pet  
        self.hunger = 50  
        self.energy = 50  

    def feed(self):
        if self.hunger > 20:
            self.hunger -= 20
            print(f"{self.name} тепер не такий голодний!")
        else:
            print(f"{self.name} не хоче їсти зараз...")

    def play(self):
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} радісно грає!")
        else:
            print(f"{self.name} занадто втомився для ігор...")

    def sleep(self):
        if self.energy < 80:
            self.energy += 30
            print(f"{self.name} солодко спить и набираєтся сил!")
        else:
            print(f"{self.name} не хоче спати зараз.")

    def status(self):
        print(f"Це {self.name} - {self.type_pet}")
        print(f"Голод: {self.hunger}/100")
        print(f"Енергія: {self.energy}/100")
        print("-----")


my_pet = Pet("Бруно", "котик")
for pet in range(5):
 my_pet.status()
 my_pet.feed()
 my_pet.play()
 my_pet.sleep()
 my_pet.status()
