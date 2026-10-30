
import heapq

# Creating a graph using an adjacency list
graph = {
    "Delhi": [("Jaipur", 280), ("Agra", 230)],
    "Jaipur": [("Delhi", 280), ("Agra", 240),
               ("Mumbai", 1150), ("Pune", 1000)],
    "Agra": [("Delhi", 230), ("Jaipur", 240),
             ("Mumbai", 1200)],
    "Mumbai": [("Jaipur", 1150), ("Agra", 1200),
               ("Pune", 150)],
    "Pune": [("Mumbai", 150), ("Jaipur", 1000)]
}


# Function to reconstruct the shortest path
def get_path(parent, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = parent[current]

    return path[::-1]


# 1. Dijkstra's Algorithm
def dijkstra(graph, source, destination):

    distance = {city: float('inf') for city in graph}
    parent = {city: None for city in graph}

    distance[source] = 0
    pq = [(0, source)]

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current_dist > distance[current]:
            continue

        if current == destination:
            break

        for neighbor, weight in graph[current]:

            new_dist = current_dist + weight

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                parent[neighbor] = current

                heapq.heappush(
                    pq, (new_dist, neighbor)
                )

    if distance[destination] == float('inf'):
        return None, None

    return distance[destination], get_path(
        parent, destination
    )


# 2. Bellman-Ford Algorithm
def bellman_ford(graph, source, destination):

    vertices = list(graph.keys())
    edges = []

    for city in graph:
        for neighbor, weight in graph[city]:
            edges.append((city, neighbor, weight))

    distance = {city: float('inf') for city in vertices}
    parent = {city: None for city in vertices}

    distance[source] = 0

    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):

        updated = False

        for u, v, weight in edges:

            if (distance[u] != float('inf') and
                distance[u] + weight < distance[v]):

                distance[v] = distance[u] + weight
                parent[v] = u
                updated = True

        if not updated:
            break

    # Check for negative weight cycle
    for u, v, weight in edges:

        if (distance[u] != float('inf') and
            distance[u] + weight < distance[v]):

            return "Negative cycle detected", None

    if distance[destination] == float('inf'):
        return None, None

    return distance[destination], get_path(
        parent, destination
    )


# 3. Breadth First Search
def bfs(graph, source):

    visited = set()
    queue = [source]
    visited.add(source)

    print("\nCities reachable from", source, ":")

    while queue:

        city = queue.pop(0)
        print(city, end=" -> ")

        for neighbor, weight in graph[city]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("End")


# Main Program
print("================================")
print("       TRAVEL ROUTE PLANNER")
print("================================")

print("\nAvailable Cities:")
for city in graph:
    print("-", city)

source = input("\nEnter Starting City: ").strip().title()
destination = input("Enter Destination City: ").strip().title()

if source not in graph or destination not in graph:
    print("Invalid city name!")

else:

    print("\nChoose Algorithm:")
    print("1. Dijkstra Algorithm")
    print("2. Bellman-Ford Algorithm")
    print("3. BFS Graph Traversal")

    choice = input("Enter your choice: ")

    if choice == "1":

        dist, path = dijkstra(
            graph, source, destination
        )

    elif choice == "2":

        dist, path = bellman_ford(
            graph, source, destination
        )

    elif choice == "3":

        bfs(graph, source)
        dist, path = None, None

    else:
        print("Invalid choice!")
        dist, path = None, None

    if choice in ("1", "2"):

        if path is None:
            print("\nNo route found or negative cycle detected.")

        else:
            print("\nShortest Route:")
            print(" -> ".join(path))

            print("Total Distance:", dist, "km")
