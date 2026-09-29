# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=list1
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        curr=list2
        while curr:
            arr.append(curr.val)
            curr=curr.next

        sra=sorted(arr)

        dummy=ListNode()
        tail=dummy

        for i in sra:
            tail.next=ListNode(i)
            tail=tail.next

        return dummy.next