class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        if len(nums1)==len(nums2):
            result=nums2[0]-nums1[0]
            return(result)
        else:
            return 0
       
        

        