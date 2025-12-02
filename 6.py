class Solution:
    def convert(self, s: str, numRows: int) -> str:
        count = 0
        ls: list[str] =[]
        for _ in range(numRows):
            ls.append("")
        dir = -1 if numRows > 1 else 0
        for char in s:
            ls[count] += char
            if count == 0 or count == numRows-1:
                dir *= -1
            count += dir
        return ("".join(ls))


test = Solution()
sol = test.convert("PAYPALISHIRING", 1)
print(sol)

'''

PAYPALISHIRING
P Y L I H R N 3 
A P I S I I G 3

PAYPALISHIRING
P   A   H   N 5
A P L S I I G 3
Y   I   R 5

3

PAYPALISHIRING
P     I    N 7
A   L S  I G 5
Y A   H R 3
P     I 7

4


PAYPALISHIRING
P       H 9
A     S 7
Y   I 5
P L 3
A 9

p
'''
