class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        v="aeiouAEIOU"
        l=0
        r=len(s)-1
        while l<r:
            if s[l] not in v:
                l+=1
            elif s[r] not in v:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
