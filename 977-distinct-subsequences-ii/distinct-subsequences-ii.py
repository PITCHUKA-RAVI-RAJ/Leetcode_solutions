class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=1
        l=[0]*26
        for ch in s:
            i=ord(ch)-ord('a')
            ndp=2*dp-l[i]
            l[i]=dp
            dp=ndp%MOD
        return (dp-1)%MOD