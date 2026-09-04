class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pm=[0]*n
        sm=[0]*n
        pm[0]=nums[0]
        for i in range(1,n):
            pm[i]=max(pm[i-1],nums[i])
        sm[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sm[i]=min(sm[i+1],nums[i])
        for i in range(n):
            if pm[i]-sm[i]<=k:
                return i
        return -1
