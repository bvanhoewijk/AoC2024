import itertools
import math
from pprint import pprint


def part1(dataset):
    dataset_size = (len(dataset), len(dataset[0]))

    all_nodes = find_nodes(dataset)

    unique_new_nodes = set()
    for tower in all_nodes:
        nodes = all_nodes[tower]
        for node1, node2 in itertools.combinations(nodes, 2):
            diff_r = node1[0] - node2[0]
            diff_c = node1[1] - node2[1]

            new_node1 = (node1[0] + diff_r, node1[1] + diff_c)
            new_node2 = (node2[0] - diff_r, node2[1] - diff_c)

            if in_bounds(new_node1, dataset_size):
                unique_new_nodes.add(new_node1)
            if in_bounds(new_node2, dataset_size):
                unique_new_nodes.add(new_node2)

    print("Part 1", len(unique_new_nodes))


def part2(dataset):
    dataset_size = (len(dataset), len(dataset[0]))

    all_nodes = find_nodes(dataset)

    unique_new_nodes = set()
    for tower in all_nodes:
        nodes = all_nodes[tower]
        for node1, node2 in itertools.combinations(nodes, 2):
            unique_new_nodes.add(node1)
            unique_new_nodes.add(node2)
            diff_r = node1[0] - node2[0]
            diff_c = node1[1] - node2[1]

            new_node1 = (node1[0] + diff_r, node1[1] + diff_c)
            new_node2 = (node2[0] - diff_r, node2[1] - diff_c)

            while in_bounds(new_node1, dataset_size):
                unique_new_nodes.add(new_node1)
                new_node1 = (new_node1[0] + diff_r, new_node1[1] + diff_c)
            while in_bounds(new_node2, dataset_size):
                unique_new_nodes.add(new_node2)
                new_node2 = (new_node2[0] - diff_r, new_node2[1] - diff_c)

    print("Part 2", len(unique_new_nodes))


def in_bounds(next_node, dataset_size):
    if next_node[0] < 0 or next_node[1] < 0:
        return False
    if next_node[0] >= dataset_size[0]:
        return False
    if next_node[1] >= dataset_size[1]:
        return False
    return True


def find_nodes(dataset):
    nodes = {}
    for r, row in enumerate(dataset):
        for c, col in enumerate(dataset[0]):
            if dataset[r][c] != ".":
                if dataset[r][c] in nodes:
                    nodes[dataset[r][c]].append((r, c))
                else:
                    nodes[dataset[r][c]] = [(r, c)]
    return nodes


if __name__ == "__main__":
    dataset = [list(line.strip()) for line in open("big.txt", "r").readlines()]
    part1(dataset)
    part2(dataset)
