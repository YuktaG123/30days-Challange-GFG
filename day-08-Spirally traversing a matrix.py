
class Solution:
    def spirallyTraverse(self,matrix): 
        r = len(matrix)
        c = len(matrix[0])
        top = 0
        left = 0
        right = c-1
        bottom = r-1
        res = []
        
        while left <= right and top <= bottom:#todo condition
            #first row
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top +=1
            
            #right row
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            
            #botom row
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # left row
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
                    
