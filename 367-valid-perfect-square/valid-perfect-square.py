class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res=math.sqrt(num)
        if res==int(res):
            return True
        else:
            return False
        