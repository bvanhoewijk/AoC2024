def part1(dataset):
    res = []
    id = 0
    for i, item in enumerate(dataset):
        if (i+1) % 2 == 0:
            for _ in range(item):
                res.append(".")
        else:
            for _ in range(item):
                res.append(id)
            id += 1

    for i, item in enumerate(res):
        if item == ".":
            last = res.pop()
            while last == ".":
                last = res.pop()
            res[i] = last

    result = 0
    for i, item in enumerate(res):
        result += i * item
    print("Part1",result)

    


def part2(dataset):
    pass

if __name__ == "__main__":
    dataset = [list(map(int, list(line))) for line in open("big.txt", "r").readlines()][0]
    part1(dataset)
    # part1(list(map(int, list("2333133121414131402"))))
    # part1(list(map(int, list("2333133121414131402"))))
