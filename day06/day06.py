from pprint import pprint

all_directions = [
    (-1, 0), # Forward ^
    (0, 1),  # Right   >
    (1, 0),  # Down    v
    (0, -1), # Left    <
]  


def in_bounds(next_node, dataset_size):
    if next_node[0] < 0 or next_node[1] < 0:
        return False
    if next_node[0] >= dataset_size[0]:
        return False
    if next_node[1] >= dataset_size[1]:
        return False
    return True


def find_start(dataset):
    for r, row in enumerate(dataset):
        for c, col in enumerate(row):
            if dataset[r][c] == "^":
                return r, c


def part1(dataset, r, c):
    dataset_size = (len(dataset), len(dataset[0]))
    seen = set()
    turn = 0
    while True:
        seen.add((r, c))
        next_r = r + all_directions[turn][0]
        next_c = c + all_directions[turn][1]
        if not in_bounds((next_r, next_c), dataset_size):
            return seen
        if dataset[next_r][next_c] == "#":
            turn += 1
            if turn == 4: turn = 0
        else:
            r = next_r
            c = next_c


def do_loop(dataset, r, c):
    dataset_size = (len(dataset), len(dataset[0]))

    seen = set()
    turn = 0
    while True:
        seen.add((r, c, turn))
        next_r = r + all_directions[turn][0]
        next_c = c + all_directions[turn][1]
        if not in_bounds((next_r, next_c), dataset_size):
            return False
        if dataset[next_r][next_c] == "#":
            turn += 1
            if turn == 4: turn = 0
        else:
            r = next_r
            c = next_c
        if (r, c, turn) in seen:
            return True


def part2(dataset, start, visited):
    loops = 0
    for item in list(visited):
        dataset[item[0]][item[1]] = "#"
        loops += do_loop(dataset, start[0], start[1])
        dataset[item[0]][item[1]] = "."
    print("Loops", loops)


# 696 is too low
# 1861 is too high
if __name__ == "__main__":
    dataset = [list(line.strip()) for line in open("big.txt", "r").readlines()]
    r, c = find_start(dataset)

    visited = part1(dataset, r, c)
    print("Part1", len(visited))

    # 1812
    dataset = [list(line.strip()) for line in open("big.txt", "r").readlines()]
    visited = part2(dataset, (r, c), set(visited))
