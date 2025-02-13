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
        print("\nAdjacency matrix: ")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

        print("\nVertex data: ")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex} : {data}")

    def isBipartite_dfs_util(self, startVertexData, colors):
       for neighbor in range(self.size):
           if self.adj_matrix[startVertexData][neighbor] == 1 and colors[neighbor] == -1:
               colors[neighbor] = 1 - colors[startVertexData]
               if not self.isBipartite_dfs_util(neighbor, colors):
                   return False
           elif colors[startVertexData] == colors[neighbor]:
               return False

       return True

    def isBipartite_dfs(self, startVertexData):
        startVertexDataIndex = self.vertex_data.index(startVertexData)
        colors = [-1] * self.size
        colors[startVertexDataIndex] = 0
        return self.isBipartite_dfs_util(startVertexDataIndex, colors)


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

if g.isBipartite_dfs_util("D"):
    print("The graph is bipartite - DFS")
else:
    print("The graph is not bipartie - DFS")