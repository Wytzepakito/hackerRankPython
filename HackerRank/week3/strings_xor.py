def strings_xor(s, t):
    l1 = []
    for i in range(len(s)):
        if s[i] == t[i]:
            l1.append('0')
        else:
            l1.append('1')

    return "".join(l1)




print(strings_xor("10101", "00101"))
