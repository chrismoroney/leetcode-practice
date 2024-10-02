# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def createTreeNode(nums, start, end):
            if start > end: 
                return None
            else:
                mid = start + (end-start) // 2
                root = TreeNode(nums[mid])
                root.left = createTreeNode(nums, start, mid-1)
                root.right = createTreeNode(nums, mid+1, end)
                return root

        if len(nums) == 0:
            return None
        else:
            return createTreeNode(nums, 0, len(nums)-1)