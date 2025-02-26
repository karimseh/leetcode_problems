class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_abs_sum = nums[0]
        current_sum = nums[0]
        for i  in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_abs_sum = max(max_abs_sum, current_sum)
        min_abs_sum = nums[0]
        current_sum = nums[0]
        for i  in range(1, len(nums)):
            current_sum = min(nums[i], current_sum + nums[i])
            min_abs_sum = min(min_abs_sum, current_sum)
            
        return max(max_abs_sum, abs(min_abs_sum))
        