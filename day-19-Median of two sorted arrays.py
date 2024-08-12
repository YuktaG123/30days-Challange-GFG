class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        
        total = n1 + n2
        mid_ele = total // 2
        first = second = 0
        
        l1, r1 = 0, n1 - 1
        l2, r2 = 0, n2 - 1
        
        while l1 <= r1:
            # print("l1 ", l1, " ", r1)
            mid1 = l1 + (r1 - l1)//2
            mid2 = mid_ele - (mid1 - l1 + 1) + l2 - 1
            if mid1 + 1 < len(arr1) and arr2[mid2] > arr1[mid1+1]:
                mid_ele -= (mid1 - l1 + 1)
                l1 = mid1 + 1
            elif mid2 + 1 < len(arr2) and arr1[mid1] > arr2[mid2+1]:
                r1 = mid1 - 1
            else:
                first = max(arr1[mid1], arr2[mid2])
                second = None
                if mid1 + 1 < len(arr1) and mid2+1 < len(arr2):
                    second = min(arr1[mid1+1], arr2[mid2+1])
                elif mid1 + 1 < len(arr1):
                    second = arr1[mid1+1]
                else:
                    second = arr2[mid2+1]
                break
            
        return first + second
