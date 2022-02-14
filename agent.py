import random
import operator
import matplotlib.pyplot
import agentframework
import csv





# function for euclidean distance between agents calculation 

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


# making the agents list
num_of_agents = 10
num_of_iterations = 100
agents = []



# attach agent to label so it can be printed
# . means create a new instance of this thing called a
#a = agentframework.Agent(1)
#b = agentframework.Agent(2)
#print(a)
#print(b)

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    agents.append(agentframework.Agent(agentframework.environment))
    
print(agents)


'''
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
'''
# Agents eat
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()        
        
        
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