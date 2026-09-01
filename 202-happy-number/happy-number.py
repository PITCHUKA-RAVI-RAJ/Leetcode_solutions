class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            s=0
            while n>0:
                ld=n%10
                s=s+(ld*ld)
                n=n//10
            n=s
        if n==1:
            return True
        else:
            return False