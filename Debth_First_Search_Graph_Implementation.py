class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * size for i in range(size)]
        self.vertex_data = [""] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacent Matrix: ")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

        print("\nVertex Data: ")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex:} {data}")

    def dfs_util(self, start_vertex_data, visited):
        visited[start_vertex_data] = True
        print(self.vertex_data[start_vertex_data], end=" ")

        for neighbour in range(self.size):
            if self.adj_matrix[start_vertex_data][neighbour] == 1 and not visited[neighbour]:
                self.dfs_util(neighbour, visited)

    def dfs(self, start_vertex_data):
        print("Depth First Search from D: ")
        start_vertex = self.vertex_data.index(start_vertex_data)
        visited = [False] * self.size
        self.dfs_util(start_vertex, visited)



g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

g.dfs('D')
