class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0
        for i in range(n):
            if i not in visited:
                provinces += 1
                q = deque([i])
                visited.add(i)
                while q:
                    city = q.popleft()
                    for nei in range(n):
                        if isConnected[city][nei] == 1 and nei not in visited:
                            visited.add(nei)
                            q.append(nei)
        return provinces
