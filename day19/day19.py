if __name__ == "__main__":
    patterns, designs = "".join(open("big.txt", "r").readlines()).split("\n\n")
    patterns = [x.strip() for x in patterns.split(",")]
    designs = designs.split("\n")

    from functools import cache

    @cache
    def find_patterns(design, start=0):
        if start == len(design):
            return 1

        # Find all solutions:
        result = 0
        for pattern in patterns:
            if design[start : start + len(pattern)] == pattern:
                result += find_patterns(design, start + len(pattern))
        return result

    solution = 0
    for d in designs:
        solution += find_patterns(d, 0) > 0
    print("Part 1: ", solution)

    solution = 0
    for d in designs:
        solution += find_patterns(d, 0)
    print("Part 2: ", solution)
