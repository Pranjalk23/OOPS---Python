#initiate a class
class employee:
    #special method,magic method, dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "Data Scientist"
        
        def travel(self, destination):
            print("Pranjal is travelling to {destination}")
        
        #create an object/instance of class
        Pranjal = employee()
        
        print(self.designation)
        
        Pranjal.travel("Delhi")
        