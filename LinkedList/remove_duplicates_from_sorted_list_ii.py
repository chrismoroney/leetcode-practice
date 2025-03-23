"""
Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def delete_duplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sentinel = ListNode(0, head)
        predecessor = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                
                predecessor.next = head.next
            
            else:
                predecessor = predecessor.next

            head = head.next
        
        return sentinel.next
    
    def convert_list_to_linked_list(self, head):
        linked_list = ListNode()
        a = linked_list

        for val in head:
            linked_list.next = ListNode(val)
            linked_list = linked_list.next
        
        return a.next

    def print_linked_list(self, head):
        curr = head

        while curr:
            print(curr.val, end=" -> " if curr.next else "\n")
            curr = curr.next

if __name__ == "__main__":
    s = Solution()
    head = [1, 2, 3, 3, 4, 4, 5]
    linked_list = s.convert_list_to_linked_list(head)
    print("before: ", end="")
    s.print_linked_list(linked_list)
    new_list = s.delete_duplicates(linked_list)
    print("after: ", end="")
    s.print_linked_list(new_list)