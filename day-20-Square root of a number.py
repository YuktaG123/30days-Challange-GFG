class Solution:
    def floorSqrt(self, n):
        #Repeated Subtraction Method by odd numbers
        i = 1
        c = 0
        while 1:
            n-=i
            if(n<0):
                break
            i+=2
            c+=1
        return c
