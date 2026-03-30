# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # after the above iteration, the slow pointer will be at the middle node. 

        # reverse the second half 

        second = slow.next 
        slow.next = None 
        prev = None
        while second:
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp 
        
        # now the list 2 and the second part is reversed 
        # the head of the second is at the last element

        # merge 

        first, second = head, prev 

        while second:
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1 
            first = temp1 
            second = temp2 

        


        