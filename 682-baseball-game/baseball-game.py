class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char.isdigit() or (char[0] == '-' and char[1:].isdigit()):
                stack.append(int(char))
            elif char == "+":
                stack.append(stack[-1] + stack[-2])
            elif char == "D":
                stack.append(stack[-1] * 2)
            elif char == "C":
                stack.pop()
        return sum(stack)