class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = ""
        i = 0
        while i < len(s):
            if result[-len(part) :] == part:

                result = result[: len(result) - len(part)]
                result += s[i]
            else:
                result += s[i]

            i += 1
        if result[-len(part) :] == part:
            result = result[: len(result) - len(part)]

        return result
