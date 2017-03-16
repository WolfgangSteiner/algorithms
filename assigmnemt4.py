import random
import math
import copy

class edge(object):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __eq__(self, other):
        return self.n1 == other.n1 and self.n2 == other.n2


    def contains(self, n):
        return self.n1 == n or self.n2 == n


    def update_node(self, n1, n2):
        if self.n1 == n2:
            self.n1 = n1
        elif self.n2 == n2:
            self.n2 = n1


    def is_edge_between_nodes(self, n1, n2):
        return self.contains(n1) and self.contains(n2)


    def is_loop(self):
        return self.n1 == self.n2


def parse_node(s):
    l = map(lambda x: int(x), s.split())
    n = l.pop(0)
    return n,l


def read_adjacency_list():
    with open("kargerMinCut.txt") as f:
    #with open("test_case_a4.txt") as f:
        adjacency_list = {}
        for n,l in [parse_node(i) for i in f.readlines()]:
            adjacency_list[n] = l

    return adjacency_list


def build_edge_list(adjacency_list):
    result = []
    for n1,l in adjacency_list.iteritems():
        for n2 in l:
            result.append(edge(n1,n2))

    return result


def build_node_aliases(adjacency_list):
    result = {}
    for k in adjacency_list:
        result[k] = k

    return result


def update_edge_list(edge_list, n1, n2):
    for e in edge_list:
        if e.contains(n2):
            e.update_node(n1,n2)

    edge_list[:] = (e for e in edge_list if not e.is_loop())

    return edge_list


def update_edge_list_slow(edge_list, n1, n2):
    l = []

    for e in edge_list:
        en1,en2 = e.n1,e.n2

        if en1 == n2:
            en1 = n1

        if en2 == n2:
            en2 = n1


        if en1 != en2:
            l.append(edge(en1,en2))

    return l


def find_cut(adjacency_list, edge_list):
#    el = copy.deepcopy(edge_list)
    el = build_edge_list(adjacency_list)
    for _ in range(len(adjacency_list) - 2):
        e = random.choice(el)
        el = update_edge_list(el, e.n1, e.n2)
    return len(el) // 2


def min_cut(adjacency_list, edge_list):
    min_edges = 1e9
    num_nodes = len(adjacency_list)
    n_iter = int(num_nodes*num_nodes*math.log(num_nodes))

    for i in range(n_iter):
        num_edges = find_cut(adjacency_list, edge_list)
        min_edges = min(min_edges, num_edges)
        if i % 1 == 0:
            print("%d/%d: %d" % (i,n_iter, min_edges))

    return min_edges


if __name__ == "__main__":
    adjacency_list = read_adjacency_list()
    edge_list = build_edge_list(adjacency_list)
    node_aliases = build_node_aliases(adjacency_list)
    print(min_cut(adjacency_list, edge_list))
