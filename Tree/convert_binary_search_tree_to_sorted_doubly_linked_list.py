# Convert Binary Search Tree To Sorted Doubly Linked List

# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. 
# For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. 
# You should return the pointer to the smallest element of the linked list.


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def inorder(root):
            nonlocal head, tail

            if root:
                inorder(root.left)
                
                if tail:
                    tail.right = root
                    root.left = tail
                else:
                    head = root
                tail = root

                inorder(root.right)

        if not root:
            return None

        head, tail = None, None
        inorder(root)

        tail.right = head
        head.left = tail
        return head

if __name__ == "__main__":
    sol = Solution()
    root = Node(4, 
                left=Node(2, 
                      left=Node(1), 
                      right=Node(3)
                ), right=Node(5)
    )

    print(sol.treeToDoublyList(root))
