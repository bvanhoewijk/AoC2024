from pprint import pprint


def part2(dataset):
    pass

dirs = [
    (-1, 0), # Forward ^
    (0, 1),  # Right   >
    (1, 0),  # Down    v
    (0, -1), # Left    <
]  


def part1(dataset):
    pass

def print_grid(walls, boxes, robot, size):
    for r in range(size[0]):
        for c in range(size[1]):
            pos = (r, c)
            if pos in walls:
                print('#', end='')
            elif pos in boxes:
                print('O', end='')
            elif pos == robot:
                print('@', end='')
            else:
                print('.', end='')
        print()
    print()
def print_grid2(walls, lboxes, rboxes, robot, size):
    for r in range(size[0]):
        for c in range(size[1]):
            pos = (r, c)
            if pos in walls:
                print('#', end='')
            elif pos in lboxes:
                print('[', end='')
            elif pos in rboxes:
                print(']', end='')
            elif pos == robot:
                print('@', end='')
            else:
                print('.', end='')
        print()
    print()

def load_dataset_part1(file):
    grid, moves = "".join(open(file, "r").readlines()).split("\n\n")
    grid = [list(row.strip()) for row in grid.split("\n")]
    moves = "".join(moves.split("\n"))
    return grid, moves

def load_dataset_part2(file):
    grid, moves = "".join(open(file, "r").readlines()).split("\n\n")
    replacement = {"#" : "##", "O" : "[]", "." : "..", "@" : "@."}
    grid = [list("".join([replacement[item] for item in list(row.strip())])) for row in grid.split("\n")]
    
    moves = "".join(moves.split("\n"))
    return grid, moves

def part1(file):
    grid, moves =load_dataset_part1(file)
    walls = set()
    boxes = set()
    robot = ()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                walls.add((r,c))
            if grid[r][c] == "O":
                boxes.add((r,c))
            if grid[r][c] == "@":
                robot = (r,c)

    dirs = dict(zip(["^", "v", "<", ">"], [(-1, 0), (1, 0), (0,-1), (0,1)]))
    print_grid(walls, boxes, robot, (len(grid), len(grid[0])))

    for move in moves:
        nr, nc = dirs[move]
        pos = (robot[0] + nr, robot[1] + nc)
        if pos in boxes:
            to_move = []
            while pos in boxes:
                to_move.append(pos)
                pos = (pos[0] + nr, pos[1] + nc)
            if pos not in walls:
                robot = robot[0] + nr, robot[1] + nc
                for i, box in enumerate(to_move):
                    boxes.remove(box)
                    to_move[i] = (box[0]+nr, box[1]+ nc)
                for box in to_move:
                    boxes.add(box)
        elif pos not in walls:
            robot = pos
    solution = sum([100 * x[0] + x[1] for x in boxes])
    print_grid(walls, boxes, robot, (len(grid), len(grid[0])))
    print(solution)


if __name__ == "__main__":
    # part1("big.txt")
    # part2("small.txt")
    grid, moves = load_dataset_part2("small4.txt")

    walls = set()
    boxes = set()
    lboxes = set()
    rboxes = set()
    robot = ()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                walls.add((r,c))
            if grid[r][c] == "[":
                boxes.add((r,c))
                lboxes.add((r,c))
            if grid[r][c] == "]":
                boxes.add((r,c))
                rboxes.add((r,c))
            if grid[r][c] == "@":
                robot = (r,c)

    dirs = dict(zip(["^", "v", "<", ">"], [(-1, 0), (1, 0), (0,-1), (0,1)]))
    print_grid(walls, boxes, robot, (len(grid), len(grid[0])))

    for move in moves:
        nr, nc = dirs[move]
        pos = (robot[0] + nr, robot[1] + nc)
        if pos in lboxes or pos in rboxes:
            to_move = []
            while pos in lboxes | rboxes:
                to_move.append(pos)
                pos = (pos[0] + nr, pos[1] + nc)
            if pos not in walls:
                robot = robot[0] + nr, robot[1] + nc
                for i, box in enumerate(to_move):
                    boxes.remove(box)
                    to_move[i] = (box[0]+nr, box[1]+ nc)
                for box in to_move:
                    boxes.add(box)
        elif pos not in walls:
            robot = pos
        print_grid2(walls, lboxes, rboxes, robot, (len(grid), len(grid[0])))
    # solution = sum([100 * x[0] + x[1] for x in boxes])
    # print(solultion)