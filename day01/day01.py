from collections import Counter

def part1(lines):
    left = []
    right = []
    for l, r in lines:
        left.append(int(l))
        right.append(int(r))

    left = sorted(left)
    right= sorted(right)

    diff = 0
    for l,r in zip(left, right):
        diff += abs(l-r)

    print("Result Part1: ", diff)

def part2(lines):
    left = []
    right = []
    for l, r in lines:
        left.append(int(l))
        right.append(int(r))

    occ = Counter(right)
    simscore = 0
    for x in left:
        if x in occ:
            simscore += x * occ[x]
    print("Result Part2: ", simscore)

if __name__ == "__main__":
    lines = open("big.txt", 'r').readlines()
    lines = [x.strip().split("  ") for x in lines]
    part1(lines)
    part2(lines)
