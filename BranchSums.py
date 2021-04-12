from binarytree import Node

def branchSumsHelper(root, currentSum, sums_array):
    if root.left is None and root.right is None:
        sums_array.append(currentSum)
        return

    if root.left is not None:
        currentSum += root.left.value
        branchSumsHelper(root.left, currentSum, sums_array)
        currentSum -= root.left.value

    if root.right is not None:
        currentSum += root.right.value
        branchSumsHelper(root.right, currentSum, sums_array)
        currentSum -= root.right.value


def branchSums(root):
    sums_array = []
    branchSumsHelper(root, root.value, sums_array)
    return sums_array


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
print(branchSums(root))