class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove out-of-window indices
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # Maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            # Add max to result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result