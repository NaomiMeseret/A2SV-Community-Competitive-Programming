class MyStack:
    from collections import deque

    def __init__(self):
        self.queue=deque()
    def push(self, x: int) -> None:
        self.queue.appendleft(x)
    def pop(self) -> int:
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()