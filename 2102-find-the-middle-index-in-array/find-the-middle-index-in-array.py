class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        ps=[]
        ss=[]
        for i in range(n):
            ps.append(0)
            ss.append(0)
        for i in range(1,n):
            ps[i]=ps[i-1]+nums[i-1]
        for i in range(n-2,-1,-1):
            ss[i]=ss[i+1]+nums[i+1]
        for i in range(n):
            if ps[i]==ss[i]:
                return i
        return -1
