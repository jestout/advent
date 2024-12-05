# %%
from functools import cmp_to_key
from collections import defaultdict

# %%
ex = r"""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# %%


def parse_rules(rules):
    comes_before = defaultdict(set)

    for r in rules:
        before, after = r
        comes_before[before].add(after)

    return comes_before


def parse_input(input):
    rules, updates = input.split('\n\n')

    rules = [list(map(int, r.split('|'))) for r in rules.splitlines()]
    updates = [list(map(int, u.split(','))) for u in updates.splitlines()]
    
    rule_dict = parse_rules(rules)
    return rule_dict, updates


def is_update_good(update, rule_dict):
    already_seen = set()

    for u in update:
        if not already_seen.isdisjoint(rule_dict[u]):
            return False
        already_seen.add(u)

    return True


def mid(u):
    return u[len(u) // 2]


# %%
rule_dict, updates = parse_input(ex)
assert (
    sum(mid(u) for u in updates if is_update_good(u, rule_dict)) == 143
), "Part 1 example WRONG"

with open('./2024/inputs/05.txt', 'r') as f:
    rule_dict, updates = parse_input(f.read())
    ans1 = sum(mid(u) for u in updates if is_update_good(u, rule_dict))


# %%
def rule_cmp(x, y):
    return -1 if y in rule_dict.get(x) else 1


ans2 = sum(
    mid(sorted(u, key=cmp_to_key(rule_cmp)))
    for u in updates
    if not is_update_good(u, rule_dict)
)
# %%
if __name__ == '__main__':
    print(f'{ans1=} {ans2=}')
# %%
