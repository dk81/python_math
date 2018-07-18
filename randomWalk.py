## Random Walks Plot In Python
## dk81 User in Github

### Main Reference: Python For Data Analysis Code By Wes McKinney
### But book does not contain code for plotting the random walks
### I have included some matplotlib code for plotting random walks.


import random
from random import seed
from matplotlib import pyplot as plt
import numpy as np

# Set seed for reproducibility
seed(123)

position = 0 #Starting position of random walk (drift)
walk = [position]
steps = 1000

for i in range(steps):
    step = 1 if random.randint(0, 1) == 1 else -1
    position += step
    walk.append(position)
    
# Plot results

plt.plot(walk)

plt.xlabel("\n Number Of Steps", size = 14)
plt.ylabel("Position \n", size = 14)
plt.title("Random Walk Plot \n", size = 20) 

plt.show()


# Basic statistics on random walk:
    
print(np.min(walk))

print(np.max(walk))

print(np.mean(walk))

print(np.std(walk))


# -------------------------------

### Multiple Random Walks

# -------------------------------

nwalks = 200
nsteps = 100

draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws == 1, 1, -1) #If draw == 1 then 1, if draw != 1 step is 0.
walks = steps.cumsum(1) #Add steps

# Plot results

plt.plot(walks)

plt.xlabel("\n Time", size = 14)
plt.ylabel("Position \n", size = 14)
plt.title("Multiple Random Walks Plot \n", size = 20) 

plt.show()

# Basic statistics on multiple random walks:
    
print(np.min(walks))

print(np.max(walks))

print(np.mean(walks))

print(np.std(walks))