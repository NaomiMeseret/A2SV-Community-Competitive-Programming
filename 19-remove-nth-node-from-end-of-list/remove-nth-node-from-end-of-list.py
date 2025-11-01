# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        current = dummy
        for _ in range(length-n):
            current = current.next
        current.next = current.next.next
        return dummy.next