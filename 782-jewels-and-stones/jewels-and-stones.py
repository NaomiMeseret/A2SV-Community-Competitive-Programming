class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set (jewels)
        count = 0
        for s in stones:
            if s in jewelSet:
                count +=1
        return count