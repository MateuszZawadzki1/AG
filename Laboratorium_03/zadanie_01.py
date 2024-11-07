graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

graph2 = {
    '1' : ['2', '4'],
    '2' : ['3', '5'],
    '4' : ['3'],
    '3' : ['5'],
    '5' : [],
    '6' : ['7'],
    '7' : []
}


class TopologicSort():
    def __init__(self):
        self.visited = set()
        self.topologic_list = [] 
        

    def dfs(self, graph, node):
        if node not in self.visited:
            self.visited.add(node)
            for neighbour in graph[node]:
                self.dfs(graph, neighbour)
            self.topologic_list.append(node)

    def process_all_nodes(self, graph):
        # Dla grafow bez powiazan
        for node in graph:
            if node not in self.visited:
                self.dfs(graph, node)

    def get_topologi_list(self):
        self.topologic_list.reverse()
        return self.topologic_list

my_sort = TopologicSort()
my_sort.dfs(graph, "5")
print(my_sort.get_topologi_list())

my_sort2 = TopologicSort()
my_sort2.process_all_nodes(graph2)
print(my_sort2.get_topologi_list())

