class animal:
    def __init__(self):
        self.name = "Buddy"
        
    def speak(self):
        print(f"{self.name}makes a sound")
        
class dog(animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
        
    def speak(self):
        super().speak()
        print(f"{self.name} barks, its a {self.breed}")
        
        
Dog = dog("German Shephard")
Dog.speak()
        
        