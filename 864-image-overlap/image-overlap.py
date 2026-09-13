class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        a=[]
        b=[]
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    a.append((i,j))
                if img2[i][j]==1:
                    b.append((i,j))
        ans = 0
        for dx in range(-n+1,n):
            for dy in range(-n+1,n):
                count=0
                for x,y in a:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if img2[nx][ny]==1:
                            count+=1
                ans=max(ans,count)
        return ans