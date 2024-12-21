def part1(dataset):
    pass

def part2(dataset):
    pass

dirs = [
    (-1, 0),  # Forward ^
    (1, 0),  # Down    v
    (0, 1),  # Right   >
    (0, -1),  # Left    <
]

def in_bounds(next_node, dataset_size):
    rows = next_node[0]
    cols = next_node[1]
    width = dataset_size[0]
    height = dataset_size[1]
    return 0 <= cols < width and 0 <= rows < height

def dijkstra(start, end, key_pad):
    dsize = (len(key_pad[0]), len(key_pad))
    dirs_dict = dict(zip(dirs, list("^v><")))

    visited = set(start)
    path = []
    queue = []

    queue.append((start, [], 0))

    all_paths = []
    while queue:
        if len(queue) > 1:
            queue = sorted(queue, key=lambda x: x[2], reverse=False)
        current, path, cost = queue.pop(0)
        r, c = current
        visited.add(current)
        for dir in dirs:
            next_dir = (r + dir[0], c + dir[1])
            symbol = dirs_dict[(dir[0], dir[1])]
            if (next_dir) == end:
                all_paths.append(path + [(next_dir, symbol, cost+1)])
            elif in_bounds(next_dir, dsize) and next_dir not in visited:
                key_pad_value = key_pad[next_dir[0]][next_dir[1]]
                if key_pad_value != "G":
                    key_pad_value = key_pad[next_dir[0]][next_dir[1]]
                    new_path = path + [(next_dir, symbol, cost+1)]
                    queue.append((next_dir, new_path, cost+1))
    
    shortest = all_paths[0]
    for path in all_paths[1:]:
        if path[-1][2] < shortest[-1][2]:
            shortest = path
    return shortest

def keypad1(keys_to_press):
    keypad_coords = {"7" : (0,0), "8" : (0,1), "9" : (0,2),
                     "4" : (1,0), "5" : (1,1), "6" : (1,2),
                     "1" : (2,0), "2" : (2,1), "3" : (2,2),
                     "G" : (3,0), "0" : (3,1), "A" : (3,2)}

    keypad = [[7,8,9],
               [4,5,6],
               [1,2,3],
               ["G",0,"A"]]
    
    start = keypad_coords["A"]
    solution = []
    for target in list(keys_to_press):
        end = keypad_coords[target]
        path = dijkstra(start, end, keypad)
        for p in path:
            solution.append(p[1])
        solution.append("A")
        start = end
    return "".join(solution)

def keypad2(keys_to_press):
    keypad_coords = {"G" : (0,0), "^" : (0,1), "A" :  (0,2),
                     "<" : (1,0), "v" : (1,1), ">" :  (1,2)}

    keypad = [["G", "^", "A"],
              ["<" , "v", ">"]]
    
    start = keypad_coords["A"]
    solution = []
    for target in list(keys_to_press):
        end = keypad_coords[target]
        path = dijkstra(start, end, keypad)
        for p in path:
            solution.append(p[1])
        solution.append("A")
        start = end
    return "".join(solution)

def main():
    for input in ["029A"]:
        keypad1_result = keypad1(input)
        # Must be 28:
        keypad2_result = keypad2("<A^A>^^AvvvA")
        print(len(keypad2_result))
        keypad2_result = keypad2("<A^A^>^AvvvA")
        print(len(keypad2_result))
        keypad2_result = keypad2("<A^A^^>AvvvA")
        print(len(keypad2_result))
        # print(len(keypad2_result))
        # keypad2_result = keypad2("<A^A^>^AvvvA")
        # print(len(keypad2_result))
        # keypad2_result = keypad2("<A^A^^>AvvvA")
        # print(len(keypad2_result))
        # keypad3_result = keypad2(keypad2_result)
        # print(input, len(keypad3_result))
if __name__ == "__main__":
    main()
