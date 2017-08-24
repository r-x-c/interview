# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.leafSumHelper(root, False)
    
    def leafSumHelper(self, root, isLeft):
        # base case
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val if isLeft else 0
        return self.leafSumHelper(root.left, True) + self.leafSumHelper(root.right, False)

        
        


# Test cases
# [3]

# [3,9,20,null,null,15,7]

# [3,9,20,null,null,15,7, null, 16, 5, null, null, null, 6]
