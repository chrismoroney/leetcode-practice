# Sum of Nodes with Even-Valued Grandparents

# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. 
# If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root: TreeNode) -> int:
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    def dfs(child, parent, grandparent):
        if not child:
            return 0
        
        total_sum = 0
        if grandparent and grandparent.val % 2 == 0:
            total_sum += child.val
        
        total_sum += dfs(child.left, child, parent)
        total_sum += dfs(child.right, child, parent)

        return total_sum
    
    return dfs(root, None, None)

if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(5)

    print(sumEvenGrandparent(root))
        