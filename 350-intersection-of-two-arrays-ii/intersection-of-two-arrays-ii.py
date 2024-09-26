class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        left=0
        res=[]
        while left<len(nums1):
            if nums1[left] in nums2:
                res.append(nums1[left])
                nums2.remove(nums1[left])
            left+=1
        return res

        