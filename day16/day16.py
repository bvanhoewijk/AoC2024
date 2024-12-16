import sys
from pprint import pprint
def part1(file):
    path, _, start, end, grid = load_data(file)
    final_path, cost = dijkstra(start, end, path)
    
    for p, s in final_path[:-1]:
        grid[p[0]][p[1]] = s
    for row in grid:
        print("".join(row))
    print(f"Part1:\nsteps {len(final_path)-1}, cost: {cost}")


def part2(dataset):
    pass


def load_data(file):
    dataset = [list(item.strip()) for item in open(file, "r").readlines()]
    path = set()
    wall = set()
    start = ()
    end = ()
    for r in range(len(dataset[0])):
        for c in range(len(dataset)):
            if dataset[r][c] == ".":
                path.add((r, c))
            if dataset[r][c] == "#":
                wall.add((r, c))
            if dataset[r][c] == "S":
                path.add((r, c))
                start = (r, c)
            if dataset[r][c] == "E":
                path.add((r, c))
                end = (r, c)

    return path, wall, start, end, dataset


def dijkstra(start, end, pathblocks):
    dirs = [
        (-1, 0),  # Forward ^
        (1, 0),  # Down    v
        (0, 1),  # Right   >
        (0, -1),  # Left    <
    ]

    dirs_dict = dict(zip(dirs, list("^v><")))
    visited = set(start)
    path = []
    queue = []


    cost = 0
    queue.append((start, path + [(start, ">")], 0))

    i = 0
    while queue:
        queue = sorted(queue, key=lambda x: x[2], reverse=True)
        current, path, cost = queue.pop()
        r, c = current
        visited.add(current)
        for dir in dirs:
            next_dir = (r + dir[0], c + dir[1])
            symbol = dirs_dict[(dir[0], dir[1])]
            if (next_dir) == end:
                return path + [next_dir], cost+1
            if next_dir in pathblocks and next_dir not in visited:
                i += 1
                new_cost = cost + 1
                if path[-1][1] != symbol:
                    new_cost += 1000
                new_path = path + [(next_dir, symbol)]
                queue.append((next_dir, new_path, new_cost))

def main():
    part1("big.txt")



if __name__ == "__main__":
    main()
