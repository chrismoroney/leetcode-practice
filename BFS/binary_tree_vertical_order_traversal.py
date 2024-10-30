# Binary Tree Vertical Order Traversal

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def vertical_order(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        col_map = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is not None:
                col_map[col].append(node.val)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return_list = [col_map[col] for col in sorted(col_map.keys())]
        return return_list


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(sol.vertical_order(root))

    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4, right=TreeNode(5,right=TreeNode(6))),right=TreeNode(10)),right=TreeNode(3,left=TreeNode(9),right=TreeNode(11)))
    print(sol.vertical_order(root))
