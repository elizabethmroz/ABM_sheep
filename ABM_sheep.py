'''
NAME
    Agent-based model: sheep in a field
    
PURPOSE
    To learn the following: variables, containers, branching and loops, functions,
    classes, I/O, modules, functional/exceptions, GUIS/web
    And to demonstrate the above by creating an agent-based model

PROGRAMMER
    Elizabeth Mroz
    

'''

# imported libraries
import random 
import math
import operator 
import matplotlib.pyplot as plt
import time

# function
def dist_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5


   
    
    
'''
# distance between agents 0 and 1
# pythag = a^2+b^2 = c^2
euclid = ((math.pow((agents[0][1] - agents[1][1]),2)) + (math.pow((agents[0][0]-agents[1][0]),2)))**0.5            
print("agents 0 and 1 are", euclid, "units (euclidean distance) away from each other")

# which agent is furthest east?
print("The coordinates of the agent located furthest east are", max(agents))
print("The coordinates of the agent located furthest north are", max(agents, key=operator.itemgetter(1)))
'''






# number of agents
num_of_agents = 10

# list created for coordinates
agents = []

# timesteps
timestep = 100

# for-loop creating agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    



    
# for-loop to change x- and y-variable by timestep (Torus boundary solution)
for x in range(timestep):
      
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else: 
            agents[i][1] = (agents[i][1] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else: 
            agents[i][0] = (agents[i][0] - 1) % 100
            

plt.ylim(0,99)
plt.xlim(0,99)

for i in range(num_of_agents):
    plt.scatter(agents[i][0],agents[i][1], color='black')

# most eastern point
m_east = max(agents, key=operator.itemgetter(0))
plt.scatter(m_east[0],m_east[1], color='blue')

# most northern point
m_north = max(agents, key=operator.itemgetter(1))
plt.scatter(m_north[0],m_north[1], color='red')
plt.show()

distances_range = []

start = time.clock()

for x in range(num_of_agents):
    for y in range(num_of_agents):
        distances_range.append(dist_between(agents[x],agents[y]))
    
end = time.clock()
print('time = ' + str(end-start))


print(distances_range)

print(max(distances_range))
print(min(distances_range))









      
    
'''
# TESTING SOLID WALL SOLUTION


agents_solid_y = ([99], [0])

for x in range(timestep):
    if random.random() <0.5:
        agents_solid_y[0][0] = (agents_solid_y[0][0] +1)
    else: 
        agents_solid_y[0][0] = (agents_solid_y[0][0] -1)
        
    if random.random() <0.5:
        agents_solid_y[1][0] = (agents_solid_y[1][0] +1)
    else: 
        agents_solid_y[1][0] = (agents_solid_y[1][0] -1)
        
        

    if agents_solid_y[0][0] < 0:
        agents_solid_y[0][0] = 0
        print('bounce!')
    if agents_solid_y[1][0] < 0:
        agents_solid_y[1][0] = 1
        print('bounce!')
    if agents_solid_y [0][0] > 99:
        agents_solid_y[0][0] = 99
        print('bounce!')
    if agents_solid_y [1][0] > 99:
        agents_solid_y[1][0] = 99
        print('bounce!')
    
    
    print(agents_solid_y)
    
'''
        
'''
SOLID WALL SOLUTION        
        
    
# for-loop to change x- and y- variable by timestep (Solid wall/wall bounce solution)
for x in range(timestep):

    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1 )
        else:
            agents[i][1] = (agents[i][1] - 1 )
            
    for i in range (num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1 )
        else:
            agents[i][0] = (agents[i][0] - 1 )
            
    if agents[i][0] < 0:
        agents[i][0] = 0
    if agents[i][1] < 0:
        agents[i][1] = 1
    if agents [i][0] > 99:
        agents[i][0] = 99
    if agents [i][1] > 99:
        agents[i][1] = 99
        
    print(agents)
    
'''




    
''' would be nice if i could get this to output a separate plot for each movement of agent '''








    