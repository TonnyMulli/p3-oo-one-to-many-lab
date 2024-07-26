class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception
        self.pet_type = pet_type
        Pet.all.append(self)

        @property
        def owner(self):
            return self._owner

        @owner.setter
        def owner(self, owner):
            if not isinstance(owner, Owner):
                raise Exception
            self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)