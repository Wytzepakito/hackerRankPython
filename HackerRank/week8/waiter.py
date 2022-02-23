import math
import os

def cross_off(bit_map, prime):

    for i in range(prime * prime, len(bit_map), prime):
        bit_map[i] = False


def get_next(bit_map, prime):
    start = prime + 1
    for i in range(start, len(bit_map)):
        if bit_map[i]:
            return i


def seave(max):

    bit_map = [True] * max
    bit_map[0] = False
    bit_map[1] = False
    primes = []
    prime = 2
    primes.append(prime)

    while(prime <= math.sqrt(max)):
        cross_off(bit_map, prime)

        prime = get_next(bit_map, prime)
        primes.append(prime)
    return primes



def waiter(number,q):
    maxi = 1000
    primes = seave(maxi)

    while(len(primes) < q):
        maxi = maxi * 10
        primes = seave(maxi)

    result = []
    while(q != 0):
        prime = primes.pop(0)

        new_nums = []
        temp_result = []

        for num in number[::-1]:
            if num % prime == 0:
                temp_result.append(num)
            else:
                new_nums.append(num)
        result.extend(temp_result[::-1])
        q -= 1
        number = new_nums
    result.extend(number[::-1])
    return result





#print(waiter([2, 3, 4, 5, 6, 7], 3))
#print(waiter([3, 4, 7, 6, 5], 1))
#print(waiter([3, 3, 4, 4, 9], 2))


#print(waiter([80, 37, 86, 79, 8, 39, 43, 41, 15, 33, 30, 15, 45, 55, 61, 74, 49, 49, 20, 66, 77, 19, 85, 44, 81, 82, 27, 5, 36, 83, 91, 45, 39, 44, 19, 44, 71, 49, 8, 66, 81, 40, 29, 60, 35, 31, 44], 21))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
