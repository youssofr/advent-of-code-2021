import helpers

# get input
raw_input = helpers.read_input_at_once(__file__)

# initialize parameters 
stride = 3
count = 0

# initialize depths with first window
depths = []
for i in range(stride):
    depths.append(int(raw_input[i]))
# getting first sum
aggregate_depth = sum(depths)

# looping over the rest
for i in range(stride, len(raw_input)):
    # get the new reading 
    depths[i%stride] = int(raw_input[i])
    
    # compare current window with previous one
    if sum(depths) > aggregate_depth:
        count += 1
    
    # update depth
    aggregate_depth = sum(depths)

print(count)
