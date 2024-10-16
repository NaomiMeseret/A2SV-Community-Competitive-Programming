class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=set("aeiou")
        currentCount=0
        maxVowel=0
        for char in s[:k]:
            if char in vowel:
                currentCount+=1
        maxVowel=currentCount
        for i in range(k,len(s)):
            if s[i] in vowel:
                currentCount+=1
            if s[i-k] in vowel:
                currentCount-=1
            maxVowel=max(maxVowel,currentCount)
        return maxVowel
                