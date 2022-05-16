from enum import Enum

class RomanNumeral(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

def romanToInt(s: str) -> int:
    pos = 0
    answer = 0

    while (pos != len(s) - 1):
        num = RomanNumeral[s[pos]].value
        
        match num: # check for cases where we need to subtract
            case 1:
                if (s[pos + 1] == 'V' or s[pos + 1] == 'X'):
                    answer -= num
                else:
                    answer += num
            case 10:
                if (s[pos + 1] == 'L' or s[pos + 1] == 'C'):
                    answer -= num
                else:
                    answer += num                    
            case 100:
                if (s[pos + 1] == 'D' or s[pos + 1] == 'M'):
                    answer -= num
                else:
                    answer += num
            case _:
                answer += num     
        pos += 1
    
    # final char
    num = RomanNumeral[s[pos]].value
    answer += num

    return answer

print(romanToInt("III"))