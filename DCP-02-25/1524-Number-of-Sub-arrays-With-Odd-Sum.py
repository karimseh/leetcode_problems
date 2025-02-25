class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        pre_sum = 0
        odd = 0
        even = 1

        for n in arr:
            pre_sum += n
            if pre_sum % 2 == 0:
                count += odd #If current total is even, then subtracting any earlier odd total will give an odd subarray sum.
                even += 1 

            else: 
                count += even #If  current total is odd, then subtracting any earlier even total will give an odd subarray sum.
                odd += 1
            count %= MOD
        return count