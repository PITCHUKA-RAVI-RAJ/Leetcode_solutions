class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r_map={0:-1}
        pre=0
        for i,num in enumerate(nums):
            pre+=num
            rem=pre%k
            if rem in r_map:
                ind=i-r_map[rem]
                if ind>=2:
                    return True
            else:
                r_map[rem]=i
        return False
