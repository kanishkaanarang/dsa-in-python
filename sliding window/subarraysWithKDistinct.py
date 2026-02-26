class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(nums)):
            if count[nums[right]] == 0:
                k -= 1

            count[nums[right]] += 1

            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1

            result += right - left + 1

        return result