class Solution:
    def isPalindrome(self, x: int) -> bool:
        left_part = str(x)[:len(str(x))//2]
        right_part = str(x)[len(str(x))//2:]
        if len(left_part) == len(right_part):
            if left_part == right_part[::-1]:
                return True
        else:
            if left_part == right_part[1:]:
                return True
        return False


