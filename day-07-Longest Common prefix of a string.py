class Solution:
    def longestCommonPrefix(self, arr):
        n = len(arr)
        p=max(arr)
        q=min(arr)
        m=len(q)
        ans=""
        for i in range(m):
            if q[i]==p[i]:
                ans+=q[i]
            else:
                break
        if ans:
            return ans
        else:
            return -1
