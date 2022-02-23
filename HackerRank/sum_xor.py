import itertools
import math

def get_highest_pow_2_minus1(n):
    count = 0
    while(n != 0):
        n = n >> 1
        count += 1
    return 2 ** (count ) - 1


def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
        return 0
    return 1
    


def sumXor(n):
    # Write your code here


    n = get_highest_pow_2_minus1(n) ^ n
    bit_string = "{:08b}".format(n)
    indices = []

    for i,bit in enumerate(bit_string[::-1]):
        if bit =="1":
            indices.append(i)


    # The number of subsets of length i of a list is, with length list K:
    # K!/(i! * (K-i)!)
    # So number of lenght 1 subsets of a list of 7:
    # 7!/(1! *(7-1)!) = 7

    num = len(indices)
    result = 0
    for i in range(num +1):
         result += math.factorial(num)/(math.factorial(i)*math.factorial(num-i))

    print(indices)
    subsets_count = 2 ** len(indices)
    sets = []
    for i in range(subsets_count):
        st = set([])
        for j in range(0, len(indices)):
            if get_bit(i, j) ==1:
                st.add(indices[j])
        sets.append(st)
    print(sets)





    return(int(result))





print(sumXor(100))
