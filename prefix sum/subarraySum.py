class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        seen = {}
        seen[0] = 1   # Base case: one way to have prefix sum 0
        current_sum = 0
        total_subarrays = 0
        
        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            required_sum = current_sum - k

            if required_sum in seen:
                total_subarrays = total_subarrays + seen[required_sum]

            if current_sum in seen:
                seen[current_sum] = seen[current_sum] + 1
            else:
                seen[current_sum] = 1

        return total_subarrays