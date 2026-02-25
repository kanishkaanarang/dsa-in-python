class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        curr_sum = 0
        ans = len(nums) + 1   # acts like infinity

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        if ans == len(nums) + 1:
            return 0
        return ans
