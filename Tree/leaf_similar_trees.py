# Leaf-Similar Trees
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# [3,5,1,6,2,9,8,null,null,7,4]
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def leaf_similar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        root1_list = []
        root2_list = []

        def preorder(root, root_list):
            if not root:
                return
            # is a leaf
            if not root.left and not root.right:
                root_list.append(root.val)

            preorder(root.left, root_list)
            preorder(root.right, root_list)


        preorder(root1, root1_list)
        preorder(root2, root2_list)
        
        return root1_list == root2_list
    
if __name__ == "__main__":
    solution = Solution()
    root1 = TreeNode(3,left=TreeNode(5,left=TreeNode(6),right=TreeNode(2, left=TreeNode(7),right=TreeNode(4))),right=TreeNode(1, left=TreeNode(9),right=TreeNode(8)))
    root2 = TreeNode(3,left=TreeNode(5,left=TreeNode(6),right=TreeNode(7)),right=TreeNode(1,left=TreeNode(4),right=TreeNode(2, left=TreeNode(9), right=TreeNode(8))))
    
    print(solution.leaf_similar(root1, root2))
