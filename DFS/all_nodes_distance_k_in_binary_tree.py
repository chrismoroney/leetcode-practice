# All Nodes Distance K in Binary Tree

# Given the root of a binary tree, the value of a target node target, and an integer k, 
# return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distance_k(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        return_nodes = []
        
        def add_parent(current, parent):
            if current:
                current.parent = parent
                add_parent(current.left, current)
                add_parent(current.right, current)
        
        def dfs(current, distance, visited):
            if not current or current in visited:
                return
            visited.add(current)
            if distance == 0:
                return_nodes.append(current.val)
                return
            
            dfs(current.parent, distance-1, visited)
            dfs(current.left, distance-1, visited)
            dfs(current.right, distance-1, visited)

        add_parent(root, None)
        visited_nodes = set()
        dfs(target, k, visited_nodes)

        return return_nodes
    
if __name__ == "__main__":
    sol = Solution()
    
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    target = root.left
    k = 2
    print(sol.distance_k(root, target, k))