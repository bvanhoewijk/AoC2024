import re


def part1(data):
    res = 0
    for x in re.finditer(r"mul\((\d+),(\d+)\)", data):
        res += int(x.group(1)) * int(x.group(2))
    return res


def part2(data):
    res = 0
    do = True
    for x in re.finditer(r"(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)", data):
        if x.group(0) == "don't()":
            do = False
        elif x.group(0) == "do()":
            do = True
        elif do:
            res += int(x.groups()[2]) * int(x.groups()[3])
    return res


if __name__ == "__main__":
    lines = open("big.txt", "r").readlines()
    lines = "".join(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
