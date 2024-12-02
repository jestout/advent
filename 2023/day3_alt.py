#%%
import re
from operator import mul
from functools import reduce

#%%
example = r"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open("inputs/03.txt") as f:
    schem = f.read()

def pad_input(input):
    l = input.find("\n")
    vert_pad = l*"." + "\n" + input + "\n" + l*"."
    return "." + vert_pad.replace("\n", ".\n.") + "."

schem = pad_input(schem)

# %%
def parse_dig(m, schem):
    l = schem.find("\n")+1
    s_above = schem[m.start()-l-1:m.end()-l+1]
    s_below = schem[m.start()+l-1:m.end()+l+1]
    s_l = schem[m.start()-1]
    s_r = schem[m.end()]

    gears = [(m.start()-l-1 + m2.start()) for m2 in re.finditer("[*]", s_above)] + [(m.start()+l-1 + m2.start()) for m2 in re.finditer("[*]", s_below)]
    gears += [m.start()-1] if s_l == "*" else []
    gears += [m.end()] if s_r == "*" else []

    s_tot = s_above+s_l + s_r + s_below

    return s_tot, gears

gear_dict = {}
id_sum = 0

for m in re.finditer("\d+", schem):
    
    num = int(m.group())
    s_text, gears = parse_dig(m, schem)

    for g in gears:
        gear_dict.setdefault(g, set()).add(num)

    if re.findall("[^.\d]", s_text):
        id_sum += num

print(id_sum)
print(sum(reduce(mul, list(i)) if len(i) == 2 else 0 for i in gear_dict.values()))