import numpy as np
from math import ceil, floor
from time import time

import helpers

init_state = np.array(helpers.read_input_at_once(__file__, 'int')).squeeze()

# problem parameters
cycle = 6
dev_period = 2

def tree_solve(state, n):
    # print('Initial State:', *state)
    for i in range(1, n+1):
        # update state (direct translation to problem statment)
        state -= 1
        state = np.append(state, np.repeat(8, np.where(state<0, 1, 0).sum()))
        state = np.where(state<0, cycle, state)
        # print(f'Day {i}:', *state)
    return state.size


def recur_solve(state, n):
    # function to count offspring over a life span period
    def descendants(period):
        # direct descendants of a member over period
        d = int(ceil(period/(cycle+1)))
        # print(period, d)
        # descendants of descendants
        for p in range(period-(cycle + dev_period + 1), 0, -(cycle+1)):
            d += descendants(p)
        return d

    # initial population size
    population = state.size
    # count of lanterns in each state
    states, counts = np.unique(state, return_counts=True)

    # count their offspring
    for s, c in zip(states, counts): 
        population += c * descendants(n - s)

    return population

def numer_solve(state, n):
    pass

observation_period = 150

timer = time()
print(tree_solve(init_state.copy(), observation_period), end='')
print(' in time {}'.format(time()-timer))

timer = time()
print(recur_solve(init_state.copy(), observation_period), end='')
print(' in time {}'.format(time()-timer))
