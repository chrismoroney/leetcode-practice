'''
Rotate List

Given the head of a linked list, rotate the list to the right by k places.
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotate_right(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        if not head:
            return None
        elif not head.next:
            return head

        tail = head
        size = 1
        while tail.next:
            tail = tail.next
            size += 1
        tail.next = head

        n_tail = head
        for i in range(size - k % size - 1):
            n_tail = n_tail.next
        n_head = n_tail.next

        n_tail.next = None

        return n_head
    
    def print_linked_list(self, head: ListNode):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next
    
if __name__ == "__main__":
    head = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    k = 2
    sol = Solution()

    print("Before: ")
    sol.print_linked_list(head)
    print("After: ")
    sol.print_linked_list(sol.rotate_right(head, k))
