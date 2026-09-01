class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r=[]
        for i in range(left,right+1):
            temp=i
            sd=True
            while temp>0:
                d=temp%10
                if d==0 or i%d!=0:
                    sd=False
                    break
                temp//=10
            if sd:
                r.append(i)
        return r


        return l 
