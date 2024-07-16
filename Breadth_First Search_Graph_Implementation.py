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

    def bfs(self, start_vertex_data):
        #print(f"The BFS from {start_vertex_data} is:")
        print("The BFS from", start_vertex_data, "is:")
        start_vertex = self.vertex_data.index(start_vertex_data) # Find the index of start_vertex_data in self.vertex_data
        queue = [start_vertex] # Initialize the queue with the index
        visited = [False] * self.size
        visited[start_vertex] = True
        #visited[queue[0]] = True

        # Run while there are vertices in queue
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=" ")
            for neighbour in range(self.size):
                if self.adj_matrix[current_vertex][neighbour] == 1 and not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

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

g.bfs('D')