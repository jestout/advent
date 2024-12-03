from itertools import pairwise, chain

ex = r"""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def check_report(diffs):
    if (d1 := next(diffs)) == 0:
        return False
    sign = 1 if d1 > 0 else -1

    return abs(d1 - 2 * sign) <= 1 and all(abs(d - 2 * sign) <= 1 for d in diffs)

def sol2a(input):
    return sum(
        check_report(y - x for x, y in pairwise(map(int, l.split())))
        for l in input.splitlines()
    )


assert sol2a(ex) == 2, "Part 1: Got example wrong"

with open('./2024/inputs/02.txt') as f:
    ans1 = sol2a(f.read())
    print(ans1)

def check_damp(diffs):
    if (prev_diff := next(diffs)) == 0:
        return check_report(diffs)

    sign = 1 if prev_diff > 0 else -1

    if abs(prev_diff - 2 * sign) > 1:
        return check_report(diffs)

    for i, d in enumerate(diffs):
        if abs(d - 2 * sign) > 1:
            try:
                next_diff = d + next(
                    diffs
                )  # Check to see if we are at the end of the list, get next element
                if abs(next_diff - 2 * sign) > 1:
                    if i == 0:  # Could just be that the list started off wrong
                        return check_report(chain(iter([d]), diffs))
                    else:  # Or it's just bad
                        return False
                return check_report(
                    chain(iter([next_diff]), diffs)
                )  # If we got here, then can check rest of list
            except StopIteration:  # At end of list, can just drop
                return True

        prev_diff = d

    return True


def sol2b(input):
    return sum(
        check_damp(y - x for x, y in pairwise(map(int, l.split())))
        for l in input.splitlines()
    )

assert sol2b(ex) == 4, "Part 2: Got example wrong"

with open('./2024/inputs/02.txt') as f:
    ans2 = sol2b(f.read())
    print(ans2)

if __name__ == "__main__":
    print(f'{ans1=}, {ans2=}')

