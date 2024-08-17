class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # Calculate products of elements to the left of each element
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product *= nums[i]
        
        # Calculate products of elements to the right of each element and combine with the left products
        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        
        return ans
