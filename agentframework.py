import random



# created instance of agent class
class Agent:
    # instance of a class
    # self becomes the argument that is passed in 
    def __init__(self, environment, agent):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.store = 0 
        self.agent = agent
        self.name = str(self.x) + "a" # VERY SIMPLISTIC NAME ASSIGNMENT, FLAWED
        
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
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -=10
            self.store += 10
            
            
    def share(self, neighbourhood):
        for agent in self.agent:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                average = sum/2
                self.store = average
                agent.store = average
                # check agents are sharing
                #print("sharing " + str(dist) + " " + str(average))
                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    
            
''' # if asked to print, this is what should be done
def __str__(self):
return "id =" + str(self.id) + "x=" + str(self.x) + "y=" + str(self.y) '''