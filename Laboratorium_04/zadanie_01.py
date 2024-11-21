
from collections import deque


class DisjointSet:
	_disjoint_set = list()

	def __init__(self, init_arr):
		self._disjoint_set = []
		if init_arr:
			for item in list(set(init_arr)):
				self._disjoint_set.append([item])

	def _find_index(self, elem):
		for item in self._disjoint_set:
			if elem in item:
				return self._disjoint_set.index(item)
		return None

	def find(self, elem):
		for item in self._disjoint_set:
			if elem in item:
				return self._disjoint_set[self._disjoint_set.index(item)]
		return None
	
	def union(self,elem1, elem2):
		index_elem1 = self._find_index(elem1)
		index_elem2 = self._find_index(elem2)
		if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
			self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2]+self._disjoint_set[index_elem1]
			del self._disjoint_set[index_elem1]
		return self._disjoint_set
		
	def get(self):
		return self._disjoint_set


def bfs(graph, start, ds):
    visited = set()  
    queue = deque([start])  
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(f"Visiting node: {node}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                # Łączenie wierzchołków w tym samym zbiorze
                ds.union(node, neighbor)

    print("Current disjoint sets after BFS:")
    print(ds.get())



if __name__ == "__main__":
    graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
    4: [5],
    5: [4]
    }
    ds = DisjointSet([0, 1, 2, 3, 4, 5])

    bfs(graph, 0, ds)

    print("Final Disjoint Sets:")
    print(ds.get())