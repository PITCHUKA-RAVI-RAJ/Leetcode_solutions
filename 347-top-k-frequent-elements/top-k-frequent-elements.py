class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        s=sorted(f,key=f.get,reverse=True)
        return s[:k]