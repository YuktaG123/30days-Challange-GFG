class Solution:
    def Maximize(self, a): 
        
        a.sort()
        sm = 0 
        for i in range(len(a)): sm = (sm + a[i] * i % 1000000007) % 1000000007
        return sm
     
