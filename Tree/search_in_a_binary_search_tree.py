# Search in a Binary Search Tree

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        
        while root:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right

        return None

if __name__ == "__main__":
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(4)), right=TreeNode(7))
    sol = Solution()
    val = 2
    val2 = 6

    print(sol.searchBST(root, val))
    print(sol.searchBST(root, val2))
