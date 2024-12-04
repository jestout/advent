import numpy as np
import itertools as it
import operator

ex = r"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# ===================== Part 1 =====================
#%%
def search_direction(arr, pos, vec, match):
    return all(c == arr[*(pos + i * vec)] for i, c in enumerate(match))


def count_valid_directions(arr, pos, match):
    return sum(
        search_direction(arr, pos, np.array(x), match)
        for x in it.product([1, 0, -1], repeat=2)
        if operator.or_(*x)
    )


def prep_input(input):
    inp = np.array([[*l] for l in input.splitlines()])
    inp = np.pad(inp, pad_width=3, mode='constant', constant_values='V')
    return inp


def sol4a(input):
    inp = prep_input(input)
    x_loc = np.where(inp == 'X')
    return sum(count_valid_directions(inp, np.array(x), 'XMAS') for x in zip(*x_loc))


assert sol4a(ex) == 18, 'Part 1: Example wrong'

with open('./2024/inputs/04.txt', 'r') as f:
    ans1 = sol4a(f.read())
    print(ans1)

# ===================== Part 2 =====================
#%%
def valid_x(inp, pos):
    diag1 = set(inp[*(pos + [i, i])] for i in [1, 0, -1])
    diag2 = set(inp[*(pos + [i, -i])] for i in [1, 0, -1])
    return diag1 == {'M', 'A', 'S'} and diag2 == {'M', 'A', 'S'}


def sol4b(input):
    inp = prep_input(input)
    a_loc = np.where(inp == 'A')
    return sum(valid_x(inp, np.array(x)) for x in zip(*a_loc))

assert sol4b(ex) == 9, 'Part 2: Example wrong'


with open('./2024/inputs/04.txt', 'r') as f:
    ans2 = sol4b(f.read())
    print(ans2)

if __name__ == '__main__':
    print(f'{ans1=} {ans2=}')
