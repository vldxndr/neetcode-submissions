# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        dummy = ListNode(0, head)

        left, right = dummy, head
        while right:
            if i >= n:
                left = left.next
                right = right.next
            else:
                right = right.next
                i += 1
        left.next = left.next.next
        return dummy.next
