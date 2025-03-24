"""
Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    path_len = 0
    def longest_zig_zag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, move_right, steps):
            if node:
                self.path_len = max(self.path_len, steps)
                if move_right:
                    dfs(node.right, False, steps + 1)
                    dfs(node.left, True, 1)
                else:
                    dfs(node.left, True, steps + 1)
                    dfs(node.right, False, 1)

        dfs(root, True, 0)
        return self.path_len
    
    def build_tree_from_list(self, values):
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            current = queue.popleft()

            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

        return root
    
if __name__ == "__main__":
    s = Solution()
    #vals = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
    vals = [1,1,1,None,1,None,None,1,1,None,1]
    root = s.build_tree_from_list(vals)
    print(s.longest_zig_zag(root))
