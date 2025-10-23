class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redAdj = [[] for _ in range(n)]
        blueAdj =[[]for _ in range(n)]
        for a , b in redEdges:
            redAdj[a].append(b)
        for a,b in blueEdges:
            blueAdj[a].append(b)
        distRed , distBlue = [-1]*n , [-1]*n
        distRed[0] , distBlue[0] = 0 ,0
        q  = deque()
        q.append((0,0))
        q.append((0,1))
        while q:
            node , lastC = q.popleft()
            if lastC == 0:
                nextList = blueAdj[node]
                nextColor = 1
                curr = distRed[node]
            else:
                nextList = redAdj[node]
                nextColor = 0
                curr = distBlue[node]
            for nei in nextList:
                if nextColor == 0 :
                    if distRed[nei] == -1:
                        distRed[nei] = curr+1
                        q.append((nei , 0))
                else:
                    if distBlue[nei] == -1:
                        distBlue[nei] = curr+1
                        q.append((nei , 1))
        ans = []
        for i in range(n):
            r = distRed[i]
            b = distBlue[i]
            if r == -1 and b == -1:
                ans.append(-1)
            elif r == -1:
                ans.append(b)
            elif b == -1:
                ans.append(r)
            else:
                ans.append(min(r,b))
        return ans
