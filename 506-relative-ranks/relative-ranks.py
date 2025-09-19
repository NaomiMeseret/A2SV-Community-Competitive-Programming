class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
            if not score:
                return []
            heap=[(-s,i) for i,s in enumerate(score)]
            heapq.heapify(heap)
            res=[""]*len(score)
            for rank in range(len(score)):
                s,i = heapq.heappop(heap)
                if rank==0:
                    res[i]="Gold Medal"
                elif rank == 1:
                    res[i]="Silver Medal"
                elif rank==2:
                    res[i]="Bronze Medal"
                else:
                    res[i]=str(rank+1)
            return res
            