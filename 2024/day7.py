#%%
import re
from collections import deque

ex = r"""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def intd(text: str) -> tuple[int]:
    return deque(map(int, re.findall(r'-?[0-9]+', text)))

def mapl(x, y):
    return list(map(x, y))

def prepare_input(s):
    numbos = mapl(intd, s.splitlines())
    numbos = [[n.popleft(), n] for n in numbos]
    return numbos

def gen_paths(d: deque[int], goal=None):
    # Given a deque, want to generate two new possible deques
    d = deque(d)
    if len(d) == 1:
        if d[0] == goal: # End the search
            raise StopIteration
        return (d[0],)
    
    # First pop the first two elements.
    x, y = d.popleft(), d.popleft()

    # Now look at the two futures
    plus = gen_paths(deque([x+y]) + d, goal)
    mul = gen_paths(deque([x*y]) + d, goal)

    return (*plus, *mul)

def is_valid_test(goal, values):
    try:
        res = gen_paths(values, goal)
    except StopIteration:
        return True
    
    return False

assert sum([g for g, vals in prepare_input(ex) if is_valid_test(g, vals)]) == 3749, "Part 1: Example wrong!"

with open('./2024/inputs/07.txt') as f:
    full_input = prepare_input(f.read())
    ans1 = sum(g for g, vals in full_input if is_valid_test(g, vals))
    print(ans1)

def gen_paths_cat(d: deque[int], goal=None):
    # Given a deque, want to generate two new possible deques
    d = deque(d)
    if len(d) == 1:
        if d[0] == goal: # End the search
            raise StopIteration
        return (d[0],)
    
    # First pop the first two elements.
    x, y = d.popleft(), d.popleft()

    # Now look at the three futures
    plus = gen_paths_cat(deque([x+y]) + d, goal)
    mul = gen_paths_cat(deque([x*y]) + d, goal)
    cat = gen_paths_cat(deque([int(str(x) + str(y))]) + d, goal)

    return (*plus, *mul, *cat)

def is_valid_test_cat(goal, values):
    try:
        res = gen_paths_cat(values, goal)
    except StopIteration:
        return True
    
    return False

assert sum([g for g, vals in prepare_input(ex) if is_valid_test_cat(g, vals)]) == 11387, "Part 2: Example wrong!"

with open('./2024/inputs/07.txt') as f:
    full_input = prepare_input(f.read())
    ans2 = sum(g for g, vals in full_input if is_valid_test_cat(g, vals))
    print(ans2)

if __name__ == '__main__':
    print(f"Part 1: {ans1} | Part 2: {ans2}")