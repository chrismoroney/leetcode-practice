# Range Sum of BST

# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def range_sum_BST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(root):
            ans = 0
            if root:
                if low <= root.val <= high:
                    ans += root.val
                
                if low < root.val:
                    ans += dfs(root.left)
                
                if root.val < high:
                    ans += dfs(root.right)
            else:
                return 0
                
            return ans
        
        total_sum = dfs(root)
        return total_sum
    
if __name__ == "__main__":
    solution = Solution()

#                       10
#                   /       \
#               5               15
#           /       \               \
#       3               7               18

    root = TreeNode(10, left=TreeNode(5, left=TreeNode(3), right=TreeNode(7)), right=TreeNode(15, right=TreeNode(18)))
    low = 7
    high = 15
    print(solution.range_sum_BST(root, low, high))