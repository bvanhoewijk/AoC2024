def part1(data):
    safe = 0
    for item in data:
        increasing = all((i < j and abs(j - i) < 4) for i, j in zip(item, item[1:]))
        decreasing = all((i > j and abs(j - i) < 4) for i, j in zip(item, item[1:]))
        safe += increasing or decreasing
    print("Part1", safe)


def part2(data):
    all_safe = 0
    for item in data:
        increasing = all((i < j and abs(j - i) < 4) for i, j in zip(item, item[1:]))
        decreasing = all((i > j and abs(j - i) < 4) for i, j in zip(item, item[1:]))

        safe = False
        if not (increasing or decreasing):
            for i in range(len(item)):
                item2 = item.copy()
                del item2[i]
                increasing = all(
                    (i < j and abs(j - i) < 4) for i, j in zip(item2, item2[1:])
                )
                decreasing = all(
                    (i > j and abs(j - i) < 4) for i, j in zip(item2, item2[1:])
                )
                if increasing or decreasing:
                    safe = True
        else:
            safe = True

        all_safe += safe

    print("Part2", all_safe)


if __name__ == "__main__":
    lines = open("big.txt", "r").readlines()
    data = [[int(y) for y in x.strip().split(" ")] for x in lines]

    part1(data)
    part2(data)
