class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        skill.sort()
        targetSum=skill[0]+skill[-1]
        totalSum=0
        left=0
        right=n-1
        while left<right:
            if skill[left]+skill[right]!=targetSum:
                return -1
            totalSum+=skill[left]*skill[right]
            left+=1
            right-=1
        return totalSum



        

        