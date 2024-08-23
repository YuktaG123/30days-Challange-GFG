#User function Template for python3
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def solve(root,ans,level):
    #base case
    if root is None:
        return
    
    #we entered into new level
    if (level == len(ans)):
        ans.append(root.data)
        
    solve(root.left,ans,level+1)
    solve(root.right,ans,level+1)

def LeftView(root):
    ans = []
    solve(root,ans,0)
    return ans
