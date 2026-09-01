from collections import deque
class Solution:
    def minMoves(self,classroom:list[str],energy:int)->int:
        m=len(classroom)
        n=len(classroom[0])
        l=[]
        st=None
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    st=(i,j)
                elif classroom[i][j]=='L':
                    l.append((i,j))
        q=deque([(st[0],st[1],energy,0,0)])
        be={(st[0],st[1],0):energy}
        while q:
            r,c,e,mask,moves=q.popleft()
            if mask==(1<<len(l))-1:
                return moves
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                x=r+dr
                y=c+dc
                if x<0 or x>=m or y<0 or y>=n:
                    continue
                if classroom[x][y]=='X':
                    continue
                ne=e-1
                if ne<0:
                    continue
                nm=mask
                for i in range(len(l)):
                    if (x,y)==l[i]:
                        nm=nm|(1<<i)
                if classroom[x][y]=='R':
                    ne=energy
                if be.get((x,y,nm),-1)<ne:
                    be[(x,y,nm)]=ne
                    q.append((x,y,ne,nm,moves+1))
        return -1