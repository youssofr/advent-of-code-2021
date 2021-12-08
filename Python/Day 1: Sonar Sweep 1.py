# initialize variables
last_depth = 0
count = 0

# read input from file
with open('../Inputs/Day 1: Sonar Sweep.txt', 'r') as f:
    
    # initialize with first input
    last_depth = int(f.readline())
    
    # iterate over all others
    for i, line in enumerate(f.readlines(), 1):
        depth = int(line)

        # increase count if condition met
        if depth > last_depth:
            count += 1
        
        # update
        last_depth = depth

print(count)