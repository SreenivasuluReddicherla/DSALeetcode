class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, i, n = [], 0, len(words)

        while i < n:
            j, lineLen = i, 0
            while j < n and lineLen + len(words[j]) + (j - i) <= maxWidth:
                lineLen += len(words[j])
                j += 1

            spaces = maxWidth - lineLen
            gaps = j - i - 1
            line = ""

            # case 1: last line OR single word
            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaceEach, extra = divmod(spaces, gaps)
                for k in range(i, j):
                    line += words[k]
                    if k < j - 1:
                        line += " " * (spaceEach + (1 if extra > 0 else 0))
                        if extra > 0: extra -= 1

            res.append(line)
            i = j

        return res