class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm={}
        res=[]
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        for i in hm:
            if hm[i]>(len(nums)//3):
                res.append(i)
        return res
        