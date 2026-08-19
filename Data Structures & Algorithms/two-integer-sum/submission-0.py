class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,n in enumerate(nums):
            rem = target-n
            
            if rem in hm:
                return [hm[rem],i]
            hm[n]=i
        
        