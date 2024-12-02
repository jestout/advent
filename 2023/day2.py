#%%
from dataclasses import dataclass


#%%
ex = r"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

input = ex.splitlines()
#%%
@dataclass
class Round:
    red: int = 0
    blue: int = 0
    green: int = 0

class Game:
    gid: int
    rounds: list

    def __init__(self, s):
        gid, rounds = s.split(':')
        _, gid = gid.split()
        gid = int(gid)
        
        def get_Round(l: list) -> Round:
            return Round(**dict((x[1], int(x[0])) for x in l))
        
        rounds = rounds.split(';')
        rounds = [[color.split() for color in g.split(',')] for g in rounds]
        rounds = list(map(get_Round, rounds))

        self.gid, self.rounds = gid, rounds

    def __repr__(self):
        return f'Game {self.gid} - Rounds: {self.rounds}'
    
    def is_possible(self, r: int, g: int, b: int):

        def is_round_possible(round: Round, r: int, g: int, b: int) -> bool:
            return round.red <= r and round.blue <= b and round.green <= g

        return all(is_round_possible(rnd, r, g, b) for rnd in self.rounds)
    
    def get_minimum(self):
        r, g, b = 0, 0, 0
        
        for rnd in self.rounds:
            if r < rnd.red:
                r = rnd.red
            if g < rnd.green:
                g = rnd.green
            if b < rnd.blue:
                b = rnd.blue

        return r, g, b
    
    def min_power(self):
        r, g, b = self.get_minimum()
        return r * g * b


def sol2a(input):
    return sum(g.gid for s in input if (g := Game(s)).is_possible(12, 13, 14))

assert sol2a(input) == 8, "Part 1: got example input wrong"

with open('./inputs/02.txt', 'r') as f:
    ans1 = sol2a(f)

# %%

def sol2b(input):
    return sum(Game(s).min_power() for s in input)

assert sol2b(input) == 2286, "Part 2: got example input wrong"

with open('./inputs/02.txt', 'r') as f:
    ans2 = sol2b(f)

if __name__ == '__main__':
    print(f'{ans1=}, {ans2=}')
# %%
