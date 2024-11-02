# Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def right_side_view(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        
        next_level = deque([root])

        answer = []

        while next_level:
            current_level = next_level
            next_level = deque()

            while current_level:
                node = current_level.popleft()
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)

            answer.append(node.val)

        return answer
        
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3, right=TreeNode(4)))
    print(solution.right_side_view(root))