class Solution:
    def celebrity(self, M):
        
        n = len(M)
        # Step 1: Find the candidate
        a = 0
        b = n - 1
        while a < b:
            if M[a][b] == 1:
                # a knows b, so a cannot be a celebrity
                a += 1
            else:
                # a does not know b, so b cannot be a celebrity
                b -= 1
        # Potential candidate
        candidate = a
        
        # Step 2: Verify the candidate
        # Check if the candidate is a real celebrity
        for i in range(n):
            if i != candidate:
                if M[candidate][i] == 1 or M[i][candidate] == 0:
                    return -1
        
        return candidate
