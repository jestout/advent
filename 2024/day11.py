# %%
from collections import Counter
from math import floor, log10

def split(n):
    s = str(n)
    l = len(s)
    return int(s[:l//2]), int(s[l//2:])

def has_even(n):
    return floor(log10(n) % 2) != 0

def process_line(s):
    l = list(map(int, s.split()))
    rocks = Counter()
    for r in l:
        rocks[r] += 1
    return rocks

def blink(rocks):
    new_rocks = Counter()
    for r, n in rocks.items():
        if r == 0:
            new_rocks[1] += n
        elif has_even(r):
            r1, r2 = split(r)
            new_rocks[r1] += n
            new_rocks[r2] += n
        else:
            new_rocks[r * 2024] += n

    return new_rocks

def n_blink(rocks, n):
    for _ in range(n):
        rocks = blink(rocks)
    return rocks

def count_rocks(s, n):
    rocks = process_line(s)
    return n_blink(rocks, n).total()

assert count_rocks('125 17', 25) == 55312, 'Part 1: Example wrong!'
#%%
with open('./inputs/11.txt', 'r') as f:
    inp = f.read()
    ans1 = count_rocks(inp, 25)
    ans2 = count_rocks(inp, 75)

if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')
# %%
