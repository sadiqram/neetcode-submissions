from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses) ]
        indeg = [0]*numCourses

        for prereq, course in prerequisites:
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

        return len(order) == numCourses
        

        