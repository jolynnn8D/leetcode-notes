from collections import deque
class Solution:
    def can_finish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            degrees[course] += 1
        
        q = deque([course for course, degree in enumerate(degrees) if degree == 0])
        course_tree = []
        while q:
            node = q.popleft()
            course_tree.append(node)
            for neighbour in adj_list[node]:
                degrees[neighbour] -= 1
                if degrees[neighbour] == 0:
                    q.append(neighbour)
        
        return len(course_tree) == numCourses