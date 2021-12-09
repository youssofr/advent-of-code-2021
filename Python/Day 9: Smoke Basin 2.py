import numpy as np
import termcolor

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

# get basin bottom list
low_points = np.where(low_points >= 0, 1, 0)
low_positions = np.transpose(np.nonzero(low_points))

def crawl_up(position):
    # a point is by default not a part of a basin
    # it is included only if it has a higher neighbor
    higher_positions = set()

    neighbors_list = [position + [0, 1],
                 position + [0, -1],
                 position + [1, 0],
                 position + [-1, 0]
    ]

    for neighbor in neighbors_list:
        try:
            if  neighbor[0] >= 0 and neighbor[1] >= 0 and\
                hight_map[neighbor[0], neighbor[1]] > hight_map[position[0], position[1]] and\
                hight_map[position[0], position[1]] != 9:
                higher_positions.add(tuple(position)) # included here
                higher_positions = higher_positions.union(crawl_up(neighbor)) # and its neighbor is considered, along with its neighbors
        except IndexError:
            pass
    return higher_positions


basins = set()
locations = set()

for p in low_positions:
    locs = crawl_up(p)
    locations = locations.union(locs)
    basins.add(frozenset(locs))

basin_sizes = sorted(list(map(len, basins)), reverse=True)


for i in range(len(hight_map)):
    for j in range(len(hight_map[i])):
        if (i, j) in locations:
            print(termcolor.colored(hight_map[i, j], 'blue'), end='')
        else:
            print(hight_map[i, j], end='')

    print()

print(helpers.multiply(*basin_sizes[:3]))
