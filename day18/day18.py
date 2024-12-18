import math
from queue import Queue

def part1(dataset):
    pass


def part2(dataset):
    pass


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


def print_grid(grid_cols, grid_rows, occupied, path):
    for col in range(grid_cols):
        for row in range(grid_rows):
            if (row, col) in occupied:
                print("#", end="")
            elif (row, col) in path:
                print("O", end="")
            else:
                print(".", end="")
        print()
    print()

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def bfs(start, end, occupied, grid_cols, grid_rows):
    visited = set(start)
    queue = Queue()
    queue.put((start, 0))

    while not queue.empty():
        current, cost = queue.get()
        r, c = current
        for dr, dc in dirs:
            next_dir = (r + dr, c + dc)
            if not in_bounds(next_dir, (grid_rows, grid_cols)) or next_dir in occupied or next_dir in visited:
                continue
            if next_dir == end:
                return cost + 1
            else:
                visited.add(next_dir)
                queue.put((next_dir, cost+1))
        
def main():
    # Small:
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("small.txt", "r").readlines()
    ]
    start = (0, 0)
    end = (6, 6)
    memory_space = (6, 6)
    cost = bfs(start, end, occupied[:12], memory_space[0]+1, memory_space[1]+1)
    # print_grid(memory_space[0]+1, memory_space[1]+1, occupied=occupied[:12], path=path)
    print(cost)
    # # Big:
    occupied = [
        tuple(map(int, item.strip().split(",")))
        for item in open("big.txt", "r").readlines()
    ]
    start = (0, 0)
    end = (70, 70)
    memory_space = (70, 70)
    # 1108 is too high
    # 285 incorrect
    # 320 incorrect
    # 268?
    cost = bfs(start, end, occupied[:1024], memory_space[0]+1, memory_space[1]+1)
    print(cost)

if __name__ == "__main__":
    main()
