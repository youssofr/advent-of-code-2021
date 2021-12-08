import numpy as np

import helpers

positions = np.array([16,1,2,0,4,2,7,1,2,14])#helpers.read_input_at_once(__file__, 'int')).squeeze()

# sort positions
positions = np.sort(positions)
# index of median element
med = positions.shape[0]//2


def part_1():
    # get median (that's the optimal position)
    if positions.shape[0] % 2 == 0:
        optimal_pos = positions[med]
    else:
        optimal_pos = positions[med] + positions[med+1]
        optimal_pos /= 2

    fuel_spent = np.abs(positions - optimal_pos).sum()

    return fuel_spent

def part_2():
    
    mean = positions.mean().astype(int)
    optimal_pos = mean
    error = np.sign(positions - optimal_pos).mean() // 2
    
    while optimal_pos != mean + error:
        print(error)
        optimal_pos += error.round(0).astype(int)
        error = np.sign(positions - optimal_pos).mean() // 2
    
    print(optimal_pos)
    steps = np.abs(positions - optimal_pos)
    fuel_spent = ((steps * (steps + 1)).sum()) / 2

    return fuel_spent

print(part_2())

