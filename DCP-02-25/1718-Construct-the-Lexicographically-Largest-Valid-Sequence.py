class Solution:
    # find bigest missing num


    def backtrack(self, index, res, seen_nums, n):
        if index == len(res):
            return True
        
        if res[index] != 0:
            return self.backtrack(index + 1, res, seen_nums, n)
        
        for num in range(n, 0, -1):
            if seen_nums[num]:
            #pass to next
                continue
            
            seen_nums[num] = True
            res[index] = num

            if num== 1:
                if self.backtrack(index + 1, res, seen_nums, n) :
                    return True
            elif (index + num < len(res) and res[index + num] == 0):
                res[index + num] = num

                if self.backtrack(index + 1, res, seen_nums, n):
                    return True

                res[index + num] = 0
            res[index] = 0
            seen_nums[num] = False
        return False 

       

    def constructDistancedSequence(self, n: int) -> List[int]:
        # init
        res = [0] * ((n * 2) - 1)
        seen_nums = [False] * (n + 1)

        self.backtrack(0, res, seen_nums, n)

        return res
