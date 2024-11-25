class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l=0
        count=0
        nums=str(num)
        divisor=int(nums[:k])
        if divisor != 0 and num % divisor == 0:
            count+=1
        for r in range(k,len(nums)):
            nums+=str(nums[r])
            divisor = int(nums[l + 1:r + 1])  
            if divisor != 0 and num % divisor == 0: 
                count += 1
            l += 1  
        return count




        