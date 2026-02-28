class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        remainder_count = {}
        remainder_count[0] = 1   # Base case
        
        current_sum = 0
        total_subarrays = 0
        
        for i in range(len(nums)):
            
            current_sum = current_sum + nums[i]
            
            remainder = current_sum % k
            
            # Handle negative remainders (important!)
            if remainder < 0:
                remainder = remainder + k
            
            if remainder in remainder_count:
                total_subarrays = total_subarrays + remainder_count[remainder]
            
            if remainder in remainder_count:
                remainder_count[remainder] = remainder_count[remainder] + 1
            else:
                remainder_count[remainder] = 1
        
        return total_subarrays