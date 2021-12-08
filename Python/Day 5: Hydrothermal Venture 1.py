import helpers

# read and prepare input
raw_input = helpers.read_input_at_once(__file__)

# split to start and end points
start_to_end = lambda x : x.split(' -> ')
lines = [coord for coord in list(map(start_to_end, raw_input))]

# split start and end points to x and y coordinates
lines = [[line[0].split(','), line[1].split(',')] for line in lines]

# clean y coordinate of end point from '\n' character
for i in range(len(lines)):
    lines[i][1][1] = lines[i][1][1].split('\n')[0]

# problem parameters
clouded_points = {}
count = 0

# walk on a horizontal or vertical line
def walk_over(x, y1, y2, var_dim='1'):
    '''Placeholder docstring'''
    global count
    global clouded_points
    if y2 >= y1:
        start, end = int(y1), int(y2)
    else:
        start, end = int(y2), int(y1)

    for i in range(start, end+1):
        if var_dim == '1':
            t = (x, str(i))
        elif var_dim == '0':
            t = (str(i), x)
        try:
            count += clouded_points[t]
            clouded_points[t] = 0
        except KeyError:
            clouded_points[t] = 1

for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    if x1 == x2:
        walk_over(x1, y1, y2, var_dim='1')
    elif y1 == y2:
        walk_over(y1, x1, x2, var_dim='0')

print(count)