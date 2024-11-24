# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def boundary_of_binary_tree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        def find_left_boundary(list_of_vals, root):
            if not root or (not root.left and not root.right):
                return list_of_vals
            list_of_vals.append(root.val)
            if root.left:
                return find_left_boundary(list_of_vals, root.left)
            else:
                return find_left_boundary(list_of_vals, root.right)

        def find_right_boundary(list_of_vals, root):
            if not root or (not root.left and not root.right):
                return list_of_vals
            if root.right:
                find_right_boundary(list_of_vals, root.right)
            else:
                find_right_boundary(list_of_vals, root.left)
            list_of_vals.append(root.val)
            return list_of_vals

        def is_leaf(root):
            return not root.left and not root.right

        def find_leaves(list_of_vals, root):
            if not root:
                return list_of_vals
            if is_leaf(root):
                if root != root_node:
                    list_of_vals.append(root.val)
            else:
                find_leaves(list_of_vals, root.left)
                find_leaves(list_of_vals, root.right)
            return list_of_vals

        root_node = root
        left_boundary = find_left_boundary([], root.left)
        right_boundary = find_right_boundary([], root.right)
        leaves = find_leaves([], root)

        total = [root.val] + left_boundary + leaves + right_boundary
        return total

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=4),
            right=TreeNode(
                val=5,
                left=TreeNode(val=7),
                right=TreeNode(val=8)
            )
        ),
        right=TreeNode(
            val=3,
            left=TreeNode(
                val=6,
                left=TreeNode(val=9),
                right=TreeNode(val=10)
            )
        )
    )
    print(sol.boundary_of_binary_tree(root))