import re

import sympy
from sympy import Eq, solve, symbols
from sympy.core.numbers import Integer
import numpy as np

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


def part1_np(dataset):
    tokens = 0
    for equation in dataset:
        a = np.array([[equation['A'][0], equation['B'][0]],[equation['A'][1], equation['B'][1]]])
        b = np.array([equation['price'][0], equation['price'][1]])

        res1, res2 = np.linalg.solve(a,b)
        res1 = int(res1)
        res2 = int(res2)
        
        check1 = (res1 * a[0][0] + res2 * a[0][1] == b[0])
        check2 = (res1 * a[1][0] + res2 * a[1][1] == b[1])
        if not (check1 and check2):
            continue

        if res1 <= 100 and res2 <= 100:
            tokens += res1 * 3 + res2 * 1
    print(tokens)

def part2_np(dataset):
    tokens = 0
    for equation in dataset:
        a = np.array([[equation['A'][0], equation['B'][0]],[equation['A'][1], equation['B'][1]]])
        b = np.array([equation['price'][0], equation['price'][1]])

        res1, res2 = np.linalg.solve(a,b)
        res1 = int(res1)
        res2 = int(res2)
        
        check1 = (res1 * a[0][0] + res2 * a[0][1] == b[0])
        check2 = (res1 * a[1][0] + res2 * a[1][1] == b[1])
        
        if res1 <= 100 and res2 <= 100 and check1 and check2:
            tokens += res1 * 3 + res2 * 1
    print(tokens)


if __name__ == "__main__":
    dataset = parse_file("small.txt")
    part1_np(dataset)
    # part2(dataset)
    # import numpy as np
    # # a = np.array([[94, 22], [34, 67]])
    # # b = np.array([8400, 5400])
    # a = np.array([[26, 67], [34, 67]])
    # b = np.array([8400, 5400])

    # print(np.linalg.solve(a,b))