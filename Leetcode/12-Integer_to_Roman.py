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
    
class Solution2: # 4/21/2026
    def intToRoman(self, num: int) -> str:
        # This is a pretty straightforward problem, we just need to 
        # create a list of the symbols and their values, and then 
        # iterate through that list in reverse order, appending the 
        # symbols to our result string as we go.
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], 
                   ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], 
                   ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = "" # Initialize our result string
        for sym, val in reversed(symList): # Takes Roman symbols and values in reverse order
            if num // val: # If our number is greater than or equal to the value of the symbol
                count = num // val
                res += sym * count # Append the symbol to our result string count times
                num = num % val # Get the remainder of our number after subtracting the value of the symbol count times
        return res