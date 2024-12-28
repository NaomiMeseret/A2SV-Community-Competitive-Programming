class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for char in s:
            if char=="(":
                stack.append(0)
            else:
                last=stack.pop()
                if last==0:
                    stack.append(1)
                else:
                    stack.append(2*last)
                if len(stack)>1:
                    top=stack.pop()
                    stack[-1]+=top
        return stack[0]


        