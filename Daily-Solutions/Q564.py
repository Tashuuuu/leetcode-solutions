class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        num = int(n)

        # Bounds. Largest (n - 1) digit and smallest (n + 1) digit
        left = 10 ** (m - 1) - 1
        right = 10 ** m + 1

        # Calculating all the values.
        isOdd = m & 1 # 0 if even and 1 if odd
        tillMid = int(n[: (m >> 1) + isOdd])
        smallerPalin = int(str(tillMid - 1) + str(tillMid - 1)[-1 -isOdd :: -1])
        same = int(str(tillMid) + str(tillMid)[-1 -isOdd :: -1])
        largerPalin = int(str(tillMid + 1) + str(tillMid + 1)[-1 -isOdd :: -1])

        if same == num:
            return str(min(
                [left, right, smallerPalin, largerPalin],
                key = lambda x: (abs(x - num), x)))
        else:
            return str(min(
                [left, right, smallerPalin, same, largerPalin],
                key = lambda x: (abs(x - num), x)))
