class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visted = {0}
        q = deque([0])
        while q:
            r = q.popleft()
            for key in rooms[r]:
                if key not in visted:
                    visted.add(key)
                    q.append(key)
        return len(visted) == len(rooms)
