class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)
    
    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)      

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index + 1 < len(self.nodes_sorted)


if __name__ == "__main__":
    root = TreeNode(7, left=TreeNode(3), right=TreeNode(15, left=TreeNode(9), right=TreeNode(20)))
    bSTIterator = BSTIterator(root)
    print(bSTIterator.next())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())
    print(bSTIterator.next())
    print(bSTIterator.hasNext())