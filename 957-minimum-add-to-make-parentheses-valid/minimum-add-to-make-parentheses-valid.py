class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        unmatchedClose=0
        for char in s:
            if char=="(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    unmatchedClose+=1
        return len(stack)+unmatchedClose
        