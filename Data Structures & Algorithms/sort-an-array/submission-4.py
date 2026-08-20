import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def QuickSort(a):
            if len(a) <= 1:
                return a
            pi = random.choice(a)         
            left  = [x for x in a if x < pi]
            mid   = [x for x in a if x == pi]
            right = [x for x in a if x > pi]
            return QuickSort(left) + mid + QuickSort(right)

        return QuickSort(nums)