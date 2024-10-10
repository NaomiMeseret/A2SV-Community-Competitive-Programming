class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result=[]
        for i in range(len(nums)-k+1):
            subarray=nums[i:i+k]
            if all(subarray[j+1]-subarray[j]==1 for j in range(k-1)):
                result.append(max(subarray))
            else:
                result.append(-1) 
        return result
        