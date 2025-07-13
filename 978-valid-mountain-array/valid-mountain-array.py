class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        left = 0
        right = n-1
        while left+1<n and arr[left]<arr[left+1]:
            left+=1
        while right-1>=0 and arr[right]<arr[right-1]:
            right -=1
        if left>0 and left == right and right<n-1:
            return True
        else:
            return False
        