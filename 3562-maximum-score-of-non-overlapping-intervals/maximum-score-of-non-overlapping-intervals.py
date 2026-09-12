class Solution:
    def maximumWeight(self, intervals):

        intervals = [(l,r,w,i) for i,(l,r,w) in enumerate(intervals)]
        intervals.sort()
        n=len(intervals)

        from bisect import bisect_right

        starts=[]
        for l,r,w,i in intervals:
            starts.append(l)

        dp={}

        def solve(i,c):

            if i==n or c==4:
                return (0,[])

            if (i,c) in dp:
                return dp[(i,c)]

            sc1,ans1=solve(i+1,c)

            l,r,w,index=intervals[i]

            j=bisect_right(starts,r)

            sc2,ans2=solve(j,c+1)
            sc2+=w
            ans2=ans2+[index]

            if sc2>sc1:
                ans=(sc2,ans2)

            elif sc1>sc2:
                ans=(sc1,ans1)

            else:
                if sorted(ans2)<sorted(ans1):
                    ans=(sc2,ans2)
                else:
                    ans=(sc1,ans1)

            dp[(i,c)]=ans

            return ans

        return sorted(solve(0,0)[1])