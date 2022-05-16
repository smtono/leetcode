def longestCommonPrefix(strs) -> str:
    base = strs[0]

    i = 1
    while i is not len(strs):
       base = find_match(base, strs[i])
       i += 1
    return base
        

def find_match(curr, str2) -> str:
    result = ""
    stop = len(curr) - 1 if len(curr) <= len(str2) else len(str2) - 1 # find shorter of 2 strings

    i = 0
    while i is not stop + 1:
        if (curr[i] == str2[i]): # if chars match, add to result
            result += curr[i]
            i += 1
        else:
            break

    return result

strs = ["geeksforgeeks", "geeks", "geek", "geezer"]
print("Longest prefix: ", longestCommonPrefix(strs))