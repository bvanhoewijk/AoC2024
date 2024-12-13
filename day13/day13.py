import re

import sympy
from sympy import Eq, solve, symbols
from sympy.core.numbers import Integer


def part1(dataset):
    A, B = symbols("A,B")

    tokens = 0
    for equation in dataset:
        eq1 = Eq((equation["A"][0] * A + equation["B"][0] * B), equation["price"][0])
        eq2 = Eq((equation["A"][1] * A + equation["B"][1] * B), equation["price"][1])

        solution = solve((eq1, eq2), (A, B))
        if isinstance(solution[A], Integer) and isinstance(solution[B], Integer):
            if solution[A] <= 100 and solution[B] <= 100:
                tokens += solution[A] * 3 + solution[B] * 1
    print(tokens)


def part2(dataset):
    A, B = symbols("A,B")

    tokens = 0
    for equation in dataset:
        eq1 = Eq(
            (equation["A"][0] * A + equation["B"][0] * B),
            equation["price"][0] + 10000000000000,
        )
        eq2 = Eq(
            (equation["A"][1] * A + equation["B"][1] * B),
            equation["price"][1] + 10000000000000,
        )

        solution = solve((eq1, eq2), (A, B))
        if isinstance(solution[A], Integer) and isinstance(solution[B], Integer):
            tokens += solution[A] * 3 + solution[B] * 1
    print(tokens)


def parse_file(file):
    res = []
    dataset = "".join(open(file).readlines()).split("\n\n")
    for machine in dataset:
        button_a, button_b, price = machine.split("\n")
        button_a = [
            int(re.findall("\\d+", item)[0]) for item in button_a.split(" ")[2:]
        ]
        button_b = [
            int(re.findall("\\d+", item)[0]) for item in button_b.split(" ")[2:]
        ]
        price = [int(re.findall("\\d+", item)[0]) for item in price.split(" ")[1:]]

        res.append({"A": button_a, "B": button_b, "price": price})
    return res


if __name__ == "__main__":
    dataset = parse_file("big.txt")
    part1(dataset)
    part2(dataset)
