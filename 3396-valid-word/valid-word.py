class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3 or not word.isalnum():
            return False
        Vowel=set("aeiouAEIOU")
        vowelCount=0
        consonantCount=0
        for char in word:
            if char in Vowel :
                vowelCount+=1
            elif char.isalpha():
                consonantCount+=1
        return vowelCount>0 and consonantCount>0 
                

        