import re

ex = r"""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

mul_pat = 'mul\\((\\d+),(\\d+)\\)'
res = re.findall(mul_pat, ex)

def sol3a(s):
    res = re.findall(mul_pat, s)
    return sum(int(r[0]) * int(r[1]) for r in res)

assert sol3a(ex) == 161, "Part 1: got example wrong"

with open('./2024/inputs/03.txt', 'r') as f:
    ans1 = sum(sol3a(s) for s in f.readlines())
    print(ans1)

ex2 = r"""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

instr_pat = "mul\\((\\d+),(\\d+)\\)|(do\\(\\))|(don't\\(\\))"

def sol3b(s):
    on = True
    sum = 0

    for m in re.finditer(instr_pat, s):
        if m.group() == 'do()':
            on = True
        elif m.group() == "don't()":
            on = False
        else:
            if on:
                x, y, _, _ = m.groups()
                sum += int(x) * int(y)
    
    return sum

assert sol3b(ex2) == 48, "Part 2: got example wrong"


with open('./2024/inputs/03.txt', 'r') as f:
    ans2 = sol3b(f.read())
    print(ans2)


if __name__ == "__main__":
    print(f'{ans1=}, {ans2=}')