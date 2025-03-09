class animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name}makes a sound")
        
class Dog(animal):
    
    def speak(self):
        print(f"{self.name} barks")
        
        
        
Animal = animal("Buddy")
Animal.speak()
        
        
dog = Dog("Leo")
dog.speak()