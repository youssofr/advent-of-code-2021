import numpy as np

import helpers

 #convert from a binary numpy array to decimal number:
def deci_from_bin(n):
    return np.sum([2**i * n[-1-i] for i in range(n.shape[0])])

# read report and convert to int
report = np.array(helpers.read_input_at_once(__file__, unit = 'char'))
report = report[:, :-1] # a bit of cleaning to get rid of '\n'
report = report.astype(int)

# get most frequent bit by rounding averages over columns
gamma_e = 1/len(report)/2   # an epsilon to add to the average 
                            # as numpy rounds to nearest even value
gamma = (report.mean(axis = 0) + gamma_e).round(decimals = 0).astype(int)

# convert gamma to decimal system
gamma = deci_from_bin(gamma)

# epsilon is the one complement of gamma
epsilon = 2**(report.shape[1]) - 1 - gamma

print(gamma * epsilon)