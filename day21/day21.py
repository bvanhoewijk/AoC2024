from functools import cache
from itertools import product

dirs = [
    (-1, 0), # Up      ^
    (1, 0),  # Down    v
    (0, 1),  # Right   >
    (0, -1), # Left    <
]
keypad_coords = {"7" : (0,0), "8" : (0,1), "9" : (0,2),
                     "4" : (1,0), "5" : (1,1), "6" : (1,2),
                     "1" : (2,0), "2" : (2,1), "3" : (2,2),
                     "G" : (3,0), "0" : (3,1), "A" : (3,2)}

keypad = ((7,8,9),
            (4,5,6),
            (1,2,3),
            ("G",0,"A"))

dir_pad_coords = {"G" : (0,0), "^" : (0,1), "A" :  (0,2),
                    "<" : (1,0), "v" : (1,1), ">" :  (1,2)}

dirpad = (("G", "^", "A"),
            ("<" , "v", ">"))
@cache
def in_bounds(next_node, dataset_size):
    rows = next_node[0]
    cols = next_node[1]
    width = dataset_size[0]
    height = dataset_size[1]
    return 0 <= cols < width and 0 <= rows < height

@cache
def dijkstra(start, end, key_pad):
    dsize = (len(key_pad[0]), len(key_pad))
    dirs_dict = dict(zip(dirs, list("^v><")))

    visited = set(start)
    path = []
    queue = []

    queue.append((start, [], 0))

    all_paths = []
    optimal = 1000
    while queue:
        current, path, cost = queue.pop(0)
        r, c = current
        visited.add(current)
        for dir in dirs:
            next_dir = (r + dir[0], c + dir[1])
            symbol = dirs_dict[(dir[0], dir[1])]
            if (next_dir) == end:
                if optimal < cost + 1:
                    break
                optimal = cost + 1
                all_paths.append(path + [(next_dir, symbol, cost+1)])
            if not in_bounds(next_dir, dsize):
                continue
            if next_dir in visited:
                continue

            key_pad_value = key_pad[next_dir[0]][next_dir[1]]
            if key_pad_value == "G":
                continue
            else:       
                new_path = path + [(next_dir, symbol, cost+1)]
                queue.append((next_dir, new_path, cost+1))

    shortest = [all_paths[0]]
    for path in all_paths[1:]:
        if path[-1][2] <= shortest[0][-1][2]:
            shortest.append(path)
    return shortest

def solve(keys_to_press, keypad_coords, keypad):
    start = keypad_coords["A"]
    solution = []
    for target in list(keys_to_press):
        end = keypad_coords[target]
        mult = []
        for path in dijkstra(start, end, keypad):
            start = path[-1][0]
            mult.append(getpathstr(path))
        solution.append(mult)

    
    return ["".join(x) for x in list(product(*solution))]

def getpathstr(path):
    pathstr = ""
    for p in path:
        pathstr += p[1]
    return pathstr +"A"

def main():
    # <A ^A >^^A vvvA
    # <A ^A ^>^A vvvA
    # <A ^A ^^>A vvvA
    
    total = 0
    for line in ["029A"]:
        robot1 = solve(line, keypad_coords, keypad)
        print(robot1)
        return
        next = robot1
        for _ in range(2):
            possible_next = []
            for seq in next:
                possible_next += solve(seq, dir_pad_coords, dirpad)
            minlen = min(map(len, possible_next))
            next = [seq for seq in possible_next if len(seq) == minlen]

        total += len(next[0]) * int(line[:-1]) 
    print(total)

if __name__ == "__main__":
    main()
