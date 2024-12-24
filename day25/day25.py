def main():
    dataset = "".join(open("big.txt").readlines()).split("\n\n")

    keys, locks = list(), list()
    for pattern in dataset:
        pattern = pattern.split("\n")
        heights = [-1] * 5
        lock = pattern[0] == "#####"

        for row in pattern:
            for i, pin in enumerate(row):
                if pin == "#":
                    heights[i] += 1
        if lock:
            locks.append(heights)
        else:
            keys.append(heights)

    solution = 0
    for lock in locks:
        for key in keys:
            solution += all([x + y <= 5 for x, y in zip(lock, key)])
    print("Part 1", solution)
    # 3201


if __name__ == "__main__":
    main()
