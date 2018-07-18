## Brownian Motion Plot In Python

### Reference: Python For Data Analysis Code By Wes McKinney

from random import seed
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Set seed for reproducibility:
    
seed(123)

# Brownian Motion is W_t ~ N(0, t) or W_t = Z * \sqrt{t} where Z ~ N(0, 1)
# Reference: https://stackoverflow.com/questions/45021301/geometric-brownian-motion-simulation-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# http://landonjross.io/simulating-brownian-motion-in-python-with-numpy.html
# https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

max_time = 10
num_steps = 100000

dt = max_time / num_steps

# Start BM at 0 (zero drift):
    
position = 0
path = [position]

# Brownian motion has mean of 0 and variance of time (std of sqrt(time)):

for i in range(num_steps):
    increment = np.random.normal(loc = 0, scale = np.sqrt(dt))
    position += increment
    path.append(position)

time_vec = [i * 0.1 for i in range(0, num_steps + 1)]

brownian_df = pd.DataFrame({"Time": time_vec, "Position": path})

plt.plot('Time', 'Position', data = brownian_df)

plt.xlabel("\n Time", size = 14)
plt.ylabel("Position Of Brownian Path \n", size = 14)
plt.title("Brownian Motion Path Plot \n", size = 20) 

plt.show()


### Function Version:
    
def brownian_path(T, N, drift):
    position = drift
    path = [position]
    dt = T / N
    time_vec = [i * 0.1 for i in range(0, num_steps + 1)]
    for i in range(num_steps):
        increment = np.random.normal(loc = 0, scale = np.sqrt(dt))
        position += increment
        path.append(position)
    brownian_df = pd.DataFrame({"Time": time_vec, "Position": path})
    return(brownian_df)



plt.plot('Time', 'Position', data = brownian_path(T = 100, N = 10000, drift = 0))

plt.xlabel("\n Time", size = 14)
plt.ylabel("Position Of Brownian Path \n", size = 14)
plt.title("Brownian Motion Path Plot \n", size = 20) 

plt.show()


