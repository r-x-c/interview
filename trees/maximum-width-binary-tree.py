# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    store = [[]]
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inOrderMapper(root, 0)
        return self.calcMaxWidth()
    
    def inOrderMapper(self, root, level):
        if len(self.store) < level + 2:
            self.store.append([])
        # left
        if root.left != None:
            self.inOrderMapper(root.left, level + 1)
        else:
            self.store[level + 1].append(False)
        # root
        if root == None:
            self.store[level].append(False)
        else:
            self.store[level].append(True)
        # right
        if root.right != None:
            self.inOrderMapper(root.right, level + 1)
        else:
            self.store[level + 1].append(False)

    def calcMaxWidth(self):
        sol = -1
        for row in self.store:
            if True in row:
                firstFoundIdx = row.index(True)
                lastFoundIdx = len(row) - 1 - row[::-1].index(True)
                width = lastFoundIdx - firstFoundIdx + 1
                if width > sol:
                    sol = width
        return sol
