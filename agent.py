import random
import operator
import matplotlib.pyplot
import agentframework
import csv


# testing the connection works
a = agentframework.Agent()
print(a.y, a.x)
a.move()
print(a.y, a.x)



# function for euclidean distance
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5



# import data
# reading data
f = open("in.txt")
data = []
for line in f:
    parsed_line = str.split(line, ",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)
print(data)
f.close()

# setting up environment
environment = []
rowlist = []

for row in range(len(data)):
    for values in range(len(data)):
        data[values][row]

rowlist.append(data[values][row])
environment.append(rowlist)

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 

# attach agent to label so it can be printed
# . means create a new instance of this thing called a
#a = agentframework.Agent(1)
#b = agentframework.Agent(2)
#print(a)
#print(b)

# agents list
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    #agents.append([random.randint(0,99),random.randint(0,99)])
    agents.append(agentframework.Agent())
    



# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)


     #   if random.random() < 0.5:
      #      agents[i][0] = (agents[i][0] + 1) % 100
       # else:
        #    agents[i][0] = (agents[i][0] - 1) % 100

        #if random.random() < 0.5:
         #   agents[i][1] = (agents[i][1] + 1) % 100
        #else:
         #   agents[i][1] = (agents[i][1] - 1) % 100


'''
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

'''