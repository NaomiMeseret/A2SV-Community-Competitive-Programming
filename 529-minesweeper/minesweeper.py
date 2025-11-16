class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m , n = len(board) , len(board[0])
        row , col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        dirs = [(-1,-1), (-1,0), (-1,1),
            (0,-1),(0,1),(1,-1),  (1,0),  (1,1)]
        queue =deque([(row , col)])
        visited = {(row , col)}
        while queue:
            r , c = queue.popleft()
            count = 0
            for dr , dc in dirs:
                nr , nc = r+dr , c+dc
                if 0<=nr<m and 0<=nc<n:
                    if board[nr][nc] == "M":
                        count +=1
            if count>0:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for dr , dc in dirs:
                    nr , nc = r+dr , c+dc
                    if 0<=nr<m and 0<=nc<n:
                        if board[nr][nc] == "E" and (nr , nc) not in visited:
                            visited.add((nr , nc))
                            queue.append((nr, nc))
        return board

        