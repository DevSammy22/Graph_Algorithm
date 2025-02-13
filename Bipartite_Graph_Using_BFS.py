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

    def isBipartite_bfs(self, start):
        colors = [-1] * self.size # -1 means no color, 0 means one color, and 1 means another color
        colors[start] = 0
        queue = [start] #initialize queue with starting vertex

        # Run while there are vertices in queue
        while queue:
            current_vertex = queue.pop(0)
            # Return false if there is a self-loop
            if self.adj_matrix[current_vertex][current_vertex] == 1:
                return False

            for neighbour in range(self.size):
                if self.adj_matrix[current_vertex][neighbour] == 1 and colors[neighbour] == -1:
                    colors[neighbour] = 1 - colors[current_vertex] # Assign alternate color to this adjacent neigbhour of current_vertex
                    queue.append(neighbour)
                elif self.adj_matrix[current_vertex][neighbour] == 1 and colors[neighbour] == colors[current_vertex]:
                    return False
        return True


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

if g.isBipartite_bfs(0):
    print("The graph is bipartite")
else:
    print("The graph is not bipartite")