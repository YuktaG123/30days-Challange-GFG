#User function Template for python3
class Solution:
    def isValid(self, str):
        list_of_address = str.split(".")
        
        # Check if there are exactly 4 segments
        if len(list_of_address) != 4:
            return 0
        
        for segment in list_of_address:
            # Check if the segment is composed of digits
            if not segment.isdigit():
                return 0
            
            # Check if the segment is within the valid range of 0 to 255
            if not 0 <= int(segment) <= 255:
                return 0
            
            # Check if the segment contains leading zeros
            if len(segment) > 1 and segment[0] == '0':
                return 0
        
        # If all conditions pass, return 1 indicating a valid IPv4 address
        return 1
