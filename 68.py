class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines: list[list[str]] = [[]]
        currLine = 0
        currCount = 0
        for word in words:
            lenWord = len(word)
            # print(word, currCount)
            if (lenWord + currCount) <= maxWidth:
                currCount += lenWord + 1
                lines[currLine].append(word)
            else:
                currCount = lenWord+1
                currLine += 1
                lines.append([])
                lines[currLine].append(word)
        # print(lines)
        ans: list[str] = []
        for i, line in enumerate(lines):
            if i == (len(lines) -1):
                break
            justified = ""
            total = sum([len(word) for word in line])
            spaces = maxWidth - total
            gap = spaces // (max(1, len(line)-1))
            rem = 0
            if (gap != 0):
                rem = spaces % (max(1, len(line)-1))
            print(total, spaces, gap, rem)
            for i, word in enumerate(line):
                justified += word
                if (i == (len(line) - 1)) and (len(line) != 1):
                    continue
                justified += " " * ((1 if rem else 0) + gap)
                rem = max(rem-1, 0)
            ans.append(justified)

        total = sum([len(word) for word in lines[-1]]) + len(lines[-1]) - 1
        spaces = maxWidth - total 
        ans.append(" ".join(lines[-1]) + " " * spaces)
        return(ans)


test = Solution()
sol = test.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"] , 20)
for line in sol:
    print(line, end = f"| {len(line)}\n")
# print(sol)
