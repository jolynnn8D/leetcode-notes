# Graph Problems

| Problem                                                                                                                                   | Code                              | Tags                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|--------------------------------------|
| [All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/) | [Python3](./ancestors_dag.py)     | Topological Sort, Kahn's Algorithm         |
| [Course Schedule](https://leetcode.com/problems/course-schedule/) | [Python3](./course_schedule.py)     | Topological Sort, Kahn's Algorithm         |
| [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/) | [Python3](./reachable_cities.py)     | Dijkstra's Algorithm, Floyd-Warshall Algorithm         |
## Algorithms

### Kahn's Algorithm (Topological Sort)
- Find all nodes with no incoming edges, and store them in a queue
- Using an adjacency list, find all neighbours / child of nodes in the queue
- Decrement degree of child nodes (= deleting edge from parent to child)
- If child node has no other incoming nodes, add it to the queue
- **Note**: If the queue becomes empty before all nodes are sorted, it means that a cycle has been detected and topological sorting is not possible