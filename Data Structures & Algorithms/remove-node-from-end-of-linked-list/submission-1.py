# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        ind = 0

        temp = head
        while temp != None:
            ind += 1
            temp = temp.next

        index_to_remove = ind - n

        temp = dummy
        for i in range(index_to_remove):
            temp = temp.next
        
        temp.next = temp.next.next

        return dummy.next