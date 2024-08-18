class Solution:
    def canSplit(self, arr):
        n=len(arr)
        sum=0
        for i in range(n):
            sum+=arr[i]
        x=sum/2
        sum1=0
        for i in range(n):
            sum1+=arr[i]
            if(sum1==x):
                return True
        return False
            
