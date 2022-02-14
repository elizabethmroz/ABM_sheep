import random
import matplotlib.pyplot



# reading data
f = open("in.txt")
data = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)
print(data)
f.close()

# making the environment list
environment = []
rowlist = []

for row in range(len(data)):
    for values in range(len(data)):
        data[values][row]
rowlist.append(data[values][row])

environment.append(rowlist)

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# created instance of agent class
class Agent:
    # instance of a class
    # self becomes the argument that is passed in         
    def __init__(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
    def __init__(environment):
        self.environment = environment
        self.store = 0
    
        
        # if asked to print, this is what should be done
    def __str__(self):
        return "id =" + str(self.id) + "x=" + str(self.x) + "y=" + str(self.y) 
    
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
                                     