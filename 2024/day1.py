from typing import Generator

example = r"""3   4
4   3
2   5
1   3
3   9
3   3"""

example_input = example.splitlines()

# Love to process inputs
def get_input(input: Generator[str, None, None] | list[str]) -> tuple[list[int], list[int]]:
    l1, l2 = [], []
    
    for line in input:
        x1, x2 = line.split()
        l1.append(int(x1))
        l2.append(int(x2))

    return l1, l2



def sol1a(l1: list[int], l2: list[int]) -> int:
    return sum(abs(x1 - x2) for x1, x2 in zip(sorted(l1), sorted(l2)))

# Test that example input matches
assert sol1a(*get_input(example_input)) == 11, "Part 1: got example input wrong"

# Part 1 Answer
with open('./inputs/day1.txt', 'r') as input:
    print(sol1a(*get_input(input)))


def sol2a(l1: list[int], l2: list[int]) -> int:
    # Construct dict of appearances in l2
    l2_counts = dict()
    for x in l2:
        l2_counts[x] = l2_counts.get(x, 0) + 1

    return sum(x * l2_counts.get(x, 0) for x in l1)


assert sol2a(*get_input(example_input)) == 31, "Part 2: got example input wrong"

with open('./inputs/day1.txt', 'r') as input:
    print(sol2a(*get_input(input)))

