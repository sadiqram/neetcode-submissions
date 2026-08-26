from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0]*numCourses

        for course,prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course]+=1
        
        q = deque(course for course in range(numCourses) if indeg[course]==0)
        order = []

        while q:
            prereq = q.popleft()
            order.append(prereq)

            for course in adj[prereq]:
                indeg[course]-=1
                if indeg[course] == 0:
                    q.append(course)
        
        return order if len(order) == numCourses else []
        