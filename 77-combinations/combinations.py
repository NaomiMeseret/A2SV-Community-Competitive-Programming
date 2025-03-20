class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res,path=[],[]
        def backTrack(firstName,path):
            if len(path)==k:
                res.append(path[:])
                return
            if firstName>n:
                return
            backTrack(firstName+1,path)
            path.append(firstName)
            backTrack(firstName+1,path)
            path.pop()
        backTrack(1,path)
        return res
        