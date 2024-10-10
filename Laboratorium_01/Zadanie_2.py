class GraphicMatrix:
    def __init__(self):
        self.neighbour = []
    
    def add_edge(self, i):
        return self.neighbour.append(i)
    
    def remove_edge(self, i):
        return self.neighbour.remove(i)

    def display(self):
        print(self.neighbour)

n1 = GraphicMatrix()
n2 = GraphicMatrix()

n1.add_edge(n2)
n1.display()
