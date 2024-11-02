# Lowest Common Ancestor of a Binary Tree 3

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: 
# "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants 
# (where we allow a node to be a descendant of itself)."


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution(object):
    def get_depth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.parent
        return depth

    def lowest_common_ancestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)

        for i in range(p_depth - q_depth):
            p = p.parent
        for j in range(q_depth - p_depth):
            q = q.parent

        while p != q:
            p = p.parent
            q = q.parent
        
        return p
    
if __name__ == "__main__":
    solution = Solution()
    root = Node(3)
    node5 = Node(5)
    node1 = Node(1)
    node6 = Node(6)
    node2 = Node(2)
    node0 = Node(0)
    node8 = Node(8)
    node7 = Node(7)
    node4 = Node(4)

    root.left = node5
    root.right = node1
    node5.parent = root
    node1.parent = root

    node5.left = node6
    node5.right = node2
    node6.parent = node5
    node2.parent = node5

    node1.left = node0
    node1.right = node8
    node0.parent = node1
    node8.parent = node1

    node2.left = node7
    node2.right = node4
    node7.parent = node2
    node4.parent = node2

    p = node5
    q = node4

    print(solution.lowest_common_ancestor(p, q).val)