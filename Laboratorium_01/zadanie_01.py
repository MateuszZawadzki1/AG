class GraphicMatrix:
    def __init__(self):
        self.neighbour = []
    
    def add_edge(self, i):
        self.neighbour.append(i)
        if  self not in i.neighbour:
            i.add_edge(self)
    
    def remove_edge(self, i):
        self.neighbour.remove(i)
        if self in i.neighbour:
            i.remove_edge(self)

    def display(self):
        print(self.neighbour)

n1 = GraphicMatrix()
n2 = GraphicMatrix()

n1.add_edge(n2)
n1.display()
n2.display()
