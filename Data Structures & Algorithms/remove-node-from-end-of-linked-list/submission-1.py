# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lisst=[]
        i=head

        while i:
            lisst.append(i)
            i=i.next
        idx=len(lisst)-n
        if idx==0:
            return head.next
        lisst[idx-1].next=lisst[idx].next
        return lisst[0]
        
        