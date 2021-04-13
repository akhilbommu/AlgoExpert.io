from binarytree import Node


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
    root_node = Node(preOrderTraversalValues[0])
    index = 1
    while index < len(preOrderTraversalValues) and preOrderTraversalValues[index] < root_node.value:
        index += 1
    root_node.left = reconstructBst(preOrderTraversalValues[1:index])
    root_node.right = reconstructBst(preOrderTraversalValues[index:])
    return root_node

"""
root = Node(10)
root.left = Node(4)
root.right = Node(17)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(19)
root.left.left.left = Node(1)
root.right.right.left = Node(18)
"""

print(reconstructBst([10, 4, 2, 1, 5, 17, 19, 18]))
print(reconstructBst([5, -10, -5, 6, 9, 7]))