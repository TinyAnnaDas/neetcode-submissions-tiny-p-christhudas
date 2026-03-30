# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        temp = head 
        while temp:
            length +=1 
            temp = temp.next
        
        from_start = (length - n)
        if from_start == 0:
            return head.next 

        position = 0 
        temp = head 
        while temp:
            if position == from_start-1:
                temp.next = temp.next.next
                break 
            position +=1 
            temp = temp.next 
        return head 




        