

import re


def palindrome_sub(string, left, right):

    if left > right:
        return 0

    if string[left] == string[right]:

        return palindrome_sub(string, left + 1, right - 1) + 2


    return max(palindrome_sub(string, left, right -1), palindrome_sub(string, left + 1, right))




print(palindrome_sub("free bee", 0, len("free bee") - 1))
