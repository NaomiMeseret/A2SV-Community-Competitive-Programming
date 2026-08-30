class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        arr = list(freq.items())

        arr.sort(key=lambda x: (-x[1] , x[0]))

        ans = []

        for i in range(k):
            ans.append(arr[i][0])
        
        return ans