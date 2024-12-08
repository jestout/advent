from collections import defaultdict
from itertools import combinations
import string

ex = r"""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def process_input(s: str):
    city = set()
    freqs = defaultdict(set)

    for x, l in enumerate(s.splitlines()):
        for y, c in enumerate(l):
            pos = x + y * 1j
            if c not in string.punctuation:
                freqs[c].add(pos)
            city.add(pos)

    return city, freqs

def find_antinodes(city, freqs):
    antinodes = set()
    for freq, locs in freqs.items():
        for f1, f2 in combinations(locs, 2): # Want to iterate over all pairs
            # Find the displacement vector between them
            df = f1 - f2
            potential_anodes = (f1 + df, f2 - df) # f2 - (f1 + df) = f2 - f1 + f2 - f1 = 2 df
            antinodes = antinodes | {a for a in potential_anodes if a in city}

    return antinodes

def anode_plot(s: str):
    city, freqs = process_input(s)
    antinodes = find_antinodes(city, freqs)

    city_map = [[*l] for l in s.splitlines()]

    for a in antinodes:
        city_map[int(a.real)][int(a.imag)] = '#'

    return '\n'.join(''.join(l) for l in city_map)

#%%
assert len(find_antinodes(*process_input(ex))) == 14, "Part 1: Example wrong"


with open('./2024/inputs/08.txt', 'r') as f:
    full = f.read()
    ans1 = len(find_antinodes(*process_input(full)))
    print(ans1)


def find_antinodes_line(city, freqs):
    antinodes = set()
    for freq, locs in freqs.items():
        for f1, f2 in combinations(locs, 2): # Want to iterate over all pairs
            # Find the displacement vector between them
            df = f1 - f2
            # Search in two lines
            while f1 in city:
                antinodes.add(f1)
                f1 += df

            while f2 in city:
                antinodes.add(f2)
                f2 -= df

    return antinodes

assert len(find_antinodes_line(*process_input(ex))) == 34, "Part 2: Example wrong"

with open('./2024/inputs/08.txt', 'r') as f:
    full = f.read()
    ans2 = len(find_antinodes_line(*process_input(full)))
    print(ans2)


if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')


# %%
