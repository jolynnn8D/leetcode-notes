from tree_node import TreeNode, input_to_tree

class RecursiveSolution:
    def in_order_traversal(self, root: TreeNode) -> list[int]:
        arr = []
        self.helper(root, arr)
        return arr
    

    def helper(self, node: TreeNode, arr: list[int]):
        if not node:
            return 
            
        if node.left:
            self.helper(node.left, arr)
        
        arr.append(node.val)

        if node.right:
            self.helper(node.right, arr)

class IterativeSolution:
    def in_order_traversal(self, root: TreeNode) -> list[int]:
        curr = root
        stack = []
        arr = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                arr.append(node.val)
                curr = node.right
        
        return arr

class MorrisTraversalSolution:
    def in_order_traversal(self, root: TreeNode) -> list[int]:
        curr = root
        arr = []
        while curr:
            if curr.left:
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = curr
                temp = curr.left
                curr.left = None
                curr = temp
            else:
                arr.append(curr.val)
                curr = curr.right
        return arr
    
test_case_1 = [4, 2, 6, 1, 3, 5, 7]
root = input_to_tree(test_case_1)
print(RecursiveSolution().in_order_traversal(root))
print(IterativeSolution().in_order_traversal(root))
print(MorrisTraversalSolution().in_order_traversal(root))
