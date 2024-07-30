#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr):
        n = len(arr)
        m = len(arr[0])
        
        max_ones_row = -1  # Initialize the index of the row with the maximum number of 1s
        max_ones_count = 0  # Initialize the count of maximum 1s found in a row

        # Iterate through each row of the matrix
        for i in range(n):
            count = 0  # Initialize the count of 1s in the current row

            # Iterate through each column of the current row
            for j in range(m):
                if arr[i][j] == 1:
                    count += 1  # Increment count if the current element is 1

            # Check if the count of 1s in the current row is greater than the maximum count found so far
            if count > max_ones_count:
                max_ones_count = count  # Update the maximum count
                max_ones_row = i  # Update the index of the row with maximum 1s

        return max_ones_row  # Return the index of the row with maximum 1s
