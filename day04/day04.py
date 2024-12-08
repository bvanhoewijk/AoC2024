import sys
from pprint import pprint


def in_bounds(next_node, dataset_size):
    if next_node[0] < 0 or next_node[1] < 0:
        return False
    if next_node[0] >= dataset_size[0]:
        return False
    if next_node[1] >= dataset_size[1]:
        return False
    return True


def part1(dataset):
    dataset_size = (len(dataset), len(dataset[0]))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    count = 0
    for x, _ in enumerate(dataset):
        for y, _ in enumerate(dataset[0]):
            # If X is found find the other letters
            if dataset[x][y] == "X":
                for d in directions:
                    if not in_bounds((x + d[0] * 3, y + d[1] * 3), dataset_size):
                        continue
                    xmas = "".join(
                        [
                            dataset[x][y],
                            dataset[x + d[0] * 1][y + d[1] * 1],
                            dataset[x + d[0] * 2][y + d[1] * 2],
                            dataset[x + d[0] * 3][y + d[1] * 3],
                        ]
                    )
                    if xmas == "XMAS":
                        count += 1
    print(f"Part 1: {count}")


def part2(dataset):
    dataset_size = (len(dataset), len(dataset[0]))
    count = 0
    # Diagonals
    directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

    for x, _ in enumerate(dataset):
        for y, _ in enumerate(dataset[0]):
            # If A is found find the other letters
            if dataset[x][y] == "A":
                if all(
                    [in_bounds((x + d[0], y + d[1]), dataset_size) for d in directions]
                ):
                    diag1 = dataset[x - 1][y - 1] + "A" + dataset[x + 1][y + 1]
                    diag2 = dataset[x - 1][y + 1] + "A" + dataset[x + 1][y - 1]
                    if (diag1 == "MAS" or diag1 == "SAM") and (
                        diag2 == "MAS" or diag2 == "SAM"
                    ):
                        count += 1

    print(f"Part 2: {count}")


if __name__ == "__main__":
    dataset = [list(line.strip()) for line in open("big.txt", "r").readlines()]

    part1(dataset)
    part2(dataset)
