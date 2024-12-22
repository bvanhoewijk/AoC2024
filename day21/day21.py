from functools import cache
from itertools import product

dirs = [
    (-1, 0), # Up      ^
    (1, 0),  # Down    v
    (0, 1),  # Right   >
    (0, -1), # Left    <
]
door_keypad = [["7", "8", "9"], 
               ["4", "5", "6"], 
               ["1", "2", "3"], 
               [None, "0", "A"]]

dir_keypad = [[None, "^", "A"],
              ["<",  "v",  ">"]]

def solve(keys_to_press, keypad):
    seqs = get_possibilities(keypad)
    options = [seqs[(x,y)] for x, y in zip("A" + keys_to_press, keys_to_press)]
    return ["".join(x) for x in list(product(*options))]


def get_possibilities(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[0])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r,c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            # BFS
            possibilities = []
            queue = [(pos[x], "")]
            optimal = 1000
            while queue:
                (r,c), moves = queue.pop(0)
                for nr, nc, nm in [(r-1, c, "^"), (r+1, c, "v"), (r, c-1, "<"), (r, c+1, ">")]:
                    if nr < 0 or nc <0 or nr >= len(keypad) or nc >= len(keypad[0]):
                        continue
                    if keypad[nr][nc] is None:
                        continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1:
                            break
                        optimal = len(moves) + 1
                        possibilities.append(moves+nm+"A")
                    else:
                        queue.append(((nr, nc), moves+nm))
                else:
                    continue
                break
            seqs[(x, y)] = possibilities
    return seqs

def compute_length(x, y, depth=2):
    if depth == 1:
        len(dir_seqs[(x, y)])

def main():
    # <A ^A >^^A vvvA
    # <A ^A ^>^A vvvA
    # <A ^A ^^>A vvvA
    
    total = 0
    # for line in ["029A"]:
    for line in open("big.txt").read().splitlines():
        robot1 = solve(line, door_keypad)
        next = robot1
        for _ in range(2):
            possible_next = []
            for seq in next:
                possible_next += solve(seq, dir_keypad)
            minlen = min(map(len, possible_next))
            next = [seq for seq in possible_next if len(seq) == minlen]
        total += len(next[0]) * int(line[:-1])
    print(total)

if __name__ == "__main__":
    main()
