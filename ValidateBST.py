from binarytree import Node


def validateBSTHelper(tree, maximum, minimum):
    if tree is None:
        return True
    elif (maximum is not None and tree.value >= maximum) or (minimum is not None and tree.value < minimum):
        return False
    else:
        return validateBSTHelper(tree.left, tree.value, minimum) and validateBSTHelper(tree.right, maximum, tree.value)


def validateBst(tree):
    return validateBSTHelper(tree, None, None)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.left = Node(13)
root.right.right = Node(22)
root.left.left.left = Node(1)
root.right.left.right = Node(14)

print(validateBst(root))