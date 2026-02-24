class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        p = 1
        i = 0
        ans = 0
        n = len(nums)

        for j in range(n):
            p *= nums[j]

            while p >= k:
                p //= nums[i]
                i += 1

            ans += (j - i + 1)
            
        return ans