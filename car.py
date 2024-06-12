class Car:
    def __init__(self,make,model,year,color): # construter
        self.make =make    #atributs called 
        self.model=model 
        self.year=year
        self.color=color

  

   #method called
    def drive (self):
        print("This" +self.model + "car is driving")

    def stop(self):
        print("The car "+ self.model+ "is driving")