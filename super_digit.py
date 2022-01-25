


def superDigit(n,k):
    k_copy = k

    while k_copy != 0:
        superdigit = 0
        string = str(n)

        for char in string:
            superdigit += int(char)
        n = superdigit
        k_copy -= 1
    print(n)
    result = n * k
    print(result)
    final_answer = 0
    for char in str(result):
        final_answer += int(char)
    return final_answer
    

print(superDigit(9875, 4))
