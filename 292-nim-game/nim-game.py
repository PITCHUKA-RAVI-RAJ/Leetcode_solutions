class Solution:
    def canWinNim(self, n: int) -> bool:
        if n<=3:
            return True
        else:
            if n-3>0:
                if(n%4==0):
                    return False
                else:
                    return True
            else:
                return False