class GraphEdgeList:
    def __init__(self) -> None:
        self.edges = []

    def add_edge(self, i, j):
        if (i, j) not in self.edges and (j, i) not in self.edges:
            self.edges.append((i, j))

    def remove_edge(self, i, j):
        if (i, j) in self.edges:
            self.edges.remove((i, j))
        elif (j, i) in self.edges:
            self.edges.remove((j, i))
        else:
            print("Nie ma krawedzi")

    def display(self):
        print(self.edges)
        
obj = GraphEdgeList()

obj.add_edge(1, 2)
obj.add_edge(2, 3)

obj.display()
obj.remove_edge(3, 2)
obj.display()