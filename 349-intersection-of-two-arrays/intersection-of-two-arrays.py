class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        res=[]
        for num in nums1:
            if num in nums2:
                res.append(num)
        return res

        