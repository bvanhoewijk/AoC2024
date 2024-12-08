import itertools


def part1(page_update_numbers, rules):
    comparison = {}
    for x, y in rules:
        comparison[(x, y)] = True
        comparison[(y, x)] = False

    result = 0
    for update in page_update_numbers:
        if is_ordered(update, comparison):
            index = len(update) // 2
            result += update[index]

    print("Part1", result)


def part2(page_update_numbers, rules):
    comparison = {}
    for x, y in rules:
        comparison[(x, y)] = True
        comparison[(y, x)] = False

    result = 0
    for update in page_update_numbers:
        if not is_ordered(update, comparison):
            while not is_ordered(update, comparison):
                update = flip(update, comparison)
            index = len(update) // 2
            result += update[index]
    print("Part2", result)


def flip(update, comparison):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in comparison and not comparison[key]:
                # Flip if the numbers are not in the correct order
                # I think this is bubble sort?
                update[i], update[j] = update[j], update[i]
    return update


def is_ordered(update, comparison):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in comparison and not comparison[key]:
                return False
    return True


if __name__ == "__main__":
    rules, page_update_numbers = "".join(
        line for line in open("big.txt", "r").readlines()
    ).split("\n\n")

    rules = [[int(y) for y in x.split("|")] for x in rules.split("\n")]
    page_update_numbers = [
        [int(y) for y in x.split(",")] for x in page_update_numbers.split("\n")
    ]

    part1(page_update_numbers, rules)
    part2(page_update_numbers, rules)
