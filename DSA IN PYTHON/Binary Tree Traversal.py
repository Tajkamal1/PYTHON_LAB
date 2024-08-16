# Binary Tree Traversal (In-order, Pre-order, Post-order)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# In-order traversal (Left, Root, Right)
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)


# Pre-order traversal (Root, Left, Right)
def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)


# Post-order traversal (Left, Right, Root)
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=" ")


# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order: ", end="")
in_order(root)  # Output: 4 2 5 1 3
print("\nPre-order: ", end="")
pre_order(root)  # Output: 1 2 4 5 3
print("\nPost-order: ", end="")
post_order(root)  # Output: 4 5 2 3 1
