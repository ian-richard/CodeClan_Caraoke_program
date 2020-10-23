class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = [] #this has 3 pets

    def pet_count(self):
        return len(self.pets)
    
    def add_pet(self, pet):
        self.pets.append(pet)
    
    def get_total_value_of_pets(self):
        total = 0
        for pet in self.pets:
            print(self.pets)
            total += pet.price
        return total
    
    def remove_money(self, amount):
        self.cash -= amount
