class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        
        sorted_nums = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        
        res = []
        count = 0
        for i in sorted_nums:
            if count == k:
                break
            res.append(i)
            count += 1
        
        return res