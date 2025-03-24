"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_valid_BST(self, root: Optional[TreeNode]) -> bool:
        
        def check_nodes(node, _min=-math.inf, _max=math.inf):
            if not node:
                return True

            if node.val <= _min or node.val >= _max:
                return False
            
            return check_nodes(node.left, _min, node.val) and check_nodes(node.right, node.val, _max)

        if not root:
            return True
        
        return check_nodes(root)
    
if __name__ == "__main__":
    root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    s = Solution()

    print(s.is_valid_BST(root))