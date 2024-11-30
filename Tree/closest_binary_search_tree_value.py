# Closest Binary Search Tree value

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closest_value(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """
        
        closest_val = root.val

        while root:
            if abs(root.val - target) < abs(closest_val - target):
                closest_val = root.val
            elif abs(root.val - target) == abs(closest_val - target):
                closest_val = min(root.val, closest_val)
                
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest_val
    
if __name__ == "__main__":
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(5))
    target = 3.714286
    sol = Solution()
    print(sol.closest_value(root, target))