class Solution:
    def minimumChairs(self, s: str) -> int:
        current_people = 0
        max_chairs = 0
        for i in s:
            if i == 'E':
                current_people += 1
            else:  
                current_people -= 1
            max_chairs = max(max_chairs, current_people)
        
        return max_chairs
            