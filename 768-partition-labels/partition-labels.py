class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i ,c in enumerate(s):
            lastIndex[c] = i
        start = 0
        end = 0
        res = []
        for i , c in enumerate(s):
            end = max(end , lastIndex[c])
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res

        
        