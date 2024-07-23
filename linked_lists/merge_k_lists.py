from typing import List, Optional
from list_node import ListNode, list_to_ll
import heapq

""" 
Constraints:
1. k == lists.length
2. 0 <= k <= 10^4
3. 0 <= lists[i].length <= 500
4. -10^4 <= lists[i][j] <= 10^4
"""

class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        """
        Let n = total number of elements, k = number of lists, l = length of the lists
        Some points to note: 
        1. n = l * k
        2. k >> l
        Time complexity: O(kn) ~~O(n^2) since l is small
        """

        result = ListNode()
        curr = result
        while True:
            has_node = False
            smallest = float('inf')
            smallest_idx = -1
            for i, node in enumerate(lists):
                if not node:
                    continue
                else:
                    has_node = True
                    value = node.val
                    if value < smallest:
                        smallest = value
                        smallest_idx = i
            
            if not has_node:
                return result.next
            else:
                curr.next = ListNode(smallest)
                curr = curr.next
                lists[smallest_idx] = lists[smallest_idx].next

class HeapSolution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        To push the items onto the heap = O(nlogn)
        To pop each item = O(nlogn)
        """
        hq = []
        for ll in lists:
            while ll:
                heapq.heappush(hq, ll.val)
                ll = ll.next
        
        res = curr = ListNode()
        for _ in range(len(hq)):
            val = heapq.heappop(hq)
            curr.next = ListNode(val)
            curr = curr.next
        return res.next
    
tc1 = [[1,4,5],[1,3,4],[2,6]]

tc1_input = [list_to_ll(l) for l in tc1]
tc1_output = Solution().merge_k_lists(tc1_input)
print(tc1_output)

tc1_input = [list_to_ll(l) for l in tc1]
tc1_output = HeapSolution().merge_k_lists(tc1_input)
print(tc1_output)
