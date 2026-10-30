# Travel-Route-Planner
Travel Route Planner 
A Python-based Design and Analysis of Algorithms (DAA) mini project
that models cities and roads as a weighted graph and demonstrates graph
traversal and shortest-path algorithms.
Features
- Dijkstra's Algorithm: Finds a shortest route when all edge
  weights are non-negative.
- Bellman-Ford Algorithm: Supports negative edge weights and
  detects reachable negative-weight cycles.
- Breadth-First Search (BFS): Traverses and displays cities
  reachable from a selected starting city.

Objectives
- Represent a road network using a weighted graph.
- Store graph connections using a Python adjacency list.
- Implement Dijkstra, Bellman-Ford, and BFS.
- Reconstruct and display a route between two cities.
- Compare algorithms using time and space complexity.
Technologies Used
  Technology         Purpose
  Python 3           Main programming language
Dictionary         Stores the graph as an adjacency list
Lists and tuples   Store neighbouring cities and edge weights
Set                Tracks visited cities in BFS
heapq            Provides a min-priority queue for Dijkstra's algorithm

Graph Representation
The project uses an undirected weighted graph.
  City                                Connected cities and distances
  Delhi                               Jaipur (280 km), Agra (230 km)

  Jaipur                              Delhi (280 km), Agra (240 km),
Mumbai (1,150 km), Pune (1,000 km)

  Agra                                Delhi (230 km), Jaipur (240 km),
Mumbai (1,200 km)

  Mumbai                              Jaipur (1,150 km), Agra (1,200 km),
Pune (150 km)
Pune                                Mumbai (150 km), Jaipur (1,000 km)
Each city is a vertex, each road is an edge, and the distance is the
edge weight. The graph is stored as a Python dictionary whose values are
lists of (neighbour, distance) pairs.
Algorithms
1. Dijkstra's Algorithm
Calculates shortest distances from a source city when all edge weights
are non-negative. This implementation uses Python's heapq priority
queue.
2. Bellman-Ford Algorithm
Relaxes all graph edges for at most V - 1 rounds, where V is the
number of vertices. An additional pass checks for a reachable
negative-weight cycle.
3. Breadth-First Search (BFS)
Explores the graph level by level using a queue. In this project, BFS
displays cities reachable from the selected source. It does not
calculate a shortest weighted route when edge weights differ.
How to Run
Prerequisites
- Python 3
- VS Code, PyCharm, Jupyter Notebook, Google Colab, or a terminal
Steps
1. Clone the repository:
   git clone https://github.com/<your-username>/<repository-name>.git
2. Open the project directory:
   cd <repository-name>
3. Run the Python program:
   python travel_route_planner.py
   On systems that use python3:
   python3 travel_route_planner.py
4. Enter the starting city and destination city using names from the
   displayed city list.
5. Choose an algorithm:
   - 1 -- Dijkstra
   - 2 -- Bellman-Ford
   - 3 -- BFS
Replace travel_route_planner.py with your actual Python filename if
it is named differently.

TRAVEL ROUTE PLANNER
Available cities: Delhi, Jaipur, Agra, Mumbai, Pune

Enter starting city: Delhi
Enter destination city: Pune

1. Dijkstra  2. Bellman-Ford  3. BFS
Enter your choice: 1
Example result:
Shortest route: Delhi -> Jaipur -> Pune
Total distance: 1280 km
BFS displays a traversal order rather than a shortest-distance route.
Time and Space Complexity
Let V be the number of vertices (cities) and E be the number of
edges (roads).

  Algorithm                     Time Complexity   Auxiliary Space
  BFS                                O(V + E)            O(V)
Dijkstra (binary heap)     O((V + E) log V)            O(V)
Bellman-Ford                       O(V × E)            O(V)

The graph itself requires O(V + E) storage.
Project Structure
Travel-Route-Planner/
│
├── travel_route_planner.py   # Main Python implementation
├── README.md                 # Project documentation
├── screenshots/              # Optional output screenshots
└── DAA_Travel_Route_Planner_Project_Report.pdf  # Optional report
Limitations
- Uses a small, predefined set of cities and distances.
- Does not retrieve real-world road distances.
- Does not include GPS navigation or live traffic updates.
- The shortest-distance route may not be the fastest route.
- Dijkstra's algorithm is not suitable for negative edge weights.
Future Enhancements
- Add more cities and road connections.
- Load graph data from a CSV file or database.
- Develop a graphical user interface or web application.
- Display routes on an interactive map.
- Include estimated travel time, traffic conditions, tolls, or fuel
  cost.
- Test the algorithms on larger graphs and compare execution times.
Learning Outcomes
- Represented a real-world road network using a graph.
- Implemented graph algorithms using Python.
- Used a priority queue in Dijkstra's algorithm.
- Understood edge relaxation and negative-cycle detection.
- Used BFS and a queue for graph traversal.
- Reconstructed paths using predecessor information.
- Analysed time and space complexity.
- Practised testing and debugging a menu-driven program.
Author
Ujjawal Pauria
UID: 26MCD10091
Course: Master of Computer Applications (Data Science)

Subject: Design and Analysis of Algorithms (DAA)
Project: Travel Route Planner -- Graph Traversal and Shortest Path
Algorithms Using Python
