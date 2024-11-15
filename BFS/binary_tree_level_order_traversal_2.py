# Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def level_order_bottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        levels = []
        level_below = deque([root])

        while root and level_below:
            current_level = level_below
            level_below = deque()
            levels.append([])
            
            for node in current_level:
                levels[-1].append(node.val)

                if node.left:
                    level_below.append(node.left)
                if node.right:
                    level_below.append(node.right)
                    
        return levels[::-1]

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.level_order_bottom(root))
