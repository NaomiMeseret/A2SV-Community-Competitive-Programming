class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for pre, course in prerequisites:
            graph[pre].append(course)
        res = [set() for _ in range(numCourses)]
        for i in range(numCourses):
            q = deque([i])
            visited = set()
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        res[i].add(nei)
                        q.append(nei)
        ans = []
        for u, v in queries:
            ans.append(v in res[u])
        return ans
                