class Solution:
    def checkNumber(self, num: int, target: int) -> list[int]:
        if target < 0 or num < target:
            return False

        if num == target:
            return True
        # if target - numRight = numLeft --> target = numRight + numLeft
        return (
            self.checkNumber(num // 10, target - num % 10)
            or self.checkNumber(num // 100, target - num % 100)
            or self.checkNumber(num // 1000, target - num % 1000)
        )

    def punishmentNumber(self, n: int) -> int:
        punishment_n = 0
        for i in range(1, n + 1):
            if self.checkNumber(i * i, i):
                punishment_n += i * i
        return punishment_n
