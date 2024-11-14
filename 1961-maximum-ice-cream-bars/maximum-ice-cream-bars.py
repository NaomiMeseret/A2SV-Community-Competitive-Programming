class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maximum=max(costs)
        count=[0]*(maximum+1)
        for cost in costs:
            count[cost]+=1
        Sum=0
        res=0
        for cost in range(1, maximum + 1):
            if count[cost] == 0:
                continue
            while count[cost] > 0 and Sum + cost <= coins:
                Sum += cost
                res += 1
                count[cost] -= 1
        return res


