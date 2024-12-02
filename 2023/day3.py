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

# %%

def prep_input(input):
    new_input = ['.' + l + '.' for l in input.splitlines()]
    pad = ''.join(len(new_input[0])*['.'])
    input = pad + '\n' + '\n'.join(new_input) + '\n' + pad

    return [list(l) for l in input.splitlines()]


# %%
input = prep_input(example)
#%%
class Num:
    number: int
    row: int
    span: tuple[int]
    adj_parts: list[tuple[int]]

    def __init__(self, number, row, span, input):
        self.number = number
        self.row = row
        self.span = span
        self.find_adj_parts(input)
    
    def find_adj_parts(self, input):
        self.adj_parts = []

        not_part = '123456789.'
        row = self.row
        span = self.span

        if (c := input[row][span[0]-1]) not in not_part:
            self.adj_parts.append([c, (row, span[0]-1)])
        
        if (c := input[row][span[1]+1]) not in not_part:
            self.adj_parts.append([c, (row, span[1]+1)])

        for i in range(span[0]-1, span[1] + 2):
            if (c := input[row+1][i]) not in not_part:
                self.adj_parts.append([c, (row+1, i)])
            if (c := input[row-1][i]) not in not_part:
                self.adj_parts.append([c, (row-1, i)])

        return self.adj_parts
    
    def __repr__(self):
        return f'{self.number} at ({self.row}, {self.span[0]}) through ({self.row}, {self.span[1]})'

# %%
def get_numbos(input):
    numbo_list = []

    for i, l in enumerate(input):
        nums = []
        start = None

        for j, c in enumerate(l):
            if c in '1234567890':
                if start is None:
                    start = j
            else:
                if start is not None:
                    nums.append((start, j-1))
                    start = None
        
        for t in nums:
            val = int(''.join(l[t[0]:t[1]+1]))
            numbo_list.append(Num(val, i, t, input))

    return numbo_list
# %%

def sol3a(input):
    prepped_input = prep_input(input)
    return sum(n.number for n in get_numbos(prepped_input) if len(n.adj_parts) > 0)

assert sol3a(example) == 4361, "Part 1: Got example input wrong!"

with open('./inputs/03.txt', 'r') as f:
    finput = f.read()
    ans1 = sol3a(finput)

# %%
def sol3b(input):
    prepped_input = prep_input(input)
    gear_list = dict()
    for n in get_numbos(prepped_input):
        for p in n.adj_parts:
            if p[0] == '*':
                gear_list[p[1]] = gear_list.get(p[1], []) + [n]

    return sum([v[0].number * v[1].number for v in gear_list.values() if len(v) == 2])

assert sol3b(example) == 467835, "Part 2: Got example input wrong!"
#%%
with open('./inputs/03.txt', 'r') as f:
    finput = f.read()
    ans2 = sol3b(finput)
#%%
if __name__ == '__main__':
    print(f'{ans1=}, {ans2=}')
# %%
