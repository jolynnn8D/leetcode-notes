from heapq import heappop, heappush
from typing import List

class Solution:
    def find_city(self, n: int, edges: List[List[int]], distance_threshold: int) -> int:
        adj_list = [[] for _ in range(n)]
        for source, dest, weight in edges:
            adj_list[source].append((dest, weight))
            adj_list[dest].append((source, weight))
        
        min_city = -1
        min_cities_reached = float("inf")
        for city in range(n):
            queue = [(0, city)]
            visited = set()
            while queue:
                distance, curr = heappop(queue)
                if curr in visited:
                    continue
                
                visited.add(curr)
                for neighbour, weight in adj_list[curr]:
                    if distance + weight <= distance_threshold:
                        heappush(queue, (distance + weight, neighbour))
            cities_reached = len(visited) - 1
            if cities_reached < min_cities_reached:
                min_city = city
                min_cities_reached = cities_reached
            elif cities_reached == min_cities_reached:
                min_city = city
        return min_city


if __name__ == "__main__":
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    n = 4
    distance = 4
    result = Solution().find_city(n, edges, distance)
    print(result)







