# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        new_head = ListNode()

        if list1.val < list2.val:
            new_head.val = list1.val
            list1 = list1.next
        else:
            new_head.val = list2.val
            list2 = list2.next

        current = new_head

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            current.next = temp
            current = temp
            

        while list1 != None:
            temp = list1
            list1 = list1.next
            current.next = temp
            current = temp
        
        while list2 != None:
            temp = list2
            list2 = list2.next
            current.next = temp
            current = temp
        
        
        return new_head











