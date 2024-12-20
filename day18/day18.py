from tqdm import tqdm


def in_bounds(next_node, dataset_size):
    if next_node[0] < 0 or next_node[1] < 0:
        return False
    if next_node[0] >= dataset_size[0]:
        return False
    if next_node[1] >= dataset_size[1]:
        return False
    return True


dirs = [
    (-1, 0),  # Forward ^
    (0, 1),  # Right   >
    (1, 0),  # Down    v
    (0, -1),  # Left    <
]


def bfs(occupied, grid_size):
    start = (0, 0)
    end = (grid_size, grid_size)
    visited = set(start)
    queue = list()
    queue.append((start, 0))
    while queue:
        current, cost = queue.pop(0)
        r, c = current
        for dr, dc in dirs:
            next_dir = (r + dr, c + dc)
            if (
                not in_bounds(next_dir, (grid_size + 1, grid_size + 1))
                or next_dir in occupied
                or next_dir in visited
            ):
                continue
            if next_dir == end:
                return cost + 1
            else:
                visited.add(next_dir)
                queue.append((next_dir, cost + 1))
    return None


def part1():
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("big.txt", "r").readlines()
    ]
    # 268
    cost = bfs(occupied[:1024], 70)
    print(cost)


def part2():
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("big.txt", "r").readlines()
    ]
    occupied_sel = occupied[:1024]
    rest = occupied[1024:]

    for item in tqdm(rest):
        occupied_sel.append(item)
        cost = bfs(occupied_sel, 70)
        if cost == None:
            print("Part 2", item)
            break


def part2_binary_search():
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("big.txt", "r").readlines()
    ]

    lo = 0
    hi = len(occupied) - 1

    total_iter = 0
    while lo < hi:
        mi = (lo + hi) // 2
        cost = bfs(occupied[: mi + 1], 70)
        total_iter += 1
        if cost:
            lo = mi + 1
        else:
            hi = mi

    print(
        f"Coordinates: {",".join(map(str, occupied[lo]))}. Paths tested: {total_iter}"
    )


def main():
    # 268
    part1()

    # 64,11
    part2_binary_search()
    # This takes a while longer:
    part2()


if __name__ == "__main__":
    main()
