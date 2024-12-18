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

def bfs(start, end, occupied, grid_cols, grid_rows):
    visited = set(start)
    queue = list()
    queue.append((start, 0))
    while queue:
        current, cost = queue.pop(0)
        r, c = current
        for dr, dc in dirs:
            next_dir = (r + dr, c + dc)
            if not in_bounds(next_dir, (grid_rows, grid_cols)) or next_dir in occupied or next_dir in visited:
                continue
            if next_dir == end:
                return cost + 1
            else:
                visited.add(next_dir)
                queue.append((next_dir, cost+1))
    return None

def part1():
    print("SMALL DATASET")
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("small.txt", "r").readlines()
    ]
    start = (0, 0)
    end = (6, 6)
    cost = bfs(start, end, occupied[:12], end[0]+1, end[1]+1)
    print(cost)
    
    ############################################################

    print("BIG DATASET")
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("big.txt", "r").readlines()
    ]
    start = (0, 0)
    end = (70, 70)
    # 268
    cost = bfs(start, end, occupied[:1024], end[0]+1, end[1]+1)
    print(cost)

def part2():
    print("SMALL DATASET")
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("small.txt", "r").readlines()
    ]
    start = (0, 0)
    end = (6, 6)
    occupied_sel = occupied[:12].copy()
    rest = occupied[12:].copy()

    for item in rest: 
        occupied_sel.append(item)   
        cost = bfs(start, end, occupied_sel,  end[0]+1, end[1]+1)
        if cost == None:
            print(item)
            break
        else:
            cost
    
    ############################################################

    print("BIG DATASET")
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("big.txt", "r").readlines()
    ]
    start = (0, 0)
    end = (70, 70)
    
    occupied_sel = occupied[:1024].copy()
    rest = occupied[1024:].copy()

    for item in tqdm(rest):
        occupied_sel.append(item)   
        cost = bfs(start, end, occupied_sel,  end[0]+1, end[1]+1)
        if cost == None:
            print("Part 2", item)
            break


def main():
    # 268
    part1()

    # 64,11
    part2()
  
  

if __name__ == "__main__":
    main()
