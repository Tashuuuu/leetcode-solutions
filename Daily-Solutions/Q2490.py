class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        s = sentence.split(' ')
        n = len(s)

        if n == 1:
            return True
        else:
            i = 0
            while i < n - 1:
                if s[i][-1] != s[i + 1][0]:
                    return False
                    break
                i += 1
            return True
