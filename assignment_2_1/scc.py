from collections import namedtuple,defaultdict
Globals = namedtuple("Globals", "t,s,explored_vertices")
Node = namedtuple("Node", "finishing_time,leader")

def parse_edge_list(edge_list):
    adjacency_list = {}
    adjacency_list_transposed = {}

    for v1,v2 in edge_list:
        if not v1 in adjacency_list:
            adjacency_list[v1] = []
        adjacency_list[v1].append(v2)

        if not v2 in adjacency_list_transposed:
            adjacency_list_transposed[v2] = []
        adjacency_list_transposed[v2].append(v1)

    return adjacency_list, adjacency_list_transposed



def find_connected_components(edge_list):
    adjacency_list, adjacency_list_transposed = parse_edge_list(edge_list)
    finished_nodes = dfs_loop_a(adjacency_list)
    visited_nodes = dfs_loop_b(adjacency_list_transposed, finished_nodes)
    node_counts = defaultdict(int)
    for v,leader in visited_nodes.items():
        node_counts[leader] += 1

    result = sorted(node_counts.values(), reverse=True)
    while(len(result) < 5):
        result.append(0)

    return result[0:5]



def dfs_loop_a(adjacency_list):
    finished_nodes = []
    visited_nodes = set()

    for n_i in adjacency_list.keys():
        if not n_i in visited_nodes:
            dfs_a(adjacency_list, n_i, visited_nodes, finished_nodes)

    return finished_nodes


def dfs_a(adjacency_list, n_i, visited_nodes, finished_nodes):
    stack = [n_i]

    while len(stack):
        v = stack.pop(-1)
        if v in visited_nodes:
            continue
        stack.extend(adjacency_list[v])

        finished_nodes.append(v)
        visited_nodes.add(v)


def dfs_loop_b(adjacency_list, finished_nodes):
    visited_nodes = {}
    for n_i in reversed(finished_nodes):
        if not n_i in visited_nodes:
            leader = n_i
            dfs_b(adjacency_list, n_i, visited_nodes)


    return visited_nodes


def dfs_b(adjacency_list, leader, visited_nodes):
    stack = [leader]
    while len(stack):
        v = stack.pop(-1)
        if v in visited_nodes:
            continue
        stack.extend(adjacency_list[v])
        visited_nodes[v] = leader

    return visited_nodes


if __name__ == "__main__":
    with open("test_cases.txt") as f:
        test_cases = []
        edge_list = []
        for l in f.readlines():
            l = l.rstrip()
            if len(l) == 0 or l.startswith("==="):
                continue
            elif l.startswith("Answer:"):
                answer = [int(n) for n in l.split(" ")[1].split(",")]
                test_cases.append((list(edge_list), answer))
                edge_list = []
            else:
                edge_list.append([int(n) for n in l.split(' ')])

    for edge_list,answer in test_cases:
        result = find_connected_components(edge_list)
        print(result, answer)
        #assert result == answer