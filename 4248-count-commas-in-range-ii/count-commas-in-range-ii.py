class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n<1000000:
            return n-999
        elif n<1000000000:
            return (n-999)+(n-999999)
        elif n<1000000000000:
            return (n-999)+(n-999999)+(n-999999999)
        elif n<1000000000000000:
            return (n-999)+(n-999999)+(n-999999999)+(n-999999999999)
        else:
            return (n-999)+(n-999999)+(n-999999999)+(n-999999999999)+(n-999999999999999)