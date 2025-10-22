class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dist = [[-1]*n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range (n):
                if mat[i][j] == 0 :
                    dist[i][j] = 0 
                    q.append((i,j))
        dirs = [(1,0) , (-1,0) , (0,1) ,(0,-1)] 
        while q:
            i , j  = q.popleft()
            for di , dj in dirs:
                ni , nj = i+di , j+dj
                if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                    dist[ni] [nj] = dist[i][j]+1
                    q.append((ni , nj))
        return dist