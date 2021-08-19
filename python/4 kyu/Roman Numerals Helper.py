"""TODO: create a RomanNumerals helper object"""
SYMBOLS = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
VALS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


class RomanNumerals:

    def to_roman(n):
        roman = ''
        i = 0
        while n > 0:
            if n >= VALS[i]:
                n -= VALS[i]
                roman += SYMBOLS[i]
            else:
                i += 1
        return roman

    def from_roman(strng):
        n = 0
        while strng:
            if strng[:2] in SYMBOLS:
                n += VALS[SYMBOLS.index(strng[:2])]
                strng = strng[2:]
            else:
                n += VALS[SYMBOLS.index(strng[0])]
                strng = strng[1:]
        return n