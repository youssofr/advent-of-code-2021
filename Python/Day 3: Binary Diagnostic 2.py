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
o2 = report.copy()
co2 = report.copy()

# get oxygen rating
for i in range(len(o2[0])):
    o2_e = 1/len(o2)/2
    o2_mask = (o2[:, i].mean() + o2_e).round(decimals = 0).astype(int)
    co2_e = 1/len(o2)/2
    co2_mask = (co2[:, i].mean() + co2_e).round(decimals = 0).astype(int)
    if len(o2) != 1:
        o2 = o2[o2[:, i] == o2_mask, :]
    if len(co2) != 1:
        co2 = co2[co2[:, i] != co2_mask, :]
    # print(i, o2_mask, o2, co2_mask, co2, sep='\n')
    if len(o2) == len(co2) == 1:
        break

o2 = o2.squeeze()
co2 = co2.squeeze()

# convert gamma to decimal system
o2 = deci_from_bin(o2)
co2 = deci_from_bin(co2)

print(o2 * co2)