# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = ""
        while self:
            res += str(self.val) + " "
            self = self.next
        return res.strip()

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        a = []
        while list1 or list2:
            if list1:
                a.append(list1.val)
                list1 = list1.next
            if list2:
                a.append(list2.val)
                list2 = list2.next
        a = sorted(a)
        
        result = None
        p = None
        for i in a:
            if not p:
                result = ListNode(i, None)
                p = result
            else:
                p.next = ListNode(i, None)
                p = p.next
        return result