class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i, 0) + 1
        
        for num, count in hm.items():
            if count > len(nums) // 2:
                return num