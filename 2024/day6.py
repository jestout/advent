ex = r"""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

or_dict  = {
    '^': -1j,
    '>': 1,
    'v': 1j,
    '<': -1
}

def process_map(s):
    room = set()
    obstacles = set()
    state = None

    for y, l in enumerate(s.splitlines()):
        for x, c in enumerate(l):
            pos = x + y * 1j
            if c == '#':
                obstacles.add(pos)
            elif c in or_dict.keys():
                state = (pos, or_dict[c])

            room.add(pos)
    
    return state, obstacles, room

def walk(state, obstacles, room):
    pos, dir = state
    while pos in room:
        yield pos
        if pos + dir in obstacles:
            dir *= 1j
        else: # Either turn OR step, not maybe turn, then step
            pos += dir

assert len(set(walk(*process_map(ex)))) == 41, 'Part 1: Example wrong!'

with open('./inputs/06.txt', 'r') as f:
    ans1 = len(set(walk(*process_map(f.read()))))
    print(ans1)

def check_loop(state, obstacles, room):
    pos, dir = state
    hist = set(state)

    while pos in room:
        # check if we need to turn
        if pos + dir in obstacles:
            dir *= 1j
        else:
            pos += dir
        # check if we've been here
        if (pos, dir) in hist:
            return True
        else:
            hist.add((pos, dir))
    
    return False

def gen_loopers(state, obstacles, room):
    pos, dir = state

    while pos in room:
        new_pos = pos + dir
        if new_pos in obstacles: #If facing an obstacle, turn right
            dir *= 1j
            continue    #Try again
        
        if new_pos in room:
            # Check to see if adding an obstacle at pos + dir creates a looper
            obs = set(obstacles)
            obs.add(new_pos)
            if check_loop(state, obs, room):
                yield new_pos

        pos = new_pos

assert len(set(gen_loopers(*process_map(ex)))) == 6, "Part 2: Example wrong!"

with open('./inputs/06.txt', 'r') as f:
    ans2 = len(set(gen_loopers(*process_map(f.read()))))
    print(ans2)

if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')