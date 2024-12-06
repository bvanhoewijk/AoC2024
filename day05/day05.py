def part1(dataset):
    pass

def part2(dataset):
    pass

if __name__ == "__main__":
    page_ordering_rules, page_update_numbers = "".join(line for line in open("small.txt", "r").readlines()).split("\n\n")
    page_ordering_rules = [[int(y) for y in x.split("|")] for x in page_ordering_rules.split("\n")]
    page_update_numbers = [[int(y) for y in x.split(",")] for x in page_update_numbers.split("\n")]
    # print(input_part1)
    # print(page_update_numbers)
    # part1(dataset)
    # part2(dataset)

    # Check the first update:
    print(page_update_numbers[0])
    for rule in page_ordering_rules:
        print(rule)


