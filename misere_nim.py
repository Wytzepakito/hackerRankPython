def misereNim(s):

    if list(set(s)) == [1]:
        if len(s) % 2 == 0:
            return("First")
        else:
            return("Second")


    nim_sum = s[0]
    for i in range(1, len(s)):
        nim_sum = nim_sum ^ s[i]

    if nim_sum ==0:
        return("Second")
    else:
        return("First")






print(misereNim([1,1]))
print(misereNim([1,1,1]))
print(misereNim([2,1,3]))

print(misereNim([1,2,2]))

    
