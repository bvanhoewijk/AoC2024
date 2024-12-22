import re
from collections import defaultdict
from pprint import pprint

import networkx as nx
from networkx.algorithms.clique import find_cliques_recursive


def find_cliques3(graph):
    cliques = set()
    for u in graph:
        for v in graph[u]:
            for w in graph[v]:
                if v in graph[u] and w in graph[u] and w in graph[v]:
                    cliques.add(tuple(sorted([u, v, w])))

    return cliques


if __name__ == "__main__":
    dataset = [
        re.findall(r"(..)-(..)", item)[0][0:2]
        for item in open("big.txt", "r").readlines()
    ]
    #######

    graph = defaultdict(set)
    for u, v in dataset:
        graph[u].add(v)
        graph[v].add(u)
    res = 0
    for item in find_cliques3(graph):
        res += any([node.startswith("t") for node in item])
    print("Part 1:", res)

    ###########

    G = nx.Graph()
    G.add_edges_from(dataset)
    res = find_cliques_recursive(G)
    max = []
    for c in res:
        if len(c) >= len(max):
            max = c
    print("Part 2:", ",".join(sorted(max)))
