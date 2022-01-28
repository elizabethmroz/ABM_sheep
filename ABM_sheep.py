# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:39:06 2022

@author: gy16e3m
"""
# imported libraries
import random 
import math
import operator 
import matplotlib.pyplot as plt

# number of agents
num_of_agents = 10

# list created for coordinates
agents = []

# for-loop creating agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    

# check
print(agents)
    

# timesteps
timestep = 100

# for-loop to change y-variable by timestep (Torus boundary solution)
for x in range(timestep):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else: 
            agents[i][0] = (agents[i][0] - 1) % 100

# for-loop to change x-variable by timestep (Torus boundary solution)
for x in range(timestep):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else: 
            agents[i][1] = (agents[i][1] - 1) % 100
            
# check
print(agents)


'''
bounding the environment: 
    if the grid is constrained to 0 - 99, it is currently possible 
    for agents to be able to go ito the negative values or beyond the 99
'''



''' COMMENTED OUT FOR NOW 


# distance between agents 0 and 1
# pythag = a^2+b^2 = c^2
euclid = ((math.pow((agents[0][1] - agents[1][1]),2)) + (math.pow((agents[0][0]-agents[1][0]),2)))**0.5            
print("agents 0 and 1 are", euclid, "units (euclidean distance) away from each other")

# which agent is furthest east?
print("The coordinates of the agent located furthest east are", max(agents))
print("The coordinates of the agent located furthest north are", max(agents, key=operator.itemgetter(1)))


''' 

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

    