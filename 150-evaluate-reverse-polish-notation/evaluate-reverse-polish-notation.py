class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={"+","-","*","/"}
        for char in tokens:
            if stack and  char in operations:
                b=stack.pop()
                a=stack.pop()
                if char=="+":
                    stack.append(a+b)
                elif char=="-":
                    stack.append(a-b)
                elif char=="*":
                    stack.append(a*b)
                elif char=="/":
                    stack.append(int(a/b))
            else:
                stack.append(int(char))
        return stack[0]



        