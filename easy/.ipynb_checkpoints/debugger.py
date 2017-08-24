class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        root = TreeNode(t1.val + t2.val)
        self.mergeLeft(root, t1.left, t2.left)
        self.mergeRight(root, t1.right, t2.right)
        return root

    def mergeLeft(self, root, t1, t2):
        if t1 is None and t2 is None:
            return
        if t1 is None:
            root.left = t2
        elif t2 is None:
            root.left = t1
        else:
            _ = TreeNode(t1.val + t2.val)
            root.left = _
            self.mergeLeft(root.left, t1.left, t2.left)
            self.mergeRight(root.left, t1.right, t2.right)

    def mergeRight(self, root, t1, t2):
        if t1 is None and t2 is None:
            return
        if t1 is None:
            root.right = t2
        elif t2 is None:
            root.right = t1
        else:
            _ = TreeNode(t1.val + t2.val)
            root.right = _
            self.mergeRight(root.right, t1.right, t2.right)
            self.mergeLeft(root.right, t1.left, t2.left)




class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printInOrder(node):
    if node == None:
        return
    #left
    printInOrder(node.left)
    #center
    print(node.val)
    #right
    printInOrder(node.right)

def treeEqual(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.val != t2.val:
        return False
    return treeEqual(t1.left, t2.left) and treeEqual(t1.right, t2.right)


t1 = TreeNode(1)
a = TreeNode(3)
b = TreeNode(2)
t1.left = a
t1.right = b
c = TreeNode(5)
a.left = c

t2 = TreeNode(2)
x = TreeNode(1)
y = TreeNode(3)
t2.left = x
t2.right = y
z = TreeNode(4)
x.right = z
q = TreeNode(7)
y.right = q

tS = TreeNode(3)
s1 = TreeNode(4)
s2 = TreeNode(5)
tS.left = s1
tS.right = s2
s3 = TreeNode(5)
s4 = TreeNode(4)
s1.left = s3
s1.right = s4
s5 = TreeNode(7)
s2.right = s5

sol = Solution()
printInOrder(t1)
print("\n----\n")
printInOrder(t2)
print("\n----\n")
printInOrder(tS)
print("\n----\n")
printInOrder(sol.mergeTrees(t1,t2))