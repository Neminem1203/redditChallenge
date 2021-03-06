# https://leetcode.com/problems/valid-number/
def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """

    def isInt(char): # checks if char passed in is a number
        return ord('0') <= ord(char) <= ord('9')

    # 0 = full number, 1 = decimal, 2 = exponent
    has_num = False
    state = 0
    ind = 0
    if s[0] in ['-', '+']: # checks for a sign number
        ind += 1

    while ind < len(s):
        char = s[ind]
        if state == 0: # full number
            if char == ".":
                state = 1
            elif has_num and char.lower() == "e":
                state = 2
                has_num = False
                if ind + 1 < len(s) and s[ind + 1] in ['-', '+']:
                    ind += 1
            elif not isInt(char):
                return False
            else:
                has_num = True
        elif state == 1: # decimal
            if has_num and char.lower() == "e":
                state = 2
                has_num = False
                if ind + 1 < len(s) and s[ind + 1] in ['-', '+']:
                    ind += 1
            elif not isInt(char):
                return False
            else:
                has_num = True
        elif state == 2: #exponent
            if not isInt(char):
                return False
            else:
                has_num = True
        ind += 1
    return has_num


