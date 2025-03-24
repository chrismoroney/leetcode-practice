"""
Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def get_minimum_difference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        nodes = []

        def traverse_inorder(node):
            if node is None:
                return
            else:
                traverse_inorder(node.left)
                nodes.append(node.val)
                traverse_inorder(node.right)
        
        traverse_inorder(root)

        n = len(nodes)
        min_diff = nodes[n - 1]
        for i in range(1, n):
            min_diff = min(min_diff, nodes[i] - nodes[i-1])
        
        return min_diff
    
if __name__ == "__main__":
    root = TreeNode(1, left=TreeNode(0), right=TreeNode(48, left=TreeNode(12), right=TreeNode(49)))
    sol = Solution()
    print(sol.get_minimum_difference(root))

