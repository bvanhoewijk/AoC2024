import re
from itertools import product

from tqdm import tqdm


def part1(dataset):
    total_good = 0
    for item in dataset:
        target = item[0]
        numbers = item[1:]

        good = 0
        list_combinations = list(product("*+", repeat=len(numbers) - 1))
        for combo in list(list_combinations):
            evalstr = str(numbers[0])
            for i in range(1, len(numbers)):
                evalstr += combo[i - 1] + str(numbers[i])
                evalstr = str(eval(evalstr))
            if eval(evalstr) == target:
                good = eval(evalstr)
        total_good += good
    print("Result part1:", total_good)


def part2(dataset):
    total_good = 0
    for j, item in tqdm(enumerate(dataset), total=len(dataset)):
        target = item[0]
        numbers = item[1:]

        good = 0
        list_combinations = list(product("*+|", repeat=len(numbers) - 1))
        for combo in list(list_combinations):
            evalstr = str(numbers[0])
            for i in range(1, len(numbers)):
                op = combo[i - 1]
                if op == "|":
                    op = ""
                evalstr += op + str(numbers[i])
                evalint = eval(evalstr)
                # Minor speed increase:
                if evalint > target:
                    break
                evalstr = str(evalint)
            evalint = eval(evalstr)
            # Minor speed increase:
            if evalint == target:
                good = evalint
                break
        total_good += good
    print("Result part2", total_good)


if __name__ == "__main__":
    dataset = [
        list(map(int, re.split(": |\\s+", line.strip())))
        for line in open("big.txt", "r").readlines()
    ]
    part1(dataset)
    part2(dataset)
