import numpy as np

import helpers

init_state = np.array(helpers.read_input_at_once(__file__, 'int')).squeeze()

def tree_solve(state, n):
    # print('Initial State:', *state)
    for i in range(1, n+1):
        # update state (direct translation to problem statment)
        state -= 1
        state = np.append(state, np.repeat(8, np.where(state<0, 1, 0).sum()))
        state = np.where(state<0, 6, state)
        # print(f'Day {i}:', *state)
    return state.size


print(tree_solve(init_state, 80))