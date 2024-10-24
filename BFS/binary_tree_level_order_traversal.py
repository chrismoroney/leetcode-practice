# Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """

    def bfs(root):
        if not root:
            return []
            
        list_of_levels = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            list_of_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                list_of_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)

            list_of_levels.append(list_of_nodes)
            
        return list_of_levels

    ans = bfs(root)

    return ans

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(level_order(root))
