import numpy as np

import helpers

# read report and convert to int
report = np.array(helpers.read_input_at_once(__file__, unit = 'char'))
report = report[:, :-1] # a bit of cleaning to get rid of '\n'
report = report.astype(int)

# get most frequent bit by rounding averages over columns
gamma = report.mean(axis = 0).round(decimals = 0).astype(int)

# convert gamma to decimal system
gamma = np.sum([2**i * gamma[-1-i] for i in range(gamma.shape[0])])

# epsilon is the one complement of gamma
epsilon = 2**(report.shape[1]) - 1 - gamma

print(gamma * epsilon)