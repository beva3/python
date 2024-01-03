class Car:
    def __init__(self,color,year):
        self.color  = color
        self.year   = year
    
    def maxSpeed(self):
        if      self.year   < 1990 : max_speed = 150
        elif    self.year   < 2000 : max_speed = 200
        else :max_speed = 250
        
        return max_speed 
    
    def printCar(self):
        print(f"{self.color},{self.year} {self.maxSpeed()}")