from random import randint
from typing import List

class QuickSort:
            
    def partition(self, low: int, high: int, arr: List[int]) -> int:
        pivot_index = randint(low, high-1)
        arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
        pivot = arr[low]
        i = low
        store = low + 1
        while i < high:
            if arr[i] < pivot:
                arr[i], arr[store] = arr[store], arr[i]
                store += 1
            i += 1
        arr[low], arr[store-1] = arr[store-1], arr[low]
        return store - 1
    
    def quick_sort(self, low: int, high: int, arr: List[int]):
        if low >= high:
            return

        idx = self.partition(low, high, arr)
        self.quick_sort(low, idx, arr)
        self.quick_sort(idx+1, high, arr)

    def sort(self, nums: List[int]) -> List[int]:
        self.quick_sort(0, len(nums), nums)
        return nums

if __name__ == "__main__":
    arr = [5,4,2,1,3]
    sorted_arr = QuickSort().sort(arr)
    print(sorted_arr)