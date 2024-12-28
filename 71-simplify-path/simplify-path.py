class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        components=path.split("/")
        for parts in components:
            if parts=="..":
                if stack:
                    stack.pop()
            elif parts=="." or not parts:
                continue
            else:
                stack.append(parts)
        return "/"+"/".join(stack)
        