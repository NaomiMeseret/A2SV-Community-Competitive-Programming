class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=""
        left=0
        right=0
        while left<len(word1) and right<len(word2):
            merged+=word1[left]
            merged+=word2[right]
            left+=1
            right+=1
        if left<len(word1):
            merged+=word1[left:]
        elif right<len(word2):
            merged+=word2[right:]
        return merged

        