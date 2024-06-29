class DFSSolution:
    def get_ancestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        adj_list = [[] for _ in range(n)]
        result = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[1]].append(edge[0])
        
        for i in range(n):
            visited = set()
            stack = [i]
            while stack:
                node = stack.pop()
                if node != i:
                    visited.add(node)
                for neighbour in adj_list[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
            
            result[i] = sorted(list(visited))
        
        return result

from collections import deque
class TopologicalSortSolution:
    # Kahn's algorithm
    def get_ancestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        adj_list = [[] for _ in range(n)]
        result = [set() for _ in range(n)]
        degrees = [0] * n
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            degrees[edge[1]] += 1
        
        q = deque()
        for node, degree in enumerate(degrees):
            if degree == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            for neighbour in adj_list[node]:
                result[neighbour].add(node)
                result[neighbour].update(result[node])
                degrees[neighbour] -= 1
                if degrees[neighbour] == 0:
                    q.append(neighbour)
        
        return [sorted(s) for s in result]

n = 8
test = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(DFSSolution().get_ancestors(n, test))
print(TopologicalSortSolution().get_ancestors(n, test))