from typing import List

def issafe(m: List[List[int]], visited: List[List[int]], x: int, y: int, n: int) -> bool:
    if 0 <= x < n and 0 <= y < n and m[x][y] == 1 and visited[x][y] == 0:
        return True
    else:
        return False

def solve(m: List[List[int]], n: int, x: int, y: int, path: str, visited: List[List[int]], ans: List[str]):
    # base case
    if x == n - 1 and y == n - 1:
        ans.append(path)
        return
    
    visited[x][y] = 1
    
    # 4 choices = D, L, R, U
    
    # Down
    newx, newy = x + 1, y
    if issafe(m, visited, newx, newy, n):
        solve(m, n, newx, newy, path + 'D', visited, ans)
    
    # Left
    newx, newy = x, y - 1
    if issafe(m, visited, newx, newy, n):
        solve(m, n, newx, newy, path + 'L', visited, ans)
    
    # Right
    newx, newy = x, y + 1
    if issafe(m, visited, newx, newy, n):
        solve(m, n, newx, newy, path + 'R', visited, ans)
    
    # Up
    newx, newy = x - 1, y
    if issafe(m, visited, newx, newy, n):
        solve(m, n, newx, newy, path + 'U', visited, ans)
    
    visited[x][y] = 0

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        n = len(m)
        
        ans = []
        if m[0][0] == 0:
            return ans
    
        visited = [[0 for _ in range(n)] for _ in range(n)]
    
        path = ""
        solve(m, n, 0, 0, path, visited, ans)
        ans.sort()
        return ans
