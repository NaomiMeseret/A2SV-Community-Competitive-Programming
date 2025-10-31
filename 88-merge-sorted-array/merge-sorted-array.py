class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = m-1
        second = n-1
        k= m+n-1
        while second >= 0:
            if first>=0 and nums1[first]>nums2[second]:
                nums1[k] = nums1[first]
                first-=1
            else:
                nums1[k] = nums2[second]
                second -=1
            k-=1
        return nums1

        
        