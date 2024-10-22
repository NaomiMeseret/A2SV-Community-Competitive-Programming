# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        rightnode= head
        leftnode= head

        for _ in range(n):
            if rightnode:
                rightnode= rightnode.next
            else:
                return head

        if not rightnode:
            return head.next

        while rightnode.next:
            rightnode= rightnode.next
            leftnode= leftnode.next

        leftnode.next= leftnode.next.next
        return head
