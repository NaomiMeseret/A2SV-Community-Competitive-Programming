from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        count=Counter(s)
        for char in s:
            count[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
        return ''.join(stack)
        