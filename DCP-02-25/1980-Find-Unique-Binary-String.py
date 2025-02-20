class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        all_combinations = list(product([0, 1], repeat=len(nums)))
        combinations_str = [''.join(map(str, combo)) for combo in all_combinations]
        return list(set(combinations_str) - set(nums))[0]