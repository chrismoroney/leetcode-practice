"""
Maximum Twin Sum of a Linked list

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pair_sum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        max_sum = 0

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current, previous = slow, None
        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp

        start = head
        while previous:
            max_sum = max(max_sum, start.val + previous.val)
            previous = previous.next
            start = start.next

        return max_sum
    
    def convert_list_to_listnodes(self, head):
        root = ListNode()
        a = root
        
        for val in head:
            root.next = ListNode(val)
            root = root.next

        return a.next
    
if __name__ == "__main__":
    solution = Solution()
    head = [4,2,2,3]
    node_head = solution.convert_list_to_listnodes(head)
    print(solution.pair_sum(node_head))
    