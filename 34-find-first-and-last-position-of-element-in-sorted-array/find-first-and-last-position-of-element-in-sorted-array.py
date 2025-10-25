class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first =- 1
        last =- 1
        def firstPostion(l,r):
            nonlocal first
            while l<=r:
                mid=(l+r)//2
                if nums[mid] == target:
                    first = mid
                    r = mid-1
                elif nums[mid]<target:
                    l = mid+1
                else:
                    r=mid-1
            return first
        def lastPostion(l,r):
            nonlocal last
            while l<=r:
                mid=(l+r)//2
                if nums[mid] == target:
                    last = mid
                    l = mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return last
        ans=[firstPostion(0,len(nums)-1), lastPostion(0,len(nums)-1)]
        return ans

        
        
        

     
        