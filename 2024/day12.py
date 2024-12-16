#%%
from collections import defaultdict
#%%
ex = r"""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
# %%

def process_input(s):
    clusters = defaultdict(dict) # Dictionary of cluster -> position
    positions = defaultdict(dict) # Dictionary of position -> cluster

    for x, l in enumerate(s.splitlines()):
        for y, c in enumerate(l):
            pos = x + y * 1j

            # Want to check to see if this is in any cluster
            # Just need to look up and to the left because of how
            # we move through the list.

            cluster_up = positions[c].get(pos - 1, None)
            cluster_left = positions[c].get(pos - 1j, None)

            if cluster_up is not None and cluster_left is not None:
                # Both exist
                if cluster_up != cluster_left: # Need to heal
                    for cpos in clusters[c][cluster_left]:
                        clusters[c][cluster_up].add(cpos)
                        positions[c][cpos] = cluster_up

                    del clusters[c][cluster_left]

                clusters[c][cluster_up].add(pos)
                positions[c][pos] = cluster_up
            elif cluster_up is None and cluster_left is None:
                # Then we just define a new cluster with name pos
                clusters[c][pos] = {pos}
                positions[c][pos] = pos
            else:
                # Then one of them is an integer.
                clust = cluster_up if cluster_left is None else cluster_left
                clusters[c][clust].add(pos)
                positions[c][pos] = clust

    return positions, clusters
# %%
def measure(els):
    area = len(els)
    tmp = set()
    perimeter = 0

    for pos in els:
        perimeter += 4 - 2 * sum(pos + z in tmp for z in [-1j, 1j, -1, 1])
        tmp.add(pos)

    return area, perimeter
# %%
def calc_total_cost(cluster_list):
    total_cost = 0

    for clusters in cluster_list.values():
        for els in clusters.values():
            area, perimeter = measure(els)
            total_cost += area * perimeter

    return total_cost
# %%
pos, clust = process_input(ex)
assert calc_total_cost(clust) == 1930, "Part 1: Example wrong!"
# %%
with open('./inputs/12.txt', 'r') as f:
    pos, clust = process_input(f.read())
    ans1 = calc_total_cost(clust)

# %%
def full_measure(els):
    area = len(els)
    tmp = set()
    corners = list() # A single element can constitute more than one corner, but # corner = # sides
    perimeter = 0

    for pos in els:
        # Grow perimeter based on elements we have already seen
        perimeter += 4 - 2 * sum(pos + z in tmp for z in [-1j, 1j, -1, 1])
        tmp.add(pos)

        # Want to check if this is a corner; have two types of cases
        # XXXX  or  XXOO
        # XXOO      XXOO
        # XXO       OOOO
        # or rotations of this
        # In case 1, have a corner if -1j, -1 are all not in els
        # In case 2, have a corner if -1j and -1 are in els but -1 -1j is not.
        # Then, we can rotate these by multiplying by 1j. 
        # For instance, in case 1 we first get 1, 1 - 1j, and -1j, corresponding to
        # XXXOOOO
        # XXXOOOO
        # XXXXXXX

        for rot in [1, 1j, -1, -1j]:
            # Case 1
            if all(pos + rot * z not in els for z in [-1j, -1]):
                corners.append(pos)
            # Case 2        
            if all(pos + rot * z in els for z in [-1j, -1]) and pos + rot*(-1 -1j) not in els:
                corners.append(pos)
    
    num_sides = len(corners)

    return area, perimeter, num_sides


# %%

def calc_total_cost_sides(cluster_list):
    total_cost = 0

    for clusters in cluster_list.values():
        for els in clusters.values():
            area, perimeter, num_sides = full_measure(els)
            total_cost += area * num_sides

    return total_cost

#%%
with open('./inputs/12.txt', 'r') as f:
    pos, clust = process_input(f.read())
    ans2 = calc_total_cost_sides(clust)
# %%
if __name__ == '__main__':
    print(f'Part 1: {ans1} | Part 2: {ans2}')

