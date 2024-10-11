class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        windowSum=sum(arr[:k])
        thresholdSum=threshold*k
        if windowSum>=thresholdSum:
            count+=1
        for i in range(k,len(arr)):
            windowSum+=arr[i]-arr[i-k]
            if windowSum>=thresholdSum:
                count+=1
        return count