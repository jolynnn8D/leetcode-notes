# Problem 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

from tree_node import TreeNode, input_to_tree

'''
This solution does a reverse in-order traversal, returning the sum of the entire tree from the helper function
The GST value requires the addition of the entire right subtree & all subtrees of the right (greater) parent
Time complexity: O(n)
Space complexity: O(n) -- due to the call stack
'''
class Solution:
    def bst_to_gst(self, root: TreeNode) -> TreeNode:
        self.convert_and_sum(0, root)
        return root
    
    def convert_and_sum(self, right_parent: int, node: TreeNode) -> int:
        value = node.val
        right_subtree = self.convert_and_sum(right_parent, node.right) if node.right else 0
        node.val = value + right_parent + right_subtree
        left_subtree = self.convert_and_sum(node.val, node.left) if node.left else 0
        return right_subtree + left_subtree + value


test_case_1 = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root = input_to_tree(test_case_1)
print(root)
print(Solution().bst_to_gst(root))


