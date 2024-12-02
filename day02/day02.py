def part1(data):
    safe = 0
    for item in data:
        safe += check_increasing_decreasing(item)
    print("Part1", safe)

def check_increasing_decreasing(the_list):
    increasing = all((i < j and abs(j - i) < 4) for i, j in zip(the_list, the_list[1:]))
    decreasing = all((i > j and abs(j - i) < 4) for i, j in zip(the_list, the_list[1:]))
    
    return increasing or decreasing

def part2(data):
    all_safe = 0
    for item in data:
        safe = False
        check = check_increasing_decreasing(item)
        if not check:
            for i in range(len(item)):
                item2 = item.copy()
                del item2[i]
                check = check_increasing_decreasing(item2)
                if check:
                    safe = True
                    break
        else:
            safe = True

        all_safe += safe

    print("Part2", all_safe)


if __name__ == "__main__":
    lines = open("big.txt", "r").readlines()
    data = [[int(y) for y in x.strip().split(" ")] for x in lines]

    part1(data)
    part2(data)
