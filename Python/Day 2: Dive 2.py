import numpy as np

import helpers

# initialize parameters
direction = {'forward' : np.array([1, 0, 0]),
             'up' : np.array([0, 0, -1]),
             'down' : np.array([0, 0, 1])
            }

location = np.array([0, 0, 0])

# iterate over all input
for input in helpers.read_input_one_by_one(__file__):
    d, x = input.split()
    location += direction[d] * int(x) 
    location[1] += location[2] * (int(x) if d == 'forward' else 0)

print(location[0] * location[1])