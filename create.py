# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # battery percentage

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.model} charged to {self.battery}%")

    def use(self, hours):
        drain = hours * 10  # battery drains 10% per hour
        self.battery = max(0, self.battery - drain)
        print(f"{self.model} used for {hours} hours. Battery: {self.battery}%")

# Child class with inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game, hours):
        drain = hours * 20  # games drain battery faster
        self.battery = max(0, self.battery - drain)
        print(f"Playing {game} on {self.model} with {self.cooling_system} cooling. Battery: {self.battery}%")

# Testing the classes
phone1 = Smartphone("Samsung", "Galaxy S22", "128GB", 80)
phone1.use(2)
phone1.charge(15)

gaming_phone = GamingPhone("Asus", "ROG Phone 7", "512GB", 100, "Liquid Cooling")
gaming_phone.play_game("PUBG", 3)
gaming_phone.charge(25)



#Polymorphism Challenge
class Vehicle:
    def move(self):
        pass  # abstract-like placeholder

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water!")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

