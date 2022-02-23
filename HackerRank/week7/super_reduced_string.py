


def superReducedString(s):


    had_pair = True


    while(had_pair):
        had_pair = False

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                had_pair = True
                break

    if s == "":
        return "Empty String"
    else:
        return(s)








print(superReducedString("aab"))

print(superReducedString("abba"))