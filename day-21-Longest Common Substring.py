#User function Template for python3
class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        n, m = len(str1), len(str2)
        lo, hi = 0, min(n, m)+1
        
        def ok(l):
            for i in range(len(str1)-l+1):
                if str2.find(str1[i:i+l]) != -1:
                    return True
            return False
            
        while lo < hi:
            mi = lo+(hi-lo)//2
            if ok(mi):
                lo = mi+1
            else:
                hi = mi
        
        return lo-1
