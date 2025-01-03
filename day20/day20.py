from collections import Counter

def part1(file):
    pathblocks, wallblocks, start, end, dataset = load_data(file)
    path = dijkstra(start, end, pathblocks)
    path_dict = dict()
    for p in path:
        path_dict[p[0]] = p[2]
    
    previous = set()
    
    counter = Counter()
    for point in path_dict:
        previous.add(point)
        for d in dirs:
            nr, nc = d
            alt_point = (point[0] + nr*2, point[1] + nc*2)
            if alt_point in path_dict and alt_point not in previous:
                saved = path_dict[point] - path_dict[alt_point] + 2
                if saved:
                    counter[abs(saved)] += 1

    answer = 0
    for c in sorted(counter.keys()):
        if c >= 100:
            answer += counter[c]

    print(f"There are {answer} cheats that save at least 100 ps")

dirs = [
    (-1, 0),  # Forward ^
    (1, 0),  # Down    v
    (0, 1),  # Right   >
    (0, -1),  # Left    <
]
def load_data(file):
    dataset = [list(item.strip()) for item in open(file, "r").readlines()]
    path = set()
    wall = set()
    start = ()
    end = ()
    for r in range(1, len(dataset[0])-1, 1):
        for c in range(1, len(dataset)-1, 1):
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
    queue.append((start, path + [(start, ">", 0)], 0))

    while queue:
        # if len(queue) > 1:
        #     queue = sorted(queue, key=lambda x: x[2], reverse=True)

        current, path, cost = queue.pop(0)
        r, c = current
        visited.add(current)
        for dir in dirs:
            next_dir = (r + dir[0], c + dir[1])
            symbol = dirs_dict[(dir[0], dir[1])]
            if (next_dir) == end:
                return path + [(next_dir, symbol, new_cost+1)]
            if next_dir in pathblocks and next_dir not in visited:
                new_cost = cost + 1
                new_path = path + [(next_dir, symbol, new_cost)]
                queue.append((next_dir, new_path, new_cost))
    return None, None

def part2(file):
    pathblocks, wallblocks, start, end, dataset = load_data(file)
    path = dijkstra(start, end, pathblocks)
    path_dict = dict()
    for p in path:
        path_dict[p[0]] = p[2]
    
    count = 0
    for r in range(len(dataset)):
        for c in range(len(dataset[0])):
            if dataset[r][c] == "#": continue
            for radius in range(2, 21):
                for dr in range(radius +1):
                    dc = radius + dr
                    for nr, nc in {(r + dr, c + dc), (r+dr, c-dr), (r-dr, c+dc), (r-dr, c-dc)}:
                        if nr < 0 or nc < 0 or nr >= len(dataset) or nc >= len(dataset): continue
                        if dataset[nr][nc] == "#": continue
                        if (path_dict[(r, c)] - path_dict[(nr, nc)]) >= 50 + radius: count += 1
    print(count)

def main():
    # part1("big.txt")
    # 110986 too low.
    # 2522201 too high.
    # 1236185 too high.
    part2("small.txt")
                
if __name__ == "__main__":
    main()