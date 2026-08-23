from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0]*numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course) # We want the prereq to discover the course/ we need to take/explore prereq before course
            indeg[course]+=1 # basically incrememnt the requirements/prereqs required to take this course

        q = deque(course for course in range(numCourses) if indeg[course] == 0) # We start from courses with no prereqs
        order = []
        while q:
            prereq = q.popleft()
            order.append(prereq)
            for course in adj[prereq]:
                indeg[course]-=1
                if indeg[course]==0:
                    q.append(course)
        
        return order if len(order) == numCourses else []
