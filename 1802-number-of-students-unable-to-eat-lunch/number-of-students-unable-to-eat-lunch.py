class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue=deque(students)
        stack=sandwiches
        while queue:
            if queue[0]==stack[0]:
                queue.popleft()
                stack.pop(0)
            else:
                queue.append(queue.popleft())
            if all(student!=stack[0] for student in queue):
                break
        return len(queue)

        