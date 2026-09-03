class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=float('inf')
        ma=0
        for i in prices:
            if i<mi:
                mi=i
            elif i-mi>ma:
                ma=i-mi
        return ma
        
