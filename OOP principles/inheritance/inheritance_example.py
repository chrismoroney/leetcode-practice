# Example explained:
# In our example, the Dog class inherits from Animal, 
# taking advantage of the general properties all animals share (name, species, making sounds). 
# The Dog class adds specific behaviors (like the "Woof!" sound) while leveraging the foundation provided by Animal. 
# This reflects the natural relationship that a dog is an animal with additional specialized characteristics.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Some generic animal sound")
        
    def info(self):
        return f"{self.name} is a {self.species}"

# Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class's __init__ method
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Woof!")
        
    def info(self):
        return f"{super().info()} of breed {self.breed}"

# Create a Dog object
buddy = Dog("Buddy", "Golden Retriever")
print(buddy.info())  # Buddy is a Dog of breed Golden Retriever
buddy.make_sound()  # Woof!