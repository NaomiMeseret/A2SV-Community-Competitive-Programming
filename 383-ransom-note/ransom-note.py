class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount=Counter(ransomNote)
        magazineCount=Counter(magazine)
        for char in ransomNote:
            if ransomCount[char]>magazineCount.get(char,0):
                return False
        return True
        