class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x:x[0])
        out = []
        curr = intervals[0][:]
        for i in intervals[1:]:
            s, e = i
            if s<=curr[1]:
                curr[1] = max(curr[1] , e)
            else:
                out.append(curr)
                curr = i[:]
        out.append(curr)
        return out
        