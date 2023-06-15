import random

class Toddler:
   # -------------------------------------      
   # add any class variables as needed
   # add a vocabulary word that the toddler should know
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.vocabulary = []
    # -------------------------------------      
    # add any functions as to add what our toddler can do!
    def speak(self):
        if not self.vocabulary:
            print("Oops! The toddler hasn't learned any vocabulary yet.")
        else:
            phrase = random.choice(self.vocabulary)
            
    # -------------------------------------        
    # Example 
    # toddler = Toddler("Emma", 2, "Female")
    #toddler.speak()
    def test_fun(self):
        print("hello this is a toddler")
    