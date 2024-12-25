def main():
    dataset = "".join(open("big.txt").readlines()).split("\n\n")

    keys, locks = list(), list()
    for pattern in dataset:
        pattern = "".join(pattern.split("\n"))
        heights = set()
        lock = pattern[0] == "#"

        for r in range(len(pattern)):
            if pattern[r] == "#":
                heights.add((r))
        if lock:
            locks.append(heights)
        else:
            keys.append(heights)

    solution = 0
    for lock in locks:
        for key in keys:
            solution += (len(lock & key) == 0)
    print("Part 1", solution)
    # 3201


if __name__ == "__main__":
    main()
