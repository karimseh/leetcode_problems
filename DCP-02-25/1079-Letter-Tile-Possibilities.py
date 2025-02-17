class Solution:
    def backtrack(
        self, seen_seq: Set[str], remaining_letters: List[str], current_seq: str
    ):
        if len(remaining_letters) == 0:
            return None
        for index, letter in enumerate(remaining_letters):
            # print(current_seq, remaining_letters, seen_seq)
            if current_seq + letter in seen_seq:
                continue
            # update current seq and add it to seen
            current_seq += letter
            seen_seq.add(current_seq)

            self.backtrack(
                seen_seq,
                remaining_letters[:index] + remaining_letters[index + 1 :],
                current_seq,
            )
            current_seq = current_seq[:-1]

    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        self.backtrack(res, list(tiles), "")
        return len(res)
