class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}
        for i in strs:
            k="".join(sorted(i))
            if k not in g:
                g[k]=[]
            g[k].append(i)
        return list(g.values())
