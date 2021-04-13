from binarytree import Node


def invertBinaryTree(tree):
    if not tree:
        return None
    right,left = invertBinaryTree(tree.right),invertBinaryTree(tree.left)
    tree.left,tree.right = right,left
    return tree


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

print(invertBinaryTree(root))