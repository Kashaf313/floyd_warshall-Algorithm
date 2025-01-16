INF = float('inf')
vertices = 4  # Number of cities

def floyd_warshall(graph):
    # Initialize the distance matrix
    distance_between_vertices = [[INF] * vertices for _ in range(vertices)]
    
    # Copy the input graph to the distance matrix
    for i in range(vertices):
        for j in range(vertices):
            distance_between_vertices[i][j] = graph[i][j]
    
    # Set the distance to self as 0
    for i in range(vertices):
        distance_between_vertices[i][i] = 0
    
    # Main algorithm
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance_between_vertices[i][j] = min(
                    distance_between_vertices[i][j],
                    distance_between_vertices[i][k] + 
                                 distance_between_vertices[k][j]
                )
  
    print_shortest_paths(distance_between_vertices)

def print_shortest_paths(distance):
    print("Following shows the shortest path between all the pairs of cities:")
    for i in range(vertices):
        for j in range(vertices):
            print(f"The shortest distance between city {i + 1} and city {j + 1} is", end=" ")
            if distance[i][j] == INF:
                print("INF")
            else:
                print(distance[i][j])
        print(" ")

# Example graph representing distances between cities
# Here, the graph is represented as an adjacency matrix
graph = [
    [0, 3, INF, 5],  # Distances from city 1
    [2, 0, INF, 4],  # Distances from city 2
    [INF, 1, 0, INF], # Distances from city 3
    [INF, INF, 2, 0]  # Distances from city 4
]

# Run the Floyd-Warshall algorithm
floyd_warshall(graph)
