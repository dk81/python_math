# Mean, Median, Mode & Variance In Python Work
# Github User dk81

import math

### Mean Example:

test_ex = [5, 9, 12, 2, 4, 18, 11]

def mean(x):
    return sum(x) / len(x)
    
print("Mean:", round(mean(test_ex), 2))

### Median Code & Example:

def median(x):
    # Input: list of numbers; Output: the "middle" number of an ordered list of #s
    
    sorted_x = sorted(x)
    length_n = len(x)
    
    middle = length_n // 2 # Integer division
    
    # Even numbered amount in list:
    if length_n % 2 == 0:
        median_even = (sorted_x[middle - 1] + sorted_x[middle]) / 2
        return(median_even) # Remember index 0 as 1st element.
    else:
        return(sorted_x[middle]) # Return middle number
        
# Test Cases:

test_ex2 = [5, 1, 4, 2]

print("Median: ", median(test_ex))

print("Median: ", median(test_ex2))


### Mode Example:

# Finding most occuring number/object in a list.

from collections import Counter

# References: https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python
# https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list
# https://stackoverflow.com/questions/16670658/python-variance-of-a-list-of-defined-numbers

test_ex3 = [5, 5, 0, 1, 4, 2, -1, 4, 3, 2, 7, 5]

print(Counter(test_ex3).most_common(1))

# Alternate Way:

from statistics import mode

print("Mode: ",mode(test_ex3))

### Variances

def variance(x):
    n = len(x)
    x_bar = mean(x)
    return(round(sum((x_i - x_bar)**2 for x_i in x) / (n - 1), 2))

test_ex2 = [5, 1, 4, 2]

print("Variance: ", variance(test_ex2)) # 3.33
    
def standard_deviation(x):
    return(math.sqrt(variance(x)))
    
print("Standard Deviation: ", round(standard_deviation(test_ex2), 2))
    
    
