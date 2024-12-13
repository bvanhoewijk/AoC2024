from pprint import pprint

def in_bounds(next_node, dataset_size):
    if next_node[0] < 0 or next_node[1] < 0:
        return False
    if next_node[0] >= dataset_size[0]:
        return False
    if next_node[1] >= dataset_size[1]:
        return False
    return True

def find_plot_info(dataset, target_letter, r, c, directions):
    queue = [(r,c)]
    out_of_bounds = 0
    seen = set()
    perimeter_set = set()
    dataset_size = (len(dataset), len(dataset[0]))
    while queue:
        current = queue.pop()
        seen.add(current)
        for dr, dc in directions:
            next_pos = (current[0] + dr, current[1] + dc)
            
            if not in_bounds(next_pos, dataset_size):
                perimeter_set.add((next_pos, (dr, dc)))
                continue
            if dataset[next_pos[0]][next_pos[1]] == target_letter: 
                if next_pos not in seen:
                    queue.append(next_pos)
            else:
                perimeter_set.add((next_pos, (dr, dc)))

    return seen, out_of_bounds, perimeter_set


def part1(dataset):
    seen_all = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Start + Letter
    price = 0
    for r in range(len(dataset)):
        for c in range(len(dataset[0])):
            target_letter = dataset[r][c]
            if (r,c) not in seen_all:
                seen, out_of_bounds, perimeter_set = find_plot_info(dataset, target_letter, r, c, directions)
                seen_all = seen_all | seen
                price += len(seen) * (out_of_bounds + len(perimeter_set))
    print("Part1",price)

def get_nodes(perimeter_set):
    nodes = set()
    for item in perimeter_set:
        nodes.add(item[0])
    return nodes

def fence_sides(nodes):
    seen = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = list(nodes[0])
    fence_size = 1
    while queue:
        current = queue.pop()
        seen.add(current)
        for dr, dc in [(0, 1), (0, -1)]:
            next_pos = (current[0] + dr, current[1] + dc)
            if next_pos in nodes:
                queue.add(next_pos)



def part2(dataset):
    seen_all = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    # Start + Letter
    price = 0
    for r in range(len(dataset)):
        for c in range(len(dataset[0])):
            target_letter = dataset[r][c]
            if (r,c) not in seen_all:
                if not target_letter == "E": continue
                print(target_letter)
                seen, out_of_bounds, perimeter_set = find_plot_info(dataset, target_letter, r, c, directions)
                price += len(seen) * (out_of_bounds + len(perimeter_set))
                seen_all = seen_all | seen
                p = get_nodes(perimeter_set)
                fence_sides(p)
    

# A: 4*10
# B: 4*8
# C: 4*10
# D: 1*4
# E: 3*8
if __name__ == "__main__":
    dataset = [[row for row in item.strip()] for item in open("small3.txt", "r").readlines()]
    # pprint(dataset)

    part2(dataset)