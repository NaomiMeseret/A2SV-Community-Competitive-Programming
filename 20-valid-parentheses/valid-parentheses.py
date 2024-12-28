class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        myDict={"(":")","[":"]","{":"}"}
        for i in range(len(s)):
            if s[i] in myDict.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                a=stack.pop()
                if s[i]!=myDict[a]:
                    return False
        return stack==[]


        