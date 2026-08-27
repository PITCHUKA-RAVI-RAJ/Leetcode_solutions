class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=set(nums)
        a=1
        for i in range(len(n)+1):
            if a not in n:
                return a
            else:
                a+=1
        return a