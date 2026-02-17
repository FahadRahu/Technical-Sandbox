class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_numeral = ""
        for i in range(len(values)):
            while num >= values[i]:
                roman_numeral += symbols[i]
                num -= values[i]

        return roman_numeral
    
    def intToRoman2(self, num: int) -> str:
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], 
                   ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], 
                   ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = ""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res += sym * count
                num = num % val
        return res