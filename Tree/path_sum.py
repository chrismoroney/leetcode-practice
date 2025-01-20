# Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def has_path_sum(self, root, target_sum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        target_sum -= root.val
        if target_sum == 0 and not root.left and not root.right:
            return True
        
        return self.has_path_sum(root.left, target_sum) or self.has_path_sum(root.right, target_sum)
    
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))), right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1))))
    target_sum = 22
    print(sol.has_path_sum(root, target_sum))
        