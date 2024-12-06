from pprint import pprint

all_directions = [(-1, 0), # Forward ^
                    ( 0, 1), # Right   >
                    ( 1, 0), # Down    v
                    ( 0,-1)] # Left    <

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
                return (r,c)
            
def part1(dataset, start):
    current = start
    all_directions = [(-1, 0), # Forward ^
                      ( 0, 1), # Right   >
                      ( 1, 0), # Down    v
                      ( 0,-1)] # Left    <
    dataset_size = (len(dataset), len(dataset[0]))

    turn = 0
    travelled = [start]
    while True:
        if turn == 4:
            turn = 0
        next_position = (current[0] + all_directions[turn][0], 
                         current[1] + all_directions[turn][1]) 
        if not in_bounds(next_position, dataset_size):
            break

        if dataset[next_position[0]][next_position[1]] == "#":
            turn += 1
        else:
            current = next_position
            travelled.append(current)
    
    for item in travelled:
        dataset[item[0]][item[1]] = "X"

    with open("output.txt", "w") as out:
        for row in dataset:
            out.write("".join(row) + "\n")

    return travelled



def do_loop(dataset, start):
    dataset_size = (len(dataset), len(dataset[0]))
    turn = 0
    current = start
    travelled = [start]

    already_visited = 0
    while True:
        next_position = (current[0] + all_directions[turn][0], 
                        current[1] + all_directions[turn][1]) 
        if not in_bounds(next_position, dataset_size):
            return False

        if dataset[next_position[0]][next_position[1]] == "#":
            turn += 1
            if turn == 4:
                turn = 0
        else:
            current = next_position
            travelled.append(current)

            if current in travelled:
                already_visited += 1

            if already_visited > 5:
                return set(sorted(travelled))
        
import copy
def part2(dataset, start, visited):

    loops = []
    # for item in [(6,3)]:
    for item in visited[1:]:
        dataset_mutant = copy.deepcopy(dataset)
        dataset_mutant[item[0]][item[1]] = "#"
        res = do_loop(dataset_mutant, start)
        if res:
            loops.append(res)
    print(len(list(map(list, set(map(lambda i: tuple(i), loops))))))

# 696 is too low
# 1861 is too high
if __name__ == "__main__":
    dataset = [list(line.strip()) for line in open("big.txt", "r").readlines()]
    start = find_start(dataset)

    visited = part1(dataset, start)
    print("Result part1", len(set(visited)))

    dataset = [list(line.strip()) for line in open("big.txt", "r").readlines()]
    visited = part2(dataset, start, visited)





