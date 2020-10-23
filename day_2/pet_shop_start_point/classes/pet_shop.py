import pdb
class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name =  name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pets)
    
    def increase_pets_sold(self):
        self.pets_sold += 1
    
    def increase_total_cash(self, amount):
        self.total_cash += amount

    def add_pet(self, new_pet):
        self.pets.append(new_pet)
    
    def remove_pet(self, pet_to_remove):
        self.pets.remove(pet_to_remove)

    def find_pet_by_name(self, name_of_pet):
        #check all pets  in the  list
        #check if their name matches
        #give back a pet object
        for pet in self.pets:
           if pet.name == name_of_pet:
               return pet
               
    def sell_pet_to_customer(self,
    name_of_pet, customer):
    # know  which pet object we  need
    # remove pet from pet 
    #add pet to customer
    #remove money from  customers  wallet
    #add money  to shops till
    #increase number of pets sold  in shop
      pet_to_buy  =  self.find_pet_by_name(name_of_pet)
      self.remove_pet(pet_to_buy)
      customer.add_pet(pet_to_buy)
      self.increase_pets_sold()
      customer.remove_money(pet_to_buy.price)
      self.increase_total_cash(pet_to_buy.price)


    