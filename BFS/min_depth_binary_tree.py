# Problem: Minimum Depth of a Binary Tree
# Given a binary tree, find its minimum depth. 
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# A leaf is a node with no children.
# Example:
# Input:
#       3
#      / \
#     9  20
#       /  \
#      15   7


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    if not root:
        return 0
    
    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()
        
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))


if __name__ == "__main__":
# Binary Tree:
#        1
#       / \
#      2   3
#         / \
#        4   5
#             \
#              6

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    root1.right.right.right = TreeNode(6)
# Binary Tree:
#            1
#          /   \
#         2     3
#        /     / \
#       4     5   6
#            /   / \
#           7   8   9

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)
    root2.right.left.left = TreeNode(7)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(9)
    print(minDepth(root1))
    print(minDepth(root2))