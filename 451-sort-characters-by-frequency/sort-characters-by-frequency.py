class Solution:
    def frequencySort(self, s: str) -> str:
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        ch=sorted(f,key=f.get,reverse=True)
        a=""
        for i in ch:
            a+=i*f[i]
        return a