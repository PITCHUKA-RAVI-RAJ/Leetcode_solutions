class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            m=(l+r)//2
            def canfinish(weights,days,m):
                load=0
                d=1
                for w in weights:
                    if load+w<=m:
                        load+=w
                    else:
                        d+=1
                        load=w
                return d<=days
            n=canfinish(weights,days,m)
            if n:
                r=m
            else:
                l=m+1
        return l
