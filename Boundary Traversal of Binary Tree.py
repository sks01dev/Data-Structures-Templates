'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    # Write your code here.
    res = []
    if not root:
        return res
    res.append(root.data)

    def leftB(node):
        while node:
            if node.left or node.right:
                res.append(node.data)
            
            node = node.left if node.left else node.right

    def leafNodes(node):
        if not node:
            return
        
        if not node.left and not node.right:
            res.append(node.data)
            return

        leafNodes(node.left)
        leafNodes(node.right)

    def rightB(node):
        st = []
        while node:
            if node.left or node.right:
                st.append(node.data)

            node = node.right if node.right else node.left

        while st:
            res.append(st.pop())

    leftB(root.left)
    leafNodes(root)
    rightB(root.right)

    return res




