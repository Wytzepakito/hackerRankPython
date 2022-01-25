import itertools
import math
def get_xor_val(n):
    count = 0
    while(n != 0):
        n = n >> 1
        count += 1
    return 2 ** (count ) - 1


def sumXor(n):
    # Write your code here


    n = get_xor_val(n) ^ n
    bit_string = "{:08b}".format(n)
    indices = []

    for i,bit in enumerate(bit_string[::-1]):
        if bit =="1":
            indices.append(i)

    num = len(indices)
    result = 0
    for i in range(num +1):
        result += math.factorial(num)/(math.factorial(i)*math.factorial(num-i))

    return(int(result))


def sumXor2(n):

    for i in range(n):
        if i + n == i ^ n:
            print(i)
            print("{:08b}".format(i))


print(sumXor(100))
