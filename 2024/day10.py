
from collections import defaultdict

ex = r"""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def process_map(s):
    trail_map = defaultdict(lambda : -1)
    trail_heads = set()

    for x, l in enumerate(s.splitlines()):
        for y, c in enumerate(l):
            pos = x + y * 1j
            trail_map[pos] = int(c) if c != '.' else -1
            if c != '.' and int(c) == 0:
                trail_heads.add(pos)
    
    return trail_map, trail_heads

def walk(trails, pos, peaks):
    val = trails[pos]

    if val == 9:
        if type(peaks) is set:
            peaks.add(pos)
        elif type(peaks) is list:
            peaks.append(pos)
    
    for z in [1j, -1j, 1, -1]:
        if trails[pos + z] == val + 1:
            walk(trails, pos + z, peaks)

def count_trails(s, unique=False):
    trail_map, trail_heads = process_map(s)
    count = 0

    for h in trail_heads:
        peaks = list() if unique else set()
        walk(trail_map, h, peaks)
        count += len(peaks)
    
    return count

assert count_trails(ex) == 36, "Part 1: Example wrong!"

with open('./inputs/10.txt', 'r') as f:
    ans1 = count_trails(f.read())

assert count_trails(ex, unique=True) == 81, "Part 2: Example wrong!"

with open('./inputs/10.txt', 'r') as f:
    ans2 = count_trails(f.read(), unique=True)

if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')

