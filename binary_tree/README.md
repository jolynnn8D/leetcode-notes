# Binary Trees

| Problem                                                                                                                     | Code                              | Tags                                 |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------|--------------------------------------|
| [Binary Tree In Order Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)                              | [Python3](./inorder_traversal.py) | In-order Traversal, Morris Traversal |
| [Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/) | [Python3](./bst_to_gst.py)        | Reverse In-order Traversal           |

## Algorithms

### Morris Traversal
- In-order tree traversal algorithm that does not employ recursion or stack
- Forms a type of [threaded binary tree](https://en.wikipedia.org/wiki/Threaded_binary_tree)
- Creates links between parent and child nodes such that the links follow the order of traversal 