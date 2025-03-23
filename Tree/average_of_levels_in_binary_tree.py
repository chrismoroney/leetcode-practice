"""
Average of Levels in Binary tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def average_of_levels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        q = deque([root])
        avgs = []

        while q:
            _sum, _level_size = 0, len(q)
            for _ in range(_level_size):
                node = q.popleft()
                _sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avgs.append(_sum * 1.0 / _level_size)

        return avgs

if __name__ == "__main__":
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    s = Solution()
    print(s.average_of_levels(root))