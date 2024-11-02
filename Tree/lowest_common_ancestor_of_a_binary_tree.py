# Lowest Common Ancestor of a Binary Tree

# Given two TreeNodes of a binary tree p and q, return their lowest common ancestor (LCA).

# According to the definition of LCA on Wikipedia: 
# "The lowest common ancestor of two TreeNodes p and q in a tree T is the lowest TreeNode that has both p and q as descendants 
# (where we allow a TreeNode to be a descendant of itself)."


# Definition for a TreeTreeNode.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.answer = None

    def lowest_common_ancestor(self, root, p, q):
        """
        :type root: TreeTreeNode
        :type p: TreeTreeNode
        :type q: TreeTreeNode
        :rtype: TreeTreeNode
        """

        def recurse(root):
            if not root:
                return False
            
            left = recurse(root.left)
            right = recurse(root.right)

            mid = (root == p or root == q)

            if left + right + mid >= 2:
                self.answer = root

            return left or right or mid
    
        recurse(root)
        return self.answer
    
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    TreeNode5 = TreeNode(5)
    TreeNode1 = TreeNode(1)
    TreeNode6 = TreeNode(6)
    TreeNode2 = TreeNode(2)
    TreeNode0 = TreeNode(0)
    TreeNode8 = TreeNode(8)
    TreeNode7 = TreeNode(7)
    TreeNode4 = TreeNode(4)

    root.left = TreeNode5
    root.right = TreeNode1
    TreeNode5.parent = root
    TreeNode1.parent = root

    TreeNode5.left = TreeNode6
    TreeNode5.right = TreeNode2
    TreeNode6.parent = TreeNode5
    TreeNode2.parent = TreeNode5

    TreeNode1.left = TreeNode0
    TreeNode1.right = TreeNode8
    TreeNode0.parent = TreeNode1
    TreeNode8.parent = TreeNode1

    TreeNode2.left = TreeNode7
    TreeNode2.right = TreeNode4
    TreeNode7.parent = TreeNode2
    TreeNode4.parent = TreeNode2

    p = TreeNode6
    q = TreeNode4

    print(solution.lowest_common_ancestor(root, p, q).val)