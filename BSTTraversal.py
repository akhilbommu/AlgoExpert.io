from binarytree import Node


def inOrderTraverse(tree, array):
    if tree.left is not None:
        inOrderTraverse(tree.left, array)
    array.append(tree.value)
    if tree.right is not None:
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    array.append(tree.value)
    if tree.left is not None:
        preOrderTraverse(tree.left, array)
    if tree.right is not None:
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree.left is not None:
        postOrderTraverse(tree.left, array)
    if tree.right is not None:
        postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(22)
root.left.left.left = Node(1)


print("Inorder Traversal ", inOrderTraverse(root,[]))
print("Preorder Traversal ",preOrderTraverse(root,[]))
print("Postorder Traversal ",postOrderTraverse(root,[]))