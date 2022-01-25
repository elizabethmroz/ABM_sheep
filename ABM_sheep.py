# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:39:06 2022

@author: gy16e3m
"""
# imported libraries
import random 
import math

# xy starting variables
y0 = random.randint(0, 100) 
x0 = random.randint(0,100)

# print variables
print("starting position of agents is", y0, ",", x0)

# TIMESTEP 1
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y0 = y0 + 1
else: 
    y0 = y0 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1
    
#TIMESTEP 2
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y0 = y0 + 1
else: 
    y0 = y0 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1
    
#TIMESTEP 3
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y0 = y0 + 1
else: 
    y0 = y0 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1
    
#TIMESTEP 4
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y0 = y0 + 1
else: 
    y0 = y0 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1
    
#TIMESTEP 5
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y0 = y0 + 1
else: 
    y0 = y0 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1
    
# check
print("agent 0 is", y0, ",", x0)


# xy starting variables
y1 = random.randint(0,100) 
x1 = random.randint(0,100)

#TIMESTEP 1
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y1 = y1 + 1
else: 
    y1 = y1 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1
    
#TIMESTEP 2
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y1 = y1 + 1
else: 
    y1 = y1 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1
    
#TIMESTEP 3
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y1 = y1 + 1
else: 
    y1 = y1 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1
    
#TIMESTEP 4
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y1 = y1 + 1
else: 
    y1 = y1 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1

#TIMESTEP 5
# alter y randomly by +-1 (sheep walk one step)
if random.random() <0.5:
    y1 = y1 + 1
else: 
    y1 = y1 - 1
    
# alter x randomly by +-1
if random.random() <0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1

# CHECK
print("after 5 timesteps")
print("agent 1 is", y1, ",", x1)


# distance between agents 0 and 1
# pythag = a^2+b^2 = c^2

euclid = ((math.pow((x0 - x1),2)) + (math.pow((y0-y1),2)))**0.5            
print(euclid)