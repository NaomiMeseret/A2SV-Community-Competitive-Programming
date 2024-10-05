class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        count=0
        prefix=0
        output=0
        for r in range(len(nums)):
            if nums[r]%2!=0:
                count+=1
                prefix=0
            while count==k:
                prefix+=1
                if nums[l]%2!=0:
                    count-=1
                l+=1
            output+=prefix
        return output 
                

        

            