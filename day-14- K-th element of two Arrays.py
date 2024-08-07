class Solution:
    def kthElement(self, k, arr1, arr2):
        l=arr1+arr2
        l.sort()
        return l[k-1]
