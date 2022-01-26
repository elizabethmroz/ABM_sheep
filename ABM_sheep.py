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
timestep = 5

# for-loop to change y-variable by timestep
for x in range(timestep):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = agents[i][0] + 1
        else: 
            agents[i][0] = agents[i][0] - 1

# for-loop to change x-variable by timestep
for x in range(timestep):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][1] = agents[i][1] + 1
        else: 
            agents[i][1] = agents[i][1] - 1
    print(agents)
            

'''
bounding the environment: 
    if the grid is constrained to 0 - 99, it is currently possible 
    for agents to be able to go ito the negative values or beyond the 99
'''


# print variables
print("starting position of agent 0 is", agents[0][0], ",", agents[0][1])
print("starting position of agent 1 is", agents[1][0], ",", agents[1][1])

# AGENT 0
# TIMESTEP 1
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[0][0] = agents[0][0] + 1
else: 
    agents[0][0] = agents[0][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[0][1] = agents[0][1] + 1
else: 
    agents[0][1] = agents[0][1] - 1
    
#TIMESTEP 2
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[0][0] = agents[0][0] + 1
else: 
    agents[0][0] = agents[0][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[0][1] = agents[0][1] + 1
else: 
    agents[0][1] = agents[0][1] - 1
    
#TIMESTEP 3
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[0][0] = agents[0][0] + 1
else: 
    agents[0][0] = agents[0][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[0][1] = agents[0][1] + 1
else: 
    agents[0][1] = agents[0][1] - 1
    
#TIMESTEP 4
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[0][0] = agents[0][0] + 1
else: 
    agents[0][0] = agents[0][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[0][1] = agents[0][1] + 1
else: 
    agents[0][1] = agents[0][1] - 1
    
#TIMESTEP 5
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[0][0] = agents[0][0] + 1
else: 
    agents[0][0] = agents[0][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[0][1] = agents[0][1] + 1
else: 
    agents[0][1] = agents[0][1] - 1
    
# AGENT 1
#TIMESTEP 1
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[1][0] = agents[1][0] + 1
else: 
    agents[1][0] = agents[1][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[1][1] = agents[1][1] + 1
else: 
    agents[1][1] = agents[1][1] - 1
    
#TIMESTEP 2
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[1][0] = agents[1][0] + 1
else: 
    agents[1][0] = agents[1][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[1][1] = agents[1][1] + 1
else: 
    agents[1][1] = agents[1][1] - 1
    
#TIMESTEP 3
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[1][0] = agents[1][0] + 1
else: 
    agents[1][0] = agents[1][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[1][1] = agents[1][1] + 1
else: 
    agents[1][1] = agents[1][1] - 1
    
#TIMESTEP 4
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[1][0] = agents[1][0] + 1
else: 
    agents[1][0] = agents[1][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[1][1] = agents[1][1] + 1
else: 
    agents[1][1] = agents[1][1] - 1

#TIMESTEP 5
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    agents[1][0] = agents[1][0] + 1
else: 
    agents[1][0] = agents[1][0] - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    agents[1][1] = agents[1][1] + 1
else: 
    agents[1][1] = agents[1][1] - 1

# CHECK
print("after 5 timesteps")
print("agent 0 is", agents[0][0], ",", agents[0][1])
print("agent 1 is", agents[1][0], ",", agents[1][1])


# distance between agents 0 and 1
# pythag = a^2+b^2 = c^2
euclid = ((math.pow((agents[0][1] - agents[1][1]),2)) + (math.pow((agents[0][0]-agents[1][0]),2)))**0.5            
print("agents 0 and 1 are", euclid, "units (euclidean distance) away from each other")

# which agent is furthest east?
print("The coordinates of the agent located furthest east are", max(agents))
print("The coordinates of the agent located furthest north are", max(agents, key=operator.itemgetter(1)))

plt.ylim(0,99)
plt.xlim(0,99)
plt.scatter(agents[0][1],agents[0][0], color='black')
plt.scatter(agents[1][1],agents[1][0], color='black')
m = max(agents, key=operator.itemgetter(1))
plt.scatter(m[1],m[0], color='red')
plt.show()