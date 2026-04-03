# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        
        # 1. GĂSIM MIJLOCUL (Slow & Fast)
        # Pornim fast de la head.next ca slow să se oprească exact la finalul primei jumătăți
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # headRev va fi începutul celei de-a doua jumătăți
        headRev = slow.next
        # TĂIEM legătura dintre cele două jumătăți pentru a evita ciclul infinit
        slow.next = None
        
        # 2. INVERSĂM A DOUA JUMĂTATE (Reverse)
        # Folosim logica ta cu prev, curr și next_node
        prev = None
        curr = headRev
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 3. ÎMPLETIM CELE DOUĂ LISTE (The Zipper Merge)
        # 'prev' este acum capul listei inversate
        first = head
        second = prev
        
        while second:
            # Salvăm "viitorul" ambelor liste
            tmp1 = first.next
            tmp2 = second.next
            
            # Facem conexiunea în zig-zag
            first.next = second
            second.next = tmp1
            
            # Avansăm pointerii la nodurile salvate
            first = tmp1
            second = tmp2