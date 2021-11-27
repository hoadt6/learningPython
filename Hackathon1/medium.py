# from unittest.main import _TestRunner
def anagram_number(number):
    number = str(number)
    reverse_num = number[::-1]
    if (number == reverse_num):
     return True
    else: return False

def roman_to_int(s):
    mapping = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M':1000}
    number = temp = 0
    for i in range(0, len(s)):
        value = mapping.get(s[i])
        if value > temp:
            number = number  + (value - 2 * temp)
        else: 
            number = number + value
        temp = value
    return number
