class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        co=[0]*10
        for i in digits:
            co[i]+=1
        ans=0
        for i in range(100,1000):
            if i%2!=0:
                continue
            a=i//100
            b=(i//10)%10
            c=i%10
            if a==b==c:
                if co[a]>=3:
                    ans+=1
            elif a==b:
                if co[a]>=2 and co[c]>=1:
                    ans+=1
            elif a==c:
                if co[a]>=2 and co[b]>=1:
                    ans+=1
            elif b==c:
                if co[b]>=2 and co[a]>=1:
                    ans+=1
            else:
                if co[a]>=1 and co[b]>=1 and co[c]>=1:
                    ans+=1
        return ans