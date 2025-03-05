class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        total=0
        for num in answers:
            x=num+1
            while count[num]>0:
                count[num]-=x
                total+=x
        return total