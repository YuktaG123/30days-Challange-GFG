import heapq
class Solution:

    def kthSmallest(self, arr,k):
        
        # Convert the list into a min-heap
        heapq.heapify(arr)
        
        # Extract the minimum element k times
        for _ in range(k - 1):
            heapq.heappop(arr)
        
        # The next element is the k-th smallest element
        return heapq.heappop(arr)
        
