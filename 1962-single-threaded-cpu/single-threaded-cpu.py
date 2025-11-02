class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        data = [(tasks[i][0] , tasks[i][1],i)for i in range(len(tasks))]
        data.sort()
        res= []
        heap = []
        time , i = 0,0
        n= len(tasks)
        while len(res)<n:
            while i<n and data[i][0]<=time:
                start , proc , idx = data[i]
                heapq.heappush(heap ,(proc , idx))
                i+=1
            if heap:
                proc , idx = heapq.heappop(heap)
                time += proc
                res.append(idx)
            else:
                time = data[i][0]
        return res