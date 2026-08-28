class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        b=len(set(nums))
        c=len(nums)
        if b==c:
            return False
        else:
            return True