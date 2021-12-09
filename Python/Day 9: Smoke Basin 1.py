import numpy as np

import helpers

# read in input and clean from '\n' characters
hight_map = np.array(helpers.read_input_at_once(__file__, 'char'))
hight_map = hight_map[:, :-1].astype(int)

# track the low points 
low_points = hight_map.copy()

# to shift the hight map in each dierction in a loop
map_dim = hight_map.shape

target_indices = [  [0, map_dim[0]-1, 0, map_dim[1]], # up 
                    [1, map_dim[0], 0, map_dim[1]], # down
                    [0, map_dim[0], 1, map_dim[1]], # right
                    [0, map_dim[0], 0, map_dim[1]-1]  # left
]

source_indices = [  [1, map_dim[0], 0, map_dim[1]], # up 
                    [0, map_dim[0]-1, 0, map_dim[1]], # down
                    [0, map_dim[0], 0, map_dim[1]-1], # right
                    [0, map_dim[0], 1, map_dim[1]]  # left
]

# compare each hight value with its neighbors and leave it if it is lower
for t, s in zip(target_indices, source_indices):
                                               # expression for nighbor         # location compared
    low_points[t[0]:t[1],t[2]:t[3]] = np.where(hight_map[s[0]:s[1], s[2]:s[3]] > hight_map[t[0]:t[1],t[2]:t[3]],
                                                 low_points[t[0]:t[1],t[2]:t[3]],
                                                 -1)

answer = low_points.sum() + low_points.size

print(low_points.sum())
print(low_points.size)
print(answer)
