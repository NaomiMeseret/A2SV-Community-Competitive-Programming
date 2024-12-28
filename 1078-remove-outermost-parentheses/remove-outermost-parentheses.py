class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        depth=0
        for char in s:
            if char=="(":
                if depth>0:
                    stack.append(char)
                depth+=1
            elif char==")":
                depth-=1
                if depth>0:
                    stack.append(char)
        return "".join(stack)

        