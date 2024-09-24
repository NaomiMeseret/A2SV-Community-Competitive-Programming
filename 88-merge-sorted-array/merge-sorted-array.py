class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left=0
        right=0
        merged=[]
        while left<m and right<n:
            if nums1[left]<=nums2[right]:
                merged.append(nums1[left])
                left+=1
            else:
                merged.append(nums2[right])
                right+=1
        merged.extend(nums1[left:m])
        merged.extend(nums2[right:n])
        nums1[:]=merged
        
        