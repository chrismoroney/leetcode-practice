# Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def merge_two_lists(self, list1, list2):
        head = ListNode(-1)

        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 is not None else list2

        return head.next
        
    def merge_k_lists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        # Divide and conquer - instead of merge to list 0 every time, merge in pairs, then merge those pairs together etc.
        n = len(lists)
        div = 1

        while div < n:
            for i in range(0, n - div, div * 2):
                lists[i] = self.merge_two_lists(lists[i], lists[i + div])
            div *= 2

        return lists[0] if n > 0 else None      

    def print_linked_list(self, head):
        """
        Prints the linked list starting from the given head node.

        :param head: ListNode, the head of the linked list
        """
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

if __name__ == "__main__":
    list0 = ListNode(1, next=ListNode(4, next=ListNode(5))) 
    list1 = ListNode(1, next=ListNode(3, next=ListNode(4)))
    list2 = ListNode(2, next=ListNode(6))
    list_of_lists = [list0, list1, list2]
    solution = Solution()

    final_list = solution.merge_k_lists(list_of_lists)
    solution.print_linked_list(final_list)
