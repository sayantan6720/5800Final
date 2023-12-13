from Model.adjacencymatrix import AdjacencyMatrix
def floyd_warshall_with_path(weights):
    n = len(weights)
    # Initialize distance and predecessor matrices
    distance = [[weights[i][j] for j in range(n)] for i in range(n)]
    predecessor = [[i if weights[i][j] != float('inf') and i != j else None for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    predecessor[i][j] = predecessor[k][j]

    return distance, predecessor

def print_path(predecessor, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = predecessor[start][end]
    return path[::-1]

graph = AdjacencyMatrix("Flight Data - Sheet1.csv")

distances, predecessors = floyd_warshall_with_path(graph)
start_node = 0  # Assuming node 'A' is represented by index 0

for end_node in range(len(graph)):
    if start_node != end_node:
        path = print_path(predecessors, start_node, end_node)
        path_str = ' -> '.join(map(str, path))
        print(f"Shortest path from {start_node} to {end_node}: {path_str}")



shortest_paths = floyd_warshall_with_path(graph.get_matrix())
print(shortest_paths)

