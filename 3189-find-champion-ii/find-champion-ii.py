class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        loss = [0]*n
        for w , l in edges:
            loss[l]+=1
        champ =  [i for i in range(n) if loss[i] == 0]
        if len(champ) ==1:
            return champ[0]
        else:
            return -1

        