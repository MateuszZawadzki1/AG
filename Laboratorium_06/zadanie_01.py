import itertools

# TODO: ADD BRUTEFORCE ALGH  AND Nearest neighbour algorithm

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def is_hamiltonian_cycle(self, cycle):
        for i in range(len(cycle)):
            if cycle[i] not in self.edges[cycle[(i+1) % len(cycle)]]:
                return False
        return True

def generate_hamiltonian_cycle(graph):
    for cycle in itertools.permutations(graph.vertices):
        if graph.is_hamiltonian_cycle(cycle):
            return cycle
    return None

vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)

for u, v in itertools.combinations(vertices, 2):
    graph.add_edge(u, v)

cycle = generate_hamiltonian_cycle(graph)
print("Hamiltonian cycle:", cycle)
