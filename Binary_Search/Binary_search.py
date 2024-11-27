
'''
Binary Search 
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O(logn) time.

Example 1: Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Example 2: Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1

Constraints:
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
'''


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        n = len(nums)
        l,r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            # or we to avoid the overflow of the integer overflow we can use m = l + (r - l) / 2
            # Here we are basically calculating the range length (r - l) and then dividing the range by 2 and then adding this halfway point to l.
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1
     
    
    # search(nums=[-1,0,2,4,6,8], target=4)


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,2,4,9,8]
    target = 9
    
    print(f"nums: {nums}, target: {target}")
    result = sol.search(nums, target)
    print(f"Index of the target {target}: {result}")
    
    #  Time Complexity : O(Logn)
    #  Space Complexity : O(1)