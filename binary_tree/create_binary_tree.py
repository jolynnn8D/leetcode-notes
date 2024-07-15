
from collections import defaultdict
from typing import Optional
from tree_node import TreeNode

class Solution:
    def create_binary_tree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        index = defaultdict(lambda: TreeNode())
        no_parent = set()
        has_parent = set()
        for d in descriptions:
            parent, child, is_left = d

            parent_node = index[parent]
            parent_node.val = parent
            child_node = index[child]
            child_node.val = child
            
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        
            if parent not in has_parent:
                no_parent.add(parent)

            no_parent.discard(child)
            has_parent.add(child)
    
        no_parent = list(no_parent)
        return index[no_parent[0]]

test_case_1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
root = Solution().create_binary_tree(test_case_1)
assert str(root) == "[50, 20, 80, 15, 17, 19, None]"
print(root)