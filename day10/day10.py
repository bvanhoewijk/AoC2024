from pprint import pprint

all_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def in_bounds(next_node, dataset_size):
    if next_node[0] < 0 or next_node[1] < 0:
        return False
    if next_node[0] >= dataset_size[0]:
        return False
    if next_node[1] >= dataset_size[1]:
        return False
    return True


def traverse_trail(dataset, start, part1):
    dataset_size = (len(dataset), len(dataset[0]))
    seen = None
    if part1 == True:
        seen = set()
    else:
        seen = []

    queue = [(start, 0)]
    while queue:
        current, current_int = queue.pop()
        if current_int == "9":
            if part1:
                seen.add(current)
            else:
                seen.append(current)

        # seen.add(current)
        for dr, dc in all_directions:
            next_pos = (current[0] + dr, current[1] + dc)
            if (
                in_bounds(next_pos, dataset_size)
                and dataset[next_pos[0]][next_pos[1]] != "."
            ):
                next_int = dataset[next_pos[0]][next_pos[1]]
                if int(next_int) == int(current_int) + 1:
                    queue.append((next_pos, next_int))
    return seen


def all_starts(dataset):
    all_starts = []
    for r in range(len(dataset)):
        for c in range(len(dataset[0])):
            if dataset[r][c] == "0":
                all_starts.append((r, c))
    return all_starts


def part1(dataset):
    trail_heads = 0
    for start in all_starts(dataset):
        trail_heads += len(traverse_trail(dataset, start, True))
    print("Part1 ", trail_heads)


def part2(dataset):
    trail_heads = 0
    for start in all_starts(dataset):
        trail_heads += len(traverse_trail(dataset, start, False))
    print("Part2 ", trail_heads)


if __name__ == "__main__":
    dataset = [list(list(line.strip())) for line in open("big.txt", "r").readlines()]
    for row in dataset:
        print("".join(row))

    part1(dataset)
    part2(dataset)
