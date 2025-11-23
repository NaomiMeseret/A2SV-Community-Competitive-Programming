class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols  = len(grid),len(grid[0])
        visted = set()
        count = 0
        def bfs(r,c):
            q = deque([(r,c)])
            visted.add((r,c))
            while q:
                x,y = q.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny = x+dx , y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == "1" and (nx,ny)not in visted:
                        visted.add((nx,ny))
                        q.append((nx,ny))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visted :
                    bfs(r,c)
                    count+=1
        return count
            