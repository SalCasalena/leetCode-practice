"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self):
        node = self
        while node != None:
            print(node + ", ", end="")
            node = node.next
        print(None)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp_head = ListNode()
        
        while (list1 != None) or (list2 != None):
            if list1.val < list2.val:
                temp_head.next = list1
            else:
                temp_head.next = list2
            
            list1 = list1.next
            list2 = list2.next
        
        return temp_head.next
    
arr1 = ListNode(1, ListNode(2, ListNode(3, None)))
arr2 = [3, 4, 5]

s = Solution()
print(s.mergeTwoLists(arr1, arr2))
        