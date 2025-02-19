class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = [""]
        counter =0

        while happy_strings:
            current_str = happy_strings.pop()

            if(len(current_str) == n):
                counter += 1
                if(counter == k):
                    return current_str
                continue
            
            for char in ['c', 'b', 'a']:
                if(len(current_str) == 0 or current_str[-1] != char):
                    happy_strings.append(current_str + char)

        return ""
