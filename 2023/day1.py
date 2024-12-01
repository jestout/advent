#%%
ex = r"""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
#%%
input = ex.splitlines()

#%%

def cal_val(s: str) -> int:
    f, l = get_bookends(s)
    return f * 10 + l

#%% Wasteful solution

# def get_bookends(s: str) -> tuple[int]:
#     l = [c for c in s if c in '123456789']
#     return map(int, (l[0], l[-1]))

# assert sum(cal_val(s) for s in input) == 142, "Part 1 example wrong"

#%%
def get_bookends(s: str) -> tuple[int]:
    for c in s:
        try:
            f = int(c)
            break
        except:
            continue

    for c in reversed(s):
        try:
            l = int(c)
            break
        except:
            continue

    return (f, l)


assert sum(cal_val(s) for s in input) == 142, "Part 1 example wrong"

with open('./inputs/01.txt', 'r') as f:
    ans1 = sum(cal_val(s) for s in f)

# %%
ex = r"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

input = ex.splitlines()

nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

nums = nums | dict([(str(i), i) for i in range(1, 10)])

def get_bookends(s: str) -> tuple[int]:
    f_locs = min([(k, x) for k in nums.keys() if (x := s.find(k)) >= 0], key=lambda t: t[1])
    r_locs = max([(k, x) for k in nums.keys() if (x := s.rfind(k)) >= 0], key=lambda t: t[1])

    return nums[f_locs[0]], nums[r_locs[0]]

assert sum(cal_val(s) for s in input) == 281, "Part 2 example wrong"

with open('./inputs/01.txt', 'r') as f:
    ans2 = sum(cal_val(s) for s in f)


#%%
if __name__ == '__main__':
    print(f"{ans1=}, {ans2=}")
# %%
