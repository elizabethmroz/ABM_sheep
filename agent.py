import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv









# share with neighbours
# agent will search for close neighbours and share resources with them


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
#environment = []
#rowlist = []

for row in range(len(data)):
    for values in range(len(data)):
        data[values][row]

#rowlist.append(data[values][row])
#environment.append(rowlist)

matplotlib.pyplot.imshow(data)
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
neighbourhood = 20
agents = []


# animation figure
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])
ax.set_autoscale_on(True)



# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(data, agents))
    


carry_on = True    



# Move the agents and they eat the environment

def update(frame_number):
    fig.clear()
    global carry_on

    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share(neighbourhood)
            
    for j in range(num_of_agents):           
        if agents[i].store == 100:
            carry_on = False
            print("stopping condition")
            

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.imshow(data)
        print(agents[i].x, agents[i].y)
        
def gen_function(b = [0]):
    a=0
    global carry_on 
    while (a<10) & (carry_on):
        yield a
        a = a + 1
   

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames = num_of_iterations)  

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