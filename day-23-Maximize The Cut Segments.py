class Solution:
    def maximizeTheCuts(self,n,x,y,z):
        x,y,z=sorted([x,y,z])
        if n%x==0:
            return n//x
        from sys import setrecursionlimit
        setrecursionlimit(5*10**3)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(cur=n):
            nonlocal x,y,z
            if cur==0:
                return 0
            if cur<0:
                return -float('inf')
            return max(dfs(cur-x),dfs(cur-y),dfs(cur-z))+1
        ret=dfs()            
        return ret if ret!=-float('inf') else 0
