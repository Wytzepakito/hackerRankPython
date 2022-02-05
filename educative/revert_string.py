

def revert_string(string):
    if string== "":
        return ""
    l1 = [char for char in string]
    for i in range(len(l1)//2):

        temp = l1[i]

        l1[i] = l1[len(string) -1 - i]

        l1[len(l1) - 1 - i] = temp
    return "".join(l1)














print(revert_string("Wytze"))
print(revert_string("Marten"))

print(revert_string(""))