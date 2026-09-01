class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l=0
        r=0
        s=1
        c=0
        while r<len(nums):
            s*=nums[r]
            while(s>=k):
                s=s//nums[l]
                l+=1
            c+=r-l+1
            r+=1
        return c