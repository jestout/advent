import re

ex = r"""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def intl(text: str) -> tuple[int]:
    return list(map(int, re.findall(r'-?[0-9]+', text)))

def process_input(s):
    games = s.split('\n\n')
    return [[intl(l) for l in g.splitlines()] for g in games]


def solve(game):
    vec1, vec2, goal = game
    a, c = vec1
    b, d = vec2
    e, f = goal

    det = a*d - b*c
    n1 = (d * e - b * f) / det
    n2 = (-c * e + a * f) / det

    if n1 < 0 or n2 < 0 or n1 > 100 or n2 > 100:
        return False
    
    if n1.is_integer() and n2.is_integer():
        return [int(n1), int(n2)]
    
    return False


def num_of_needed_tokens(s):
    games = process_input(s)
    sum = 0

    for g in games:
        sol = solve(g)
        if sol:
            sum += 3 * sol[0] + sol[1]

    return sum

assert num_of_needed_tokens(ex) == 480, "Part 1: Example wrong!"

with open('./inputs/13.txt') as f:
    ans1 = num_of_needed_tokens(f.read())
    print(ans1)


def solve_new(game):
    vec1, vec2, goal = game
    a, c = vec1
    b, d = vec2
    e, f = goal
    e += 10000000000000
    f += 10000000000000

    det = a*d - b*c
    n1 = (d * e - b * f) / det
    n2 = (-c * e + a * f) / det

    print(n1, n2)
    if n1 < 0 or n2 < 0:
        return False
    
    if n1.is_integer() and n2.is_integer():
        return [int(n1), int(n2)]
    
    return False

def num_of_needed_tokens_new(s):
    games = process_input(s)
    sum = 0

    for g in games:
        sol = solve_new(g)
        if sol:
            sum += 3 * sol[0] + sol[1]

    return sum

with open('./inputs/13.txt') as f:
    ans2 = num_of_needed_tokens_new(f.read())
    print(ans2)

if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')

