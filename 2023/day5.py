
from functools import reduce
from parse import parse

ex = r"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class IMap:
    def __init__(self, s):
        self.ranges = [list(map(int, l.split())) for l in s.splitlines()]

    def __call__(self, x):
        for m in self.ranges:
            if x in range(m[1], m[1] + m[2]):
                return x - m[1] + m[0]
            
        return x
    
def map_accumulate(func_list, x):
    yield (last_val := x)

    for m in func_list:
        yield (last_val := m(last_val))

def nest(funcs):
    return lambda x: reduce(lambda acc, f: f(acc), funcs, x)


def parse_input(s):
    seeds, *maps = s.split('\n\n')
    seeds = list(map(int, seeds.split(':')[-1].split()))
    maps = [m.split(':')[-1].strip() for m in maps]
    maps = list(map(IMap, maps))
    return seeds, maps


def sol5a(s):
    seeds, maps = parse_input(s)
    return min(nest(maps)(seed) for seed in seeds)


assert sol5a(ex) == 35, 'Part 1 example wrong!'


with open('./2023/inputs/05.txt') as f:
    ans1 = sol5a(f.read())


# Do it another way
from parse import parse
import portion

lmap = lambda x, y: list(map(x, y))
    
def map_seed(seed, s):
    instruct = parse('{key1}-to-{key2} map:{maps}', s)
    loc_in = seed[instruct['key1']]
    maps = instruct['maps'].strip().splitlines()
    updated = False

    for m in maps:
        out_start, in_start, map_range = list(map(int, m.split()))
        #Check if loc_in is in the in_range
        if loc_in in range(in_start, in_start + map_range):
            seed[instruct['key2']] = loc_in - in_start + out_start
            updated = True

    if not updated:
        seed[instruct['key2']] = seed[instruct['key1']]

    return seed

def seed_gen_ind(seed_sp):
    for i in parse('seeds: {}', seed_sp)[0].split():
        yield i

def seed_gen_range(seed_sp):
    seed_spec = [int(i) for i in parse('seeds: {}', seed_sp)[0].split()]
    for i in range(0, len(seed_spec), 2):
        for j in range(seed_spec[i], seed_spec[i] + seed_spec[i+1]):
            yield j

def sol1a(s):
    input = s.split('\n\n')
    seed_list = [{'seed' : int(i)} for i in seed_gen_ind(input[0])]

    for seed in seed_list:
        for m in input[1:]:
            seed = map_seed(seed, m)

    return min(seed['location'] for seed in seed_list)
    
assert sol1a(ex) == 35

with open('./2023/inputs/05.txt', 'r') as f:
    ans1 = sol1a(f.read())


def seed_gen_interval(seed_sp):
    seed_spec = [int(i) for i in parse('seeds: {}', seed_sp)[0].split()]
    tmp = portion.empty()

    for start, range in zip(seed_spec[::2], seed_spec[1::2]):
        tmp = tmp.union(portion.closedopen(start, start + range))
        
    return tmp

def map_seed_int(seed, s):
    instruct = parse('{key1}-to-{key2} map:{maps}', s)
    in_terval = seed[instruct['key1']]
    maps = instruct['maps'].strip().splitlines()

    total_mapped = portion.empty()
   
    for map_spec in maps:
        # Get the specs
        out_start, in_start, m_range = [int(i) for i in map_spec.split()]
        
        # Compute the domain of the map and the bias
        bias = out_start - in_start
        dom_int = portion.closedopen(in_start, in_start + m_range)
       
        # Figure out which of the interval is affected
        aff_int = in_terval.intersection(dom_int)
        # Add it to the total mapped interval
        total_mapped =  total_mapped | aff_int.apply(lambda x: (x.left, x.lower + bias, x.upper + bias, x.right))
        
        # Remove it from the interval yet to be affected
        in_terval = in_terval - aff_int

    seed[instruct['key2']] = in_terval | total_mapped

    return seed

def sol5b(s):
    input = s.split('\n\n')
    seed = {"seed" : seed_gen_interval(input[0])}

    for m in input[1:]:
        seed = map_seed_int(seed, m)

    return seed['location'].lower


assert sol5b(ex) == 46, "Part 2; example wrong!"


with open('./2023/inputs/05.txt', 'r') as f:
    ans2 = sol5b(f.read())

if __name__ == '__main__':
    print(f'{ans1=} {ans2=}')

