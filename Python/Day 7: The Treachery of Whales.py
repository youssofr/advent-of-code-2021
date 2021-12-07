import numpy as np

import helpers

positions = np.array(helpers.read_input_at_once(__file__, 'int')).squeeze()

positions = np.sort(positions)

med = positions.shape[0]//2

if positions.shape[0] % 2 == 0:
    optimal_pos = positions[med]
else:
    optimal_pos = positions[med] + positions[med+1]
    optimal_pos /= 2

fuel_spent = np.abs(positions - optimal_pos).sum()

print(fuel_spent)