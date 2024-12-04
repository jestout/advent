#%%
from parse import parse

#%%
ex = r"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
# %%

tmp = parse("Card {}: {} | {}", "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
# %%
def parse_card(s):
    num, win, numbos = parse("Card {}: {} | {}", s)
    num = int(num)
    win = set(map(int, win.split()))
    numbos = list(map(int, numbos.split()))
    return num, win, numbos
# %%
def calc_score(s):
    num, win, numbos = parse_card(s)
    winnos = [n for n in numbos if n in win]
    n_win = len(winnos)
    
    if n_win == 0:
        return 0
    else:
        return 2**(n_win-1)
# %%
assert sum(calc_score(s) for s in ex.splitlines()) == 13, "Part 1 example wrong"
#%%
with open('./2023/inputs/04.txt', 'r') as f:
    ans1 = sum(calc_score(s) for s in f.readlines())
    print(ans1)
# %%




