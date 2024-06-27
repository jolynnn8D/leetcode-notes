class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        arr = []
        queue = [(self, 0)]
        max_depth = 0
        for node, depth in queue:
            max_depth = max(max_depth, depth)
            if node:
                arr.append(node.val)
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
            else:
                arr.append(None)
        num_elem = 2**depth - 1
        return str(arr[:num_elem])
    
def input_to_tree(arr):
    if not arr:
        return None
    
    it = iter(arr)
    root = TreeNode(next(it))
    queue = [root]
    for node in queue:
        left_val = next(it, None)
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        right_val = next(it, None)
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)
    return root