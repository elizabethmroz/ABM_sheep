import random
import matplotlib.pyplot







# created instance of agent class
class Agent:
    # instance of a class
    # self becomes the argument that is passed in         
    def __init__(self, environment):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
        self.environment = environment
        self.store = 0
    
        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
                
                
        
        
    def eat(self):
        if self.environment[self.y][self.x] >10:
            self.environment[self.y][self.x] -=10
            self.store += 10
                                 
        
        # if asked to print, this is what should be done
    def __str__(self):
        return "id =" + str(self.id) + "x=" + str(self.x) + "y=" + str(self.y) 
    
    