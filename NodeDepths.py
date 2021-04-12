from binarytree import Node

finalSum = 0


def nodeDepthHelper(node, currentSum):
    if node is None:
        return
    currentSum += 1
    global finalSum
    finalSum += currentSum
    nodeDepthHelper(node.left, currentSum)
    nodeDepthHelper(node.right, currentSum)

def nodeDepths(root):
    currentSum = 0
    nodeDepthHelper(root.left, currentSum)
    nodeDepthHelper(root.right, currentSum)
    return finalSum


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
print(nodeDepths(root))