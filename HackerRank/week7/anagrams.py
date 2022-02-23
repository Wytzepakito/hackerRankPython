
import math


def sherlockAndAnagrams(s):

    num = 0
    for length in range( 1,len(s)):
        dic = {}

        for i in range(len(s) - (length - 1)):
            lower = i
            upper = i + length
            sub_set = s[lower:upper]
            sorted_string = "".join(sorted(sub_set))
            if sorted_string in dic:
                num += dic[sorted_string]
                dic[sorted_string] += 1
            else:
                dic[sorted_string] = 1



  
    return num
        

print(sherlockAndAnagrams("kkkk"))
print(sherlockAndAnagrams("ifailuhkqq"))
print(sherlockAndAnagrams("cdcd"))
print(sherlockAndAnagrams("abba"))
print(sherlockAndAnagrams("abcd"))
