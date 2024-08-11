#User function Template for python3

class Solution:
    def JobScheduling(self, Jobs, n):
        # Sort jobs based on decreasing order of profit
        sorted_Jobs = sorted(Jobs, key=lambda x: x.profit, reverse=True)
        
        # Find the maximum deadline
        max_deadline = max(job.deadline for job in Jobs)
        
        # Initialize the disjoint set array for union-find
        parent = list(range(max_deadline + 1))

        # Find function for union-find
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        # Union function for union-find
        def union(x, y):
            parent[find(x)] = find(y)
        
        sm_ct, ct = 0, 0
        
        for job in sorted_Jobs:
            # Find the latest available slot for the current job's deadline
            available_slot = find(min(job.deadline, max_deadline))
            
            if available_slot > 0:
                # If available, assign the job to this slot
                union(available_slot, available_slot - 1)
                sm_ct += job.profit
                ct += 1
        
        return [ct, sm_ct]
