# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_val = head

        if current_val == None:
            return current_val
        
        prev = None

        while current_val != None:
            temp = current_val.next
            current_val.next = prev
            prev = current_val
            current_val = temp

        return prev 


