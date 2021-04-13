from binarytree import Node


def inorderTraversal(tree, inorderArray):
    if tree is not None:
        inorderTraversal(tree.left, inorderArray)
        inorderArray.append(tree.value)
        inorderTraversal(tree.right, inorderArray)
    return inorderArray


def findKthLargestValueInBst(tree, k):
    array = inorderTraversal(tree, [])
    return array[len(array) - k]


root = Node(15)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.left = Node(17)
root.right.right = Node(22)
root.left.left.left = Node(1)
root.left.left.right = Node(3)

print(findKthLargestValueInBst(root, 3))

"""
Java Solution
-------------
import java.util.*;

class Program {
  // This is an input class. Do not edit.
  static class BST {
    public int value;
    public BST left = null;
    public BST right = null;

    public BST(int value) {
      this.value = value;
    }
  }
	public int k,res=-1;
  public int findKthLargestValueInBst(BST tree, int k) {
    // Write your code here.
    this.k = k;
    find(tree);
    return res;
  }
    
  public void find(BST node) {
    if (node == null){
			return;
		}
    find(node.right);
    k -= 1;
    if(k == 0) {
      res = node.value;
      return;
  	}
    find(node.left);
    }
}
"""
