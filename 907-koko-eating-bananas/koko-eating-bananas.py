class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=1
        def vaild(mid):
            totalSum=0
            for pile in piles:
                totalSum+=ceil(pile/mid)
            return totalSum<=h
        while l<=r:
            mid=(l+r)//2
            if vaild(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        