class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        depth=0
        maxDepth=0
        for char in s:
            if char=="(":
                if depth>0:
                    stack.append(char)
                depth+=1
            elif char==")":
                depth-=1
                if depth>0:
                    stack.append(char)
            maxDepth=max(maxDepth,depth)
        return maxDepth
        