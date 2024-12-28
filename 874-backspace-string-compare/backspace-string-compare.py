class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        l=0
        r=0
        while l<len(s):
            if s[l]=="#":
                if stack1:
                   stack1.pop()
            else:
                stack1.append(s[l])
            l+=1
        while r<len(t):
            if t[r]=="#":
                if stack2:
                   stack2.pop()
            else:
                stack2.append(t[r])
            r+=1
        return stack1==stack2
        