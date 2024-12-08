import re
from functools import reduce
from operator import mul, add
from math import sqrt, ceil, floor

ex = r"""Time:      7  15   30
Distance:  9  40  200"""

def ints(text: str) -> tuple[int]:
    return tuple(map(int, re.findall(r'-?[0-9]+', text)))

def process(s):
    times, dists = [ints(l) for l in s.splitlines()]
    return times, dists

def count_ways(total, record):
    return sum(h*(total - h) > record for h in range(0, total))


assert reduce(mul, [count_ways(t, r) for t, r in zip(*process(ex))]) == 288, "Part 1: Example wrong"


with open('./inputs/06.txt', 'r') as f:
    ans1 = reduce(mul, [count_ways(t, r) for t, r in zip(*process(f.read()))])
    print(ans1)

# Smarter
def calc_ways(t, r):
    sq = sqrt(t**2 - 4*r)
    lb, ub = 0.5 * (t - sq), 0.5 * (t + sq)
    ub = floor(ub) - 1 if abs(int(ub) - ub) < 1e-5 else floor(ub)
    lb = ceil(lb) + 1 if abs(int(lb) - lb) < 1e-5 else ceil(lb)
    return floor(ub) - ceil(lb) + 1

assert reduce(mul, [calc_ways(t, r) for t, r in zip(*process(ex))]) == 288
assert calc_ways(*tuple(int(reduce(add, map(str, x))) for x in process(ex))) == 71503, "Part 2: Example wrong!"

with open('./inputs/06.txt', 'r') as f:
    ans2 = calc_ways(*tuple(int(reduce(add, map(str, x))) for x in process(f.read())))
    print(ans2)


if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')

