'''
Search a 2D Matrix 

You are given an m x n 2-D integer array matrix and an integer target. Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1: Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000


'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        ROW, COL = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROW - 1
        
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        mid_row = (top + bottom) // 2
        
        l,r = 0, COL - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid_row][mid]:
                l = mid + 1
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                return True
        
        return False

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 11
    result = sol.searchMatrix(matrix, target)
    
    print(f" {target} is in the {matrix}?: {result}")
    
    
    # Time Complexity : O(Logm + Logm)
    #  Space Complexity: O(1)