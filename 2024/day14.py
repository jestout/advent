from collections import Counter
from functools import reduce
import re

ex = r"""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

class Robot: 
    def __init__(self, s, bounds):
        vals = list(map(int, re.findall(r'-?[0-9]+', s)))
        self.p = vals[:2]
        self.v = vals[2:]
        self.bounds = bounds
        self.steps = 0

    def step(self):
        p, v, b = self.p, self.v, self.bounds
        self.steps += 1
        self.p = [(p[0] + v[0]) % b[0], (p[1] + v[1]) % b[1]]
        return self

    def walk(self, n):
        p, v, b = self.p, self.v, self.bounds
        self.steps += n
        self.p = [(p[0] + n * v[0]) % b[0], (p[1] + n * v[1]) % b[1]]
        return self
    
    def get_quadrant(self):
        p, b = self.p, self.bounds
        
        if p[0] in range(0, b[0]//2) and p[1] in range(0, b[1]//2):
            # upper left
            return 0
        if p[0] in range(b[0]//2 + 1, b[0]) and p[1] in range(0, b[1]//2):
            # upper right
            return 1
        if p[0] in range(0, b[0]//2) and p[1] in range(b[1]//2 + 1, b[1]):
            # lower left
            return 2
        if p[0] in range(b[0]//2 + 1, b[0]) and p[1] in range(b[1]//2 + 1, b[1]):
            return 3

        return None

def part1(s, bounds): 
    counts = Counter(Robot(l, bounds).walk(100).get_quadrant() for l in s.splitlines())
    valid_counts = (v for k, v in counts.items() if k is not None)
    return reduce(lambda x, y: x * y, valid_counts)

assert part1(ex, [11, 7]) == 12, "Part 1: Example wrong!"

with open('./inputs/14.txt', 'r') as f:
    ans1 = part1(f.read(), [101, 103])
    print(ans1)


with open('./inputs/14.txt', 'r') as f:
    inp = f.read()
    robots = [Robot(l, [101, 103]) for l in inp.splitlines()]

def print_map(robots, bounds):
    plan = [[' ' for _ in range(bounds[0])] for _ in range(bounds[1])]
    for r in robots:
        plan[r.p[1]][r.p[0]] = '*'
    
    print('\n'.join(''.join(l) for l in plan[20:52]))


with open('./inputs/14.txt', 'r') as f:
    inp = f.read()
    robots = [Robot(l, [101, 103]) for l in inp.splitlines()]

#%%
def get_max_counts(robots):
    #x_counts = Counter(r.p[0] for r in robots)
    y_counts = Counter(r.p[1] for r in robots if r.p[1] != 20 and r.p[1] != 52)
    return max(y_counts.values())

def get_counts(robots):
    y_counts = Counter(r.p[1] for r in robots)
    return y_counts

hist = []
robots = [Robot(l, [101, 103]) for l in inp.splitlines()]
for i in range(10000):
    hist.append([i, get_max_counts(robots)])
    [r.step() for r in robots]

sorted(hist, key = lambda x: x[1], reverse=True)
# Can see that we get a max line of 34 every 103 steps, starting at 31.
# This is the max it gets to over 100000 steps, so start checking to see
# what happens to other lines.

robots = [Robot(l, [101, 103]).walk(31) for l in inp.splitlines()]

[r.walk(103) for r in robots]
print_map(robots, [101, 103])

[r.walk(103) for r in robots]
get_counts(robots)

print_map(robots, [101, 103])

def get_max_counts(robots, exclude=[]):
    #x_counts = Counter(r.p[0] for r in robots)
    y_counts = Counter(r.p[1] for r in robots if r.p[1] not in exclude)
    return max(y_counts.items(), key=lambda x: x[1])

[r.walk(103) for r in robots]
get_max_counts(robots, [20, 52, 44, 43, 42])

[r.walk(103) for r in robots]
print_map(robots, [101, 103])

robots[0].steps # Visually found it after 7344

