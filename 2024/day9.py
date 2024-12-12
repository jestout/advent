from collections import deque

ex = '2333133121414131402'

def process_input(s):
    return deque([(None if i % 2 else i//2, int(c)) for i, c in enumerate(s)])

def check_sum(mem):
    sum = 0
    pos = 0 # Position we are at in memory

    while mem: 

        while True: # Get first valid f_id
            if not mem:
                return sum
            f_id, f_val = mem.popleft()
            if f_val != 0: # Make sure the front value isn't empty
                break
        
        if f_id is None: # Pop from the back
            while True: # Get the first nonempty value
                if not mem:
                    return sum
                b_id, b_val = mem.pop()
                if b_id is not None and b_val != 0:
                    break
            
            while f_val > 0 and b_val > 0:
                sum += pos * b_id # Update checksum
                b_val -= 1
                f_val -= 1
                pos += 1
            
            if b_val > 0:
                mem.append((b_id, b_val))

        else: # Can just append from the front
            while f_val > 0:
                sum += pos * f_id
                f_val -= 1
                pos += 1
        
        if f_val > 0:
            mem.appendleft((f_id, f_val))
    
    return sum

assert check_sum(process_input(ex)) == 1928, "Part 1: Example wrong!"

with open('./inputs/09.txt', 'r') as f:
    ans1 = check_sum(process_input(f.read().strip()))
    print(ans1)

def reg_check_sum(mem):
    sum = 0
    pos = 0

    while mem:
        f_id, f_val = mem.popleft()

        if f_id is None:
            pos += f_val
            continue

        while f_val > 0:
            sum += pos * f_id
            f_val -= 1
            pos += 1

    return sum

def walk(d):
    front = deque()
    mid = None
    back = deque(d)

    while back:
        if mid is not None:
            front.append(mid)

        mid = back.popleft()
        yield front, mid, back
    

def rearrange(mem):
    rmem = deque()

    while mem: # Work our way through
        b_id, b_val = mem.pop()

        if b_id is None: # Don't have to move
            rmem.appendleft((b_id, b_val))
        else:
            moved = False
            for front, (m_id, m_val), back in walk(mem):
                if m_id is None and m_val >= b_val: # Found an empty spot
                    mid = deque([(b_id, b_val)])
                    if m_val != b_val: # split into two
                        mid.append((None, m_val - b_val))
                    mid.extendleft(reversed(front))
                    mid.extend(back)

                    mem = mid
                    moved = True
                    break
            
            rmem.appendleft((None, b_val) if moved else (b_id, b_val))
    
    return rmem

assert reg_check_sum(rearrange(process_input(ex))) == 2858, "Part 2: Example wrong!"

with open('./inputs/09.txt', 'r') as f:
    ans2 = reg_check_sum(rearrange(process_input(f.read().strip())))
    print(ans2)


if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')

