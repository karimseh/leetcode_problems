class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        values = {}
        result = -1
        for num in nums:
            digit_sum = sum(map(int, str(num)))
            if digit_sum in values:
                last_value = values.get(digit_sum)[-1]
                values[digit_sum] = sorted(values.get(digit_sum) + [num])
                if last_value + num > result:
                    result = last_value + num
            else:
                values[digit_sum] = [num]

        return result
