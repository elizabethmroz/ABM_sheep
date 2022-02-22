import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework


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
#print(data)
f.close()



for row in range(len(data)):
    for values in range(len(data)):
        data[values][row]


# agents list
num_of_agents = 20
num_of_iterations = 100
neighbourhood = 100
agents = []


# animation figure
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])
#ax.set_autoscale_on(True)



# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(data, agents))
    # CHECKING THAT THE AGENTS STORE IS 0 AT THE START
    #print(agents[i].store)
    #print(agents[i].name)

carry_on = True    



# Move the agents and they eat the environment

def update(frame_number):
    
    fig.clear()
    global carry_on

    for j in range(num_of_iterations):
        #random.shuffle(agents)
        for i in range(num_of_agents):
            print("UNIQUE MOVEMENT")
            #random.shuffle(agents) # not shuffling which moves first, just shuffling the agents in the actual list around so they
            #become different colours / take over from another agent
            agents[i].move()
            print("MOVEWMENT agent #", agents[i].name, "is at:", agents[i].x, agents[i].y)
            agents[i].eat()
            agents[i].share(neighbourhood)
            
        print("\n")
            
            
            
        
    if agents[i].store >= 2501:
        carry_on = False
        
    print("stopping condition")
    for i in range(num_of_agents):
        print(agents[i].store)
                     

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.imshow(data)
        #print("agent #", agents[i].name, "is at:", agents[i].x, agents[i].y)
        #print(agents[i].store)
        
        
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a = a + 1
        
   

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=True, frames = num_of_iterations)  
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)  
matplotlib.pyplot.show()

'''

matplotlib.pyplot.imshow(data)
'''


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
        distance = distance_between(agents_row_a, agents_row_b)'''