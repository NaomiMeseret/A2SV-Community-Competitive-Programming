class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxValue=max(count.values())
        buckets = [[] for i in range(maxValue+1)]
        for num , freq in count.items():
            buckets[freq].append(num)
        res = []
        for i in range(maxValue,0,-1):
            if buckets[i]:
                res.extend(buckets[i])
            if len(res)>=k:
                break
        return res


        