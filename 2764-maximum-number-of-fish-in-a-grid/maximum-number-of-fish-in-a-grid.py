class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_fish = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visited:
                    q = deque([(r, c)])
                    visited.add((r, c))
                    total = grid[r][c]
                    while q:
                        x, y = q.popleft()
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nx, ny = x + dr, y + dc
                            if (0 <= nx < rows and 0 <= ny < cols
                                and grid[nx][ny] > 0 and (nx, ny) not in visited):
                                visited.add((nx, ny))
                                q.append((nx, ny))
                                total += grid[nx][ny]
                    max_fish = max(max_fish, total)
        return max_fish
            