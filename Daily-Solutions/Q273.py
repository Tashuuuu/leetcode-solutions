class Solution:
    def __init__(self):
        self.digit2s = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"
        }
        self.dozens2s = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        self.teens2s = {
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }

    def parse(self, num):
        if num == 0:
            return ""

        if num <= 10:
            return self.digit2s[num]

        if num <= 19:
            return self.teens2s[num]

        if num <= 99:
            tens, ones = divmod(num, 10)
            return f"{self.dozens2s[tens]}{' ' + self.digit2s[ones] if ones else ''}"

        hundreds, rest = divmod(num, 100)
        result = f"{self.digit2s[hundreds]} Hundred"
        if rest:
            result += f" {self.parse(rest)}"
        return result

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        billions, num = divmod(num, 10**9)
        millions, num = divmod(num, 10**6)
        thousands, num = divmod(num, 10**3)

        result = []
        if billions:
            result.append(f"{self.parse(billions)} Billion")
        if millions:
            result.append(f"{self.parse(millions)} Million")
        if thousands:
            result.append(f"{self.parse(thousands)} Thousand")
        if num:
            result.append(self.parse(num))

        return " ".join(result)
