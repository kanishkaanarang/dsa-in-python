class Solution:
    def moveZeroes(self, nums):
        position = 0 
        n = len(nums)
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1
        while position < n:
            nums[position] = 0
            position += 1

# or approach 2
class Solution:
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

# Time complexity: O(n)
# Space complexity: O(1)