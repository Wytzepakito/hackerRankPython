


def recursive_perms(string, new_string, new_char, perms, n):
    new_string += new_char
    if len(new_string) == n:
        if new_string in perms:
            print("Created a duplicate")
        perms.append(new_string)

    for i in range(len(string)):

        copy_string = string[:i] + string[i + 1:]
        recursive_perms(copy_string, new_string, string[i],  perms, n)



def recursive_perms2(string, perms):
    

    char = string[0]
    new_string = string[1:]
    print(perms)
    new_perms = []
    for perm in perms:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + char  + perm[i:]
            new_perms.append(new_perm)


    if new_string == "":
        return new_perms
    else:
        return recursive_perms2(new_string, new_perms)











perms = ["A"]
string = "BCD"

# print(recursive_perms(list(string), "", "",  perms, len(string)))

# print(len(perms))
# print(len(set(perms)))

print(recursive_perms2(string,perms))














